#! /usr/bin/env python3
import aocd

nums = [int(n) for n in aocd.get_data(year=2020, day=1).splitlines()]

d = {}
for num in nums:
    d[num] = True
    if 2020-num in d:
        print('Answer: ', num * (2020 - num))
        aocd.submit(num * (2020 - num), part="a", year=2020, day=1)
