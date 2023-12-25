"""
Task 2 Time taken: 1.99 ms
Sum of each game where the minimun number of each colour of cube required to make it possible is multiplied


"""
import re, time


start = time.time()
game_total = 0
with open("day2-input.txt", "rt") as f:
    input=f.readlines()
    for game in input:
        
        red=[int(x) for x in (re.findall(r"(\d+) red",game ))]
        green=[int(x) for x in (re.findall(r"(\d+) green", game))]
        blue=[int(x) for x in (re.findall(r"(\d+) blue", game))]
        game_total += max(red)*max(green)*max(blue)

delta = time.time() - start
print("task took %.2f ms" % (delta * 1000))
print(game_total)
        
