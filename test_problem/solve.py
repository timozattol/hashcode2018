import sys
import numpy as np

lines = sys.stdin.readlines()
lines = [line.strip() for line in lines]

R, C, L, H = [int(x) for x in (lines[0].split())]

#print(R,C,L,H)

pizza = lines[1:]

#print(pizza)

if H > C:
    H = R

slices = []

for i in range(R):
    for j in range(0, C - H, H):
        chunk = ''.join([pizza[i][j:j + H]])

        if chunk.count('M') >= L and chunk.count('T') >= L:
            slices.append('{} {} {} {}'.format(i, j, i, j + H - 1))



print(len(slices))
print("\n".join(slices))
