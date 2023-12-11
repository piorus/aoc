import os
import re

with open('{}/input'.format(os.path.dirname(__file__)), 'r') as f:
    galaxy_matrix = [re.findall(r"(.)", line) for line in f.readlines()]


def expand(matrix):
    result = []

    for x, row in enumerate(matrix):
        if all([col == '.' for col in row]):
            print('append row {}'.format(x))
            result.append(row)
        result.append(row)

    cols_added = 0

    for y, col in enumerate(matrix[0]):
        if all([matrix[x][y] == '.' for x, row in enumerate(matrix)]):
            print('append col {}'.format(y))
            for x, v in enumerate(result):
                result[x] = result[x][:y + cols_added] + ['.'] + result[x][y + cols_added:]

            cols_added += 1

    return result


space = expand(galaxy_matrix)
galaxies = [(x, y) for x, row in enumerate(space) for y, col in enumerate(row) if col != '.']

solution = 0

for i, p1 in enumerate(galaxies):
    for p2 in galaxies[i + 1:]:
        a = abs(p1[0] - p2[0])
        b = abs(p1[1] - p2[1])
        solution += (a + b)

print(solution)