"""
Advent of Code Day 3  - Task 2
Convert task 1 to only reguard "*" symbols
where there are 2 ajacent part numbers, multiply them and return that as valid part for sum
Task 2 Result 80403602 Time taken:27.08 ms
"""
import numpy as np
import time

start = time.time()
matrix = np.fromfile("day3-input.txt", dtype="S1").reshape(140, 141)
valid_symbols = "*"
valid_parts = []


def castabout(ix, iy):
    adj = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            rangeX = range(0, matrix.shape[0])
            rangeY = range(0, matrix.shape[1])

            (newX, newY) = (ix + dx, iy + dy)

            if (newX in rangeX) and (newY in rangeY) and (dx, dy) != (0, 0):
                adj.append((newX, newY))

    return adj


def traverse(x, y):
    # Decrement y until cell value is not a digit (return index of digit range start)
    digit = True
    while digit:
        y -= 1
        if (matrix[x, y].decode("UTF-8")).isnumeric():
            digit = True
        else:
            digit = False

    numstart = y + 1
    return numstart


def scan(x, y):
    # Increment y until cell value is not a digit (return  index of digit end (+1) for easy ranges)
    digit = True
    while digit:
        y += 1
        if matrix[x, y].decode("UTF-8").isnumeric():
            digit = True
        else:
            digit = False
    numend = y
    return numend


for ix, iy in np.ndindex(matrix.shape):
    val = (matrix[ix, iy]).decode("UTF-8")
    if val in valid_symbols:
        #print(f"{val} - [{ix=}, {iy=}]")
        surround = castabout(ix, iy)
        numstart, numend = 0,0
        gears=[]
        gearratio=0
        for cords in surround:
            point = matrix[cords[0], cords[1]].decode("UTF-8")
            if cords[0] == ix: numend=numstart # prevent range overlap carry over to bottom row
            if point.isnumeric() and cords[1] not in range(numstart,numend):
                numstart = traverse(cords[0], cords[1])
                numend = scan(cords[0], numstart)
                partrange = matrix[cords[0], numstart:numend]
                partnumber = "".join([d.decode("UTF-8") for d in partrange])
                #print(int(partnumber))
                gears.append(int(partnumber))
        if len(gears) == 2:
            gearratio= np.prod(gears)
            valid_parts.append(int(gearratio))


print(sum(valid_parts))
delta = time.time() - start
print("task took %.2f ms" % (delta * 1000))
