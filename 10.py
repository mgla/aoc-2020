#! /usr/bin/env python3
import aocd
from pprint import pprint

nums = [int(n) for n in aocd.get_data(year = 2020, day = 10).splitlines()]

min = 0
max = nums[0]
adapters = {}
targets = {}
for num in nums:
    if num > max: max = num
    assert(min < num)
    adapters[num] = True
    for i in range(3): targets[num + 1 + i] = True

ones = 0
twos = 0
threes = 0

jolt = min
while jolt < max:
    # count ones and threes for path selecting all adapters
    assert((jolt == 0) or adapters[jolt])
    if jolt + 1 in adapters:
        ones += 1
        jolt += 1
    elif jolt + 2 in adapters:
        jolt += 2
        twos += 1 # no twos in my puzzle, strangely
    else:
        threes += 1
        jolt += 3

# final joltage
threes += 1
assert(ones + twos + threes == len(nums) + 1)
print(ones * threes)
