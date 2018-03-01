import sys
import numpy as np

lines = sys.stdin.readlines()
lines = [line.strip() for line in lines]

R, C, F, N, B, T = [int(x) for x in (lines[0].split())]

rides = [tuple(map(int, line.split())) for line in lines[1:]]

cars = [([], (0, 0), 0) for c in range(F)]


print(R, C, F, N, B, T)

print(rides)

print(cars)
