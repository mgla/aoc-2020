#! /usr/bin/env python3
import sys
import aocd

nums = [int(n) for n in aocd.get_data(year=2020, day=1).splitlines()]

for num1 in nums:
    left = 2020 - num1
    d = {}
    for num2 in nums:
        if num1 == num2: continue
        d[left - num2] = [num1, num2]
        if num2 in d:
            res = d[num2][0] * d[num2][1] * num2
            print('Answer: ', res)
            aocd.submit(res, part="b", year=2020, day=1)
            sys.exit(0)
