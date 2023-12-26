"""
Done -load matrix into numpy array
Done -scan array for symbols,
Done -castabout for digits in ajacent cells
Done -identify the number those digits are from
        would be easier to find numbers the check they are valid by using the castabout to find symbols
Done -sum the valid part numbers
TODO -fix getting part numbers you have already (but allowing genuine duplicate parts elsewhere)
"""
import numpy as np
import time

start = time.time()
matrix = np.fromfile("day3-input.txt", dtype="S1").reshape(140, 141)
# valid_symbols = "!@#$%^&*()_-+={}[]"
valid_symbols = "#%&*+-/=@$"
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
        print(f"{val} - [{ix=}, {iy=}]")
        surround = castabout(ix, iy)
        # print(f"{surround}") #list of bounding coords
        for cords in surround:
            point = matrix[cords[0], cords[1]].decode("UTF-8")
            if point.isnumeric():
                # print(f"{point} - [{cords[0],cords[1]}]")
                # scan(cords[0],traverse(cords[0], cords[1]))
                numstart = traverse(cords[0], cords[1])
                numend = scan(cords[0], numstart)
                partrange = matrix[cords[0], numstart:numend]
                partnumber = "".join([d.decode("UTF-8") for d in partrange])
                print(int(partnumber))
                valid_parts.append(int(partnumber))


print(sum(valid_parts))
delta = time.time() - start
print("task took %.2f ms" % (delta * 1000))
