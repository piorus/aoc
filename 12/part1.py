import os
import re
import itertools

with open('{}/input'.format(os.path.dirname(__file__)), 'r') as f:
    groups = [
        (cipher, list(map(int, sequence.split(","))))
        for line in f.readlines()
        for cipher, sequence in re.findall(r"(.*) (.*)", line)
    ]

total = 0
groups = [groups[5]]

for cipher, sequence in groups:
    num_unknown = sum([1 for c in cipher if c == '?'])
    sorted_sequence = sorted([list(j) for i, j in itertools.groupby(sequence)], key=lambda x: x[0])
    for p in list(itertools.product(['#', '.'], repeat=num_unknown)):
        transpiled_cipher = cipher
        for c in p:
            transpiled_cipher = re.sub(r"\?", c, transpiled_cipher, 1)

        print(transpiled_cipher)

        arrangement = list(map(len, re.findall(r"(#+)", transpiled_cipher)))
        sorted_arrangement = sorted([list(j) for i, j in itertools.groupby(arrangement)], key=lambda x: x[0])
        if sorted_arrangement == sorted_sequence:
            total += 1

