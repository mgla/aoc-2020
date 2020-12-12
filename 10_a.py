#! /usr/bin/env python3
import aocd

nums = [int(n) for n in aocd.get_data(year=2020, day=10).splitlines()]

min_j = 0
max_j = nums[0]
adapters = {}
targets = {}
for num in nums:
    if num > max_j: max_j = num
    assert min_j < num
    adapters[num] = True
    for i in range(3): targets[num + 1 + i] = True

ones = 0
twos = 0
threes = 0

jolt = min_j
while jolt < max_j:
    # count ones and threes for path selecting all adapters
    assert (jolt == 0) or adapters[jolt]
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
assert ones + twos + threes == len(nums) + 1
print(ones * threes)
