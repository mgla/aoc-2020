#! /usr/bin/env python3
import aocd

(departure, busses) = aocd.get_data(year=2020, day=13).splitlines()
departure = int(departure)
busses = list(map(int, filter(lambda x: x != 'x', busses.split(','))))

fastest_t = departure + busses[0] - departure % busses[0]
fastest_b = busses[0]

for bus in busses:
    departure_t = departure + bus - (departure % bus)
    assert departure % bus != 0
    if departure_t < fastest_t:
        fastest_t = departure_t
        fastest_b = bus

res = fastest_b * (fastest_t - departure)
print('Answer: ', res)
aocd.submit(res, part="a", year=2020, day=13)
