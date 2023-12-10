import os
import re
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

with open('{}/input'.format(os.path.dirname(__file__)), 'r') as f:
    pipe_lines = [re.findall(r"(.)", line) for line in f.readlines()]

starting_point = None

for x, pipes in enumerate(pipe_lines):
    for y, pipe in enumerate(pipes):
        if pipe == 'S':
            starting_point = (x, y)
            break

if not starting_point:
    raise Exception('starting point is missing')

MOVE_LEFT = 1
MOVE_RIGHT = 2
MOVE_UP = 4
MOVE_DOWN = 8

pipe_movements = {
    '|': {
        'in': MOVE_UP | MOVE_DOWN,
        'out': MOVE_UP | MOVE_DOWN,
    },
    '-': {
        'in': MOVE_LEFT | MOVE_RIGHT,
        'out': MOVE_LEFT | MOVE_RIGHT,
    },
    'L': {
        'in': MOVE_DOWN | MOVE_LEFT,
        'out': MOVE_UP | MOVE_RIGHT,
    },
    'J': {
        'in': MOVE_DOWN | MOVE_RIGHT,
        'out': MOVE_UP | MOVE_LEFT
    },
    '7': {
        'in': MOVE_UP | MOVE_RIGHT,
        'out': MOVE_DOWN | MOVE_LEFT,
    },
    'F': {
        'in': MOVE_UP | MOVE_LEFT,
        'out': MOVE_DOWN | MOVE_RIGHT,
    },
    'S': {
        'in': MOVE_UP | MOVE_DOWN | MOVE_LEFT | MOVE_RIGHT,
        'out': MOVE_UP | MOVE_DOWN | MOVE_LEFT | MOVE_RIGHT,
    }
}

x_boundary = (0, len(pipe_lines) - 1)
y_boundary = (0, len(pipe_lines[0]) - 1)
p = starting_point
prev_p = None
pipe = 'S'
cycle_found = False

polygon_points = [starting_point]

while not cycle_found:
    out_movement = pipe_movements.get(pipe).get('out')
    possible_movements = [
        (move, vec)
        for move, vec in [
            (MOVE_UP, [-1, 0]),
            (MOVE_DOWN, [1, 0]),
            (MOVE_LEFT, [0, -1]),
            (MOVE_RIGHT, [0, 1])
        ]
        if move & out_movement
    ]

    for move, vec in possible_movements:
        x_diff, y_diff = vec
        next_p = (p[0] + x_diff, p[1] + y_diff)

        if (
                x_boundary[0] <= next_p[0] <= x_boundary[1]
                and y_boundary[0] <= next_p[1] <= y_boundary[1]
                and prev_p != next_p
                and pipe_lines[next_p[0]][next_p[1]] != '.'
        ):
            next_pipe = pipe_lines[next_p[0]][next_p[1]]
            can_move = pipe_movements.get(next_pipe).get('in') & move

            if can_move and next_pipe == 'S':
                cycle_found = True
                break

            if can_move:
                pipe = next_pipe
                prev_p = p
                p = next_p
                polygon_points.append(next_p)
                break

polygon = Polygon(polygon_points)

points_inside = 0

for x, pipes in enumerate(pipe_lines):
    for y, pipe in enumerate(pipes):
        if (pipe not in pipe_movements.keys() or (x, y) not in polygon_points) and polygon.contains(Point(x, y)):
            points_inside += 1

print(points_inside)