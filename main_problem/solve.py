import sys
import numpy as np

lines = sys.stdin.readlines()
lines = [line.strip() for line in lines]


def distance(x0, y0, x1, y1):
    return abs(x1 - x0) + abs(y1 - y0)
