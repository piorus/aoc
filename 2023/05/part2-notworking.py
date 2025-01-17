import os
import re

with open('{}/input'.format(os.path.dirname(__file__)), 'r') as f:
    lines = f.readlines()
    source_ranges = {}
    destination_ranges = {}
    source = None
    destination = None
    source_to_destination_map = {}
    destination_to_source_map = {}
    for line in lines[1:]:
        source_and_destination = re.match(r"(\w+)-to-(\w+)", line)
        if source_and_destination:
            source = source_and_destination.group(1)
            destination = source_and_destination.group(2)
            source_to_destination_map[source] = destination
            destination_to_source_map[destination] = source

        mapping = list(map(int, re.findall(r"(\d+)", line)))
        if len(mapping):
            source_ranges[source] = source_ranges.get(source, []) + [mapping]
            destination_ranges[destination] = destination_ranges.get(destination, []) + [mapping]

    seeds = list(map(int, re.findall(r"(\d+)", lines[0])))
    chunked_seeds = [seeds[i:i + 2] for i in range(0, len(seeds), 2)]

    for i, chunked_seed in enumerate(chunked_seeds):
        seed_start, seed_length = chunked_seed
        source = 'seed'
        while source in source_to_destination_map:
            for destination_range_start, source_range_start, range_length in source_ranges.get(source):
                if source_range_start <= seed_start <= source_range_start + range_length:
                    chunked_seeds[i] = [
                        destination_range_start + (seed_start - source_range_start),

                    ]
            source = source_to_destination_map.get(source)
    # locations = []
    #
    # location_ranges = sorted([
    #     [destination_range_start, destination_range_start + range_length - 1]
    #     for destination_range_start, source_range_start, range_length in destination_ranges.get('location')
    # ], key=lambda x: x[0])

    # smallest possible upside-down
    # smaller than smallest
    #
    # min_location = None
    #
    # print(location_ranges)
    #
    # for location in range():
    #     destination = 'location'
    #     destination_value = location
    #     while destination in destination_to_source_map:
    #         for destination_range_start, source_range_start, range_length in destination_ranges.get(destination):
    #             if destination_range_start <= destination_value <= destination_range_start + range_length:
    #                 destination_value = destination_value + (source_range_start - destination_range_start)
    #                 break
    #         destination = destination_to_source_map.get(destination)
    #
    #     for seed_start, seed_length in chunked_seeds:
    #         if seed_start <= destination_value <= seed_start + seed_length:
    #             if min_location is None or location < min_location:
    #                 min_location = location
    #
    # print(min_location)

    # treat out of ranges as possible solution, try to eliminate them
    # for seed in range(seed_start, seed_start + seed_length + 1):
    # for seed in range(1, 20):
    # source = 'seed'
    #
    #     source = source_to_destination_map.get(source)
    # locations.append(destination_value)
    # print(min(locations))
    #
    # for seed_start, seed_length in chunked_seeds:
    #     for seed in range(seed_start, seed_start + seed_length + 1):
    #         # for seed in range(1, 20):
    #         # source = 'seed'
    #         destination = 'location'
    #         source_value = 'asdf'
    #         while source in source_to_destination_map:
    #             for destination_range_start, source_range_start, range_length in source_ranges.get(source):
    #                 if source_range_start <= source_value <= source_range_start + range_length:
    #                     # print('seed = {} {} {} <{}, {}>'.format(seed, source, source_value, source_range_start, source_range_start + range_length))
    #                     source_value = source_value + (destination_range_start - source_range_start)
    #                     break
    #             source = source_to_destination_map.get(source)
    #         locations.append(source_value)
    # print(min(locations))
