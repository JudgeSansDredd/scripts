from random import choice
from statistics import mean, stdev

DIE_SIZES = [20, 12, 10, 8, 6, 4]
BUST_ROLLS = [1, 2]
NUM_SIMULATIONS = 100_000

def roll_die(num_sides: int) -> int:
    roll = choice(range(num_sides))
    return roll + 1

def get_next_size(current_size: int) -> int:
    current_index = DIE_SIZES.index(current_size)
    return 0 if current_index == len(DIE_SIZES) - 1 else DIE_SIZES[current_index + 1]

def use_until_empty(usage_die: int) -> int:
    num_rolls = 0
    current_die = usage_die
    while current_die != 0:
        num_rolls += 1
        roll = roll_die(current_die)
        if roll in BUST_ROLLS:
            current_die = get_next_size(current_die)
    return num_rolls

def main():
    for usage_die in DIE_SIZES:
        simulations = [use_until_empty(usage_die) for _ in range(NUM_SIMULATIONS)]
        print(usage_die, mean(simulations), stdev(simulations))

if __name__ == '__main__':
    main()
