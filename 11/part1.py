import os
import re

with open('{}/input'.format(os.path.dirname(__file__)), 'r') as f:
    galaxy_matrix = [re.findall(r"(.)", line) for line in f.readlines()]


def calculate_expansion_points(matrix):
    expanded_rows = []

    for x, row in enumerate(matrix):
        if all([col == '.' for col in row]):
            expanded_rows.append(x)

    expanded_cols = []

    for y, col in enumerate(matrix[0]):
        if all([matrix[x][y] == '.' for x, row in enumerate(matrix)]):
            expanded_cols.append(y)

    return expanded_rows, expanded_cols

expanded_rows, expanded_cols = calculate_expansion_points(galaxy_matrix)

space = galaxy_matrix
galaxies = [(x, y) for x, row in enumerate(space) for y, col in enumerate(row) if col != '.']

expansion_multiplier = 2
solution = 0

for i, p1 in enumerate(galaxies):
    for p2 in galaxies[i + 1:]:
        a = abs(p1[0] - p2[0])
        b = abs(p1[1] - p2[1])

        x_expansion = 0
        y_expansion = 0

        for x in expanded_rows:
            ax = abs(p1[0] - x)
            bx = abs(p2[0] - x)
            if ax + bx == a:
                x_expansion += 1

        for y in expanded_cols:
            ay = abs(p1[1] - y)
            by = abs(p2[1] - y)
            if ay + by == b:
                y_expansion += 1

        solution += (a + b - x_expansion - y_expansion) + (x_expansion * expansion_multiplier) + (y_expansion * expansion_multiplier)

print(solution)