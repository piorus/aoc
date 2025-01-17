import os
import re

with open('{}/input'.format(os.path.dirname(__file__)), 'r') as f:
    lines = f.readlines()
    value_maps = {}
    source = None
    destination = None
    source_to_destination_map = {}
    for line in lines[1:]:
        source_and_destination = re.match(r"(\w+)-to-(\w+)", line)
        if source_and_destination:
            source = source_and_destination.group(1)
            destination = source_and_destination.group(2)
            source_to_destination_map[source] = destination

        mapping = list(map(int, re.findall(r"(\d+)", line)))
        if len(mapping):
            # VERY MUCH NOT OPTIMAL
            # destination_range_start, source_range_start, range_length = mapping
            # destination_range = list(range(destination_range_start, destination_range_start + range_length))
            # source_range = list(range(source_range_start, source_range_start + range_length))
            # value_maps[source] = {**value_maps.get(source, {}), **dict(zip(source_range, destination_range))}
            value_maps[source] = value_maps.get(source, []) + [mapping]

    seeds = list(map(int, re.findall(r"(\d+)", lines[0])))
    locations = []
    for seed in seeds:
        source = 'seed'
        source_value = seed
        while source in source_to_destination_map:
            for destination_range_start, source_range_start, range_length in value_maps.get(source):
                if source_range_start <= source_value <= source_range_start + range_length:
                    source_value = source_value + (destination_range_start - source_range_start)
                    break
            source = source_to_destination_map.get(source)
        locations.append(source_value)

    print(min(locations))