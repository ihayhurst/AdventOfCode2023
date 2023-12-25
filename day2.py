"""
Task 1 Time Taken: 2.55 ms

test={"red":12, "green":13, "blue":14}
Sum the game ID of games that were possible with the test set of cubes
"""
import re, time


start = time.time()
valid = []
valid= set(valid)
with open("day2-input.txt", "rt") as f:
    input=f.readlines()
    for game in input:
        game = game.split(';')
        game_id=[int(x) for x in (re.findall(r"Game (\d+)", game[0]))]
        pullcount =0 
        for pull in game:
            red=[int(x) for x in (re.findall(r"(\d+) red", pull))]
            if red and red[0]>12:
                valid.discard(game_id[0])
                break
            green=[int(x) for x in (re.findall(r"(\d+) green", pull))]
            if green and green[0]>13:
                valid.discard(game_id[0])
                break
            blue=[int(x) for x in (re.findall(r"(\d+) blue", pull))]
            if blue and blue[0]>14:
                valid.discard(game_id[0])
                break
            pullcount +=1
        if pullcount == len(game):
            valid.add(game_id[0])
delta = time.time() - start
print("task took %.2f ms" % (delta * 1000))
print(valid)
print (sum(valid))
        
