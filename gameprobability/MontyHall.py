import os
import random

from whiptail import Whiptail

TERMINAL_WIDTH = os.get_terminal_size().columns
TERMINAL_HEIGHT = os.get_terminal_size().lines

WHIPTAIL_SETTINGS = {
    "title": "Monty Hall",
    "width": TERMINAL_WIDTH - 10,
    "height": TERMINAL_HEIGHT - 10,
}


def run_experiment():
    doors = ["car", "goat", "goat"]
    selected = random.choice(doors)
    keep_win = selected == "car"
    return keep_win


def main():
    wt = Whiptail(**WHIPTAIL_SETTINGS)
    (
        num_experiments,
        res,
    ) = wt.inputbox("How many times do you want to attempt?", "1")
    if res == 1:
        exit()
    keep_wins = 0
    change_wins = 0
    for _ in range(int(num_experiments)):
        keep_win = run_experiment()
        keep_wins = keep_wins + 1 if keep_win else keep_wins
        change_wins = change_wins + 1 if not keep_win else change_wins
    print(f"Keep wins: {keep_wins}")
    print(f"Change wins: {change_wins}")


if __name__ == "__main__":
    main()
