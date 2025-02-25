import random

NUM_SIMS = 1_000_000

def roll():
    return random.randint(1, 20)

def roll_save():
    result = roll()
    if result == 1:
        return 0, 2
    elif result == 20:
        return 3, 0
    elif result < 10:
        return 0, 1
    else:
        return 1, 0

def do_saves():
    successes = 0
    failures = 0
    while successes < 3 and failures < 3:
        newSuccesses, newFailures = roll_save()
        successes += newSuccesses
        failures += newFailures
    return successes >= 3

def main():
    attempts = [do_saves() for _ in range(NUM_SIMS)]
    successes = sum(attempts)
    failures = NUM_SIMS - successes

    print(f"Successes: {successes}")
    print(f"Failures: {failures}")
    print(f"Percentage: {round(successes / NUM_SIMS * 100, 2)}%")


if __name__ == '__main__':
    main()
