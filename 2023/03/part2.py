import os

with open('{}/input'.format(os.path.dirname(__file__)), 'r') as f:
    lines = [line.replace('\n', '') for line in f.readlines()]

    y_boundary = len(lines[0]) - 1
    x_boundary = len(lines) - 1
    nums = {}
    asterisks = {}

    for x, line in enumerate(lines):
        nums[x] = []
        asterisks[x] = []
        num = None
        for cursor_y, c in enumerate(list(line)):
            if c == '*':
                asterisks[x].append({
                    'y_boundary': (cursor_y, cursor_y),
                    'value': '*'
                })
            if c.isnumeric() and num is None:
                num = {
                    'y': cursor_y,
                    'value': ''
                }
            if c.isnumeric() and num is not None:
                num['value'] += c
            if (not c.isnumeric() or cursor_y == x_boundary) and num is not None:
                nums[x].append({
                    'y_boundary': (num.get('y'), num.get('y') + len(num.get('value')) - 1),
                    'value': num.get('value')
                })
                num = None


    def find_gear(x, y):
        for num_boundary in nums[x]:
            y_start, y_end = num_boundary.get('y_boundary')
            if y_start <= y <= y_end:
                return num_boundary


    total_gear_ratios = 0

    for x in asterisks.keys():
        for asterisk in asterisks[x]:
            *_, y = asterisk.get('y_boundary')
            adjacent_gears = [
                find_gear(adjacent_x, adjacent_y)
                for adjacent_x in range(x - 1, x + 1 + 1)
                for adjacent_y in range(y - 1, y + 1 + 1)
                if lines[adjacent_x][adjacent_y].isnumeric()
            ]
            deduplicated_adjacent_gears = [dict(t) for t in {tuple(d.items()) for d in adjacent_gears}]

            if len(deduplicated_adjacent_gears) == 2:
                gear_1, gear_2 = deduplicated_adjacent_gears
                total_gear_ratios += int(gear_1.get('value')) * int(gear_2.get('value'))

    print(total_gear_ratios)
