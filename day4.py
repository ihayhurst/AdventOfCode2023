"""
Advent of Code 2023 day 4
Task 1: 17782 Time taken 2.02 ms
"""
import time


start = time.time()
sum = 0
lines=[]
with open("day4-input.txt", "rt") as f:
    for file_line in f:
        lines.append(file_line.strip())

# file_line = f.readlines()
for line in lines:
    data = line.split("|")
    winning_nums = [int(d) for d in data[0].split() if d.isdigit()]
    our_nums = [int(d) for d in data[1].split() if d.isdigit()]
    result = [w for w in our_nums if w in winning_nums]
    if result:
        sum += 2 ** (len(result) - 1)

print(sum)
delta = time.time() - start
print("task took %.2f ms" % (delta * 1000))
