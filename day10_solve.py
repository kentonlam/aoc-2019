from util import * 
from collections import defaultdict, deque, namedtuple
from dataclasses import dataclass
from typing import *
import sys

import fractions as frac
from pprint import pprint

import math
# from statistics import mean

INPUT = 'day10_input.txt' if len(sys.argv) == 1 else sys.argv[1]

# import numpy as np 
# import scipy as sp

def parse(lines: List[str]):
    asteroids = set()
    for y, row in enumerate(lines):
        for x, char in enumerate(row):
            if char == '#':
                asteroids.add((x,y))
    return asteroids

def lcm(x, y):
    return x * y // frac.gcd(x, y)



def solve_1(data):
    m = Maxer()
    for centre in data:
        angles = set(math.atan2(other[1] - centre[1], other[0] - centre[0])
            for other in data if other != centre)
        m.update(centre, len(angles))
    return m.get_max()


def solve_2(data):
    def ell2(a, b):
        return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5

    angle = 0
    from itertools import count

    data = set(data)
    centre = (22, 25)
    data.remove(centre)

    def f(other):
        a =( 90 + math.degrees(math.atan2(other[1] - centre[1], other[0] - centre[0])))
        if a < 0: a += 360
        return (a, ell2(centre, other), other)

    d = lmap(f, data)

    angles = set(x[0] for x in d)
    by_angle = {}
    for x in d:
        if x[0] not in by_angle:
            by_angle[x[0]] = []
        by_angle[x[0]].append(x)
    #pprint(by_angle)
    

    angle = 0
    for i in count():
        x = by_angle[angle].pop(0)
        #print(i, x)
        if i == 199: break
        if not by_angle[angle]:
            del by_angle[angle]
            angles.remove(angle)
        angle = min(((a - angle) % 360, a) for a in angles if a != angle)[1]
    return x

if __name__ == "__main__":
    with open(INPUT) as f:
        print('sol 1:', solve_1(parse(f.readlines())))
        print()
        f.seek(0)
        print('sol 2:', solve_2(parse(f.readlines())))