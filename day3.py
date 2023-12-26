"""
Done -load matrix into numpy array
Done -scan array for symbols,
Done -castabout for digits in ajacent cells
TODO -identify the number those digits are from
        would be easier to find numbers the check they are valid by using the castabout to find symbols
TODO -sum the valid part numbers
"""
import numpy as np
import time

start = time.time()
matrix = np.fromfile("day3-input.txt", dtype='S1').reshape(140,141)
#valid_symbols = "!@#$%^&*()_-+={}[]"
valid_symbols = "#%&*+-/=@$"


def castabout(ix, iy):
    adj = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            rangeX = range(0, matrix.shape[0])
            rangeY = range(0, matrix.shape[1])
            
            (newX, newY) = (ix+dx, iy+dy)
            
            if (newX in rangeX) and (newY in rangeY) and (dx, dy) != (0, 0):
                adj.append((newX, newY))
    
    return adj

for ix, iy in np.ndindex(matrix.shape):
   val=(matrix[ix,iy]).decode('UTF-8')
   if val in valid_symbols:
    print(f"{val} - [{ix=}, {iy=}]") 
    surround= castabout(ix,iy)
    print(f"{surround}") #list of bounding coords
    for cords in surround:
       point=(matrix[cords[0],cords[1]].decode('UTF-8'))
       if point.isnumeric():
          print(f"{point} - [{cords[0],cords[1]}]")

"""
for x in np.nditer(matrix, flags=['buffered'], op_dtypes=['S1']):
     print(x)
"""
delta = time.time() - start
print("task took %.2f ms" % (delta * 1000))