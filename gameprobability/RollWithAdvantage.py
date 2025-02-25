import os
from random import randint

from whiptail import Whiptail

TERMINAL_WIDTH = os.get_terminal_size().columns
TERMINAL_HEIGHT = os.get_terminal_size().lines

WHIPTAIL_SETTINGS = {
    "title": f"Die roller",
    "width": TERMINAL_WIDTH - 10,
    "height": TERMINAL_HEIGHT - 10,
}


def determine(die_size):
    rollArray = [0] * die_size
    totalRolls = pow(die_size, 2)

    for i in range(die_size):
        for j in range(die_size):
            roll = max(i, j)
            rollArray[roll] += 1

    weightedValues = [
        (numberOfTimesValueRolled / totalRolls) * (value + 1)
        for value, numberOfTimesValueRolled in enumerate(rollArray)
    ]

    print(f"Expected Value: {sum(weightedValues)}")


def simulate(die_size):
    NUM_ROLLS = 1000000
    rolls = []
    for i in range(NUM_ROLLS):
        x = randint(1, die_size)
        y = randint(1, die_size)
        rolls.append(max(x, y))
    total = sum(rolls)
    print(f"Simulated average: {total/NUM_ROLLS}")


if __name__ == "__main__":
    wt = Whiptail(**WHIPTAIL_SETTINGS)
    strDieSize, res = wt.inputbox("How many sides does your die have?", "20")
    if res == 1:
        exit()
    die_size = int(strDieSize)
    strSimulateOrDetermine, res = wt.menu(
        "Do you want to simulate, or determine mathematically?",
        [
            ["Simulate", "Simulate a large number of rolls"],
            ["Determine", "Use the power of mathematics to calculate it"],
        ],
    )
    if res == 1:
        exit()

    if strSimulateOrDetermine == "Simulate":
        simulate(die_size)
    else:
        determine(die_size)
