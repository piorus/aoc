import os
import re

digit_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}
# source: https://topaz.github.io/paste/#XQAAAQCTCQAAAAAAAAAyGUj/TtE37nHm9MbTqXp4hXzri19W5QR9fKZQPCX+oeMV3ji3GpljQOHuqQbhygWEIsPFCOQIk4UHotA/tsEOIhYBmp5z3p34WCKwFkPGgOZfcamAK7LZOrC/cLSoFEBSq2NrM53p+1uxE//7PfLIiY4eq0qmt6rgry5WvbuVDJ2rHsfk3ZSBfeWkcQqEQvFLlqI6/oXKvrU55zXY75GydNHc6N3CtTKynLIaDYKZuTVZPkjuGAFjRpW7BD3/aX+12Hf9ToVC7XWNGRA9pO+M5ZwvaKHxz0KrcEPqHDmtzsChl8WBL1qmeKpi2JR9F1O8vOl9ZCwcAA//v1YKn2sNoBuDsS290NCA+xlJkZ/cNvulxUM1md5aBiSgAO/+dCDtxsIKbE9W4rTF5r0zf+KFv+lenOrL5sdY8NWTpzSElpmV3Z2mnQmLpfNtopEXdMgDwvI2OoTqZNDghz3Q59/qknRcSxmR6nBBFb4BICShkR1Dph3+kaeMjcGt1cQ1bQ76CRzqy46T4GIp1a6qqNBKiI1VvbCzlPKrDv+SuGH0yTiEVwvo1yIssPNDM4UoMTQcULfuEzL13mwb/2+0dL8z16qnG2vIHLcHRFnjf8/3vAo4hAhfWsQVXkIA+iuIw0ZSbZ/RABKUAibvke1v4/0Ew6+a8o6OtGI3zAFZWonygaYlLHoS8L/4Hb5P936eQcfyyRjcGjYi0x+nr03JNi3jSFBYk9zdCCrpjbc9uF4l83h8d7TPDr8tT8M0RSvdcT+wEmY5BaRmCC3Tu/jAjl3wYUn9I5Aby0TaZPO7bhnw1anA9EB1lLiRKBWb23HOBzAOeLO1Pza83OSHTkptZjug/++XFB5jw7cjOF37pTbHJOSCvix/qnC2XA5boXYN0yuUWDcjIeqbdX33KoE3gKQSCXrQZ9EZuBzrY5se8PFfapq1Nm+/U9570zbgF76I1hHCMj7SbT1IuWyrCxQ91C/6RqIEJklxJXv4F7hwAnXxaTUxxrTHakhh/wTf+HLXFhP3IFsqawHu5pHKJ84Js+rnJghzpj8uelI+BIFAsPCSJUrmogLEF6uQvuWh9cc90hBJRVO0VzL0UFvDdWTlTZ1Xk62Mg8Dt4ZTSQAaQIqOti9koK2oro0Cyed7jKh8sU2g1mM/RQg2iV5hlRuxIkNjH6r9sH6uE//ydeT0=
digit_regex = re.compile(r"(?=(\d|" + "|".join(digit_dict) + r"))")


def calibration_number_for_line(line):
    digits = digit_regex.finditer(line)
    next_digit = next(digits)
    first_digit = last_digit = digit_dict.get(
        next_digit.group(1),
        next_digit.group(1),
    )
    try:
        *_, last = digits
        last_digit = digit_dict.get(
            last.group(1),
            last.group(1)
        )
    except ValueError:
        pass

    return int(first_digit + last_digit)


with open('{}/input'.format(os.path.dirname(__file__)), 'r') as f:
    lines = [line.replace('\n', '') for line in f.readlines()]
    print(sum([calibration_number_for_line(line) for line in lines]))
