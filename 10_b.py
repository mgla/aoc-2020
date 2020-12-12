#! /usr/bin/env python3
import aocd
nums = [int(n) for n in aocd.get_data(year=2020, day=10).splitlines()]

max_j = nums[0]
adapters = {}
targets = {}
for num in nums:
    if num > max_j: max_j = num
    assert 0 < num
    adapters[num] = True
    for i in range(3): targets[num + 1 + i] = True
max_j += 3
ways = 1

jolt = 0
visited = {}
win = {0: 1}
todo = []

while jolt < max_j:
    visited[jolt] = True
    options = []
    assert (jolt == 0) or adapters[jolt]
    for i in range(3):
        check = jolt + i + 1
        if check in adapters:
            options += [check]
    assert len(options) > 0 or jolt == max_j - 3
    # cull options to prevent double visits
    for opt in options:
        if opt not in win:
            todo += [opt]
            win[opt] = win[jolt]
        else:
            win[opt] += win[jolt]
    if len(todo) > 0:
        jolt = todo.pop(0)
    else:
        jolt = max_j

print('Answer: ', win[max_j - 3])
aocd.submit(win[max_j -3], part="b", year=2020, day=10)
