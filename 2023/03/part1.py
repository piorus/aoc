import os

with open('{}/input'.format(os.path.dirname(__file__)), 'r') as f:
    lines = [line.replace('\n', '') for line in f.readlines()]

    y_boundary = len(lines[0]) - 1
    x_boundary = len(lines) - 1
    total = 0


    def within_boundary(x, y):
        return 0 <= y <= y_boundary and 0 <= x <= x_boundary


    def not_numeric(x, y):
        return not lines[x][y].isnumeric()


    def is_symbol(x, y):
        return within_boundary(x, y) and not_numeric(x, y) and lines[x][y] != '.'


    for x, line in enumerate(lines):
        num = None
        for cursor_y, c in enumerate(list(line)):
            if c.isnumeric() and num is None:
                num = {
                    'y': cursor_y,
                    'value': ''
                }
            if c.isnumeric() and num is not None:
                num['value'] += c
            if (not c.isnumeric() or cursor_y == x_boundary) and num is not None:
                adjacent_symbols = [
                    lines[adjacent_x][adjacent_y]
                    for adjacent_x in range(x - 1, x + 1 + 1)
                    for adjacent_y in range(num.get('y') - 1, num.get('y') + len(num.get('value')) + 1)
                    if is_symbol(adjacent_x, adjacent_y)
                ]

                if len(adjacent_symbols):
                    total += int(num.get('value'))

                num = None

    print(total)
