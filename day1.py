"""
Advent of Code 2023 day 1
Task 1 Time Taken: 3.58 ms
combine first and last digits in each line to make a 2 digit number
sum the total of all lines
Task 2 Time Taken: 7.09 ms
convert the words to digits too before proceeding as in task 1
"""
import time


def parse_text(line):
    lookup = {
        "twone":"21",
        "oneight":"18",
        "fiveight":"58",
        "threeight":"38",
        "nineeight":"98",
        "sevenine":"79",
        "eightwo":"82",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    for word, number in lookup.items():
        line = line.replace(word, number)
    return line


start = time.time()
sum = 0
with open("day1-input.txt", "rt") as f:
    input = f.readlines()
    for line in input:
        line = parse_text(line )
        data = line.split()
        grab = [[int(d) for d in data[0] if d.isdigit()][i] for i in (0, -1)]
        value = grab[0] * 10 + grab[1]
        sum = sum + value
    print(sum)
    delta = time.time() - start
    print("task took %.2f ms" % (delta * 1000))
