#! /usr/bin/env python3
import aocd

(departure, busses) = aocd.get_data(year=2020, day=13).splitlines()
busses = list(busses.split(','))
assert busses[0] != 'x'

index = {}
factors = []
for i, bus in enumerate(busses):
  if bus != 'x':
      factors += [int(bus)]
      index[int(bus)] = i

check = 100000000000000
res = -1
inc = 1
verified_f = -1

searching = True
while searching:
    possible = True
    f = verified_f + 1
    found = False
    while possible:
        if (check + index[factors[f]]) % factors[f] == 0:
            inc *= factors[f]
            verified_f += 1
            f += 1
            if f == len(factors):
                searching = False
                res = check
                break
        else:
            possible = False
    check += inc

print('Answer: ', res)
aocd.submit(res, part="b", year=2020, day=13)
