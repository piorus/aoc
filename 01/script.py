import os
import re

def parse(line):
    res = re.findall('\d', line)
    return int(res[0] + res[-1]) if len(res) > 1 else int(res[0] + res[0])


with open('{}/input'.format(os.path.dirname(__file__)), 'r') as f:
    nums = [parse(line) for line in f]
    print(sum(nums))
