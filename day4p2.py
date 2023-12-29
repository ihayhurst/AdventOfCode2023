"""
Advent of Code 2023 day 4
Task 2 8477787 Time Taken 5.75ms
"""
import time
import numpy as np

INPUT_FILE="day4-input.txt"

def main():
    start = time.time()
    sum = 0
    cards=parse_input(INPUT_FILE)
    structure=np.array(cards)
    structure = np.column_stack((structure, np.ones_like(structure)))
    for i,card in enumerate(structure):
        copies = card[0]*card[1]
        structure[i+1:i+1+card[0], 1] += card[1]
        print(f"{i=} {copies=}")
    print(structure)    
    column_sum = np.sum(structure[:, 1])
    print(column_sum)
    delta = time.time() - start
    print("task took %.2f ms" % (delta * 1000))
    

def parse_input(FILE):
    cards=[]
    with open(FILE, "rt") as f:
        input = f.readlines()

    for line in input:
        data = line.split("|")
        winning_nums = [int(d) for d in data[0].split() if d.isdigit()]
        our_nums = [int(d) for d in data[1].split() if d.isdigit()]
        result =[w for w in our_nums if w in winning_nums]
        cards.append(len(result))
    return cards

if __name__ == "__main__":
    main()