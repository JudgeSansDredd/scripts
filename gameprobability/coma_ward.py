import random


def rollDie():
    # TODO: Finish this roll die method
    roll = random.randint(1, 6)
    if roll == 4:
        rolls = []
        rolls.extend(rollDie())
        rolls.extend(rollDie())
    else:
        rolls = [roll]
    return rolls

def determineProbability(target, dice):
    numAttempts = 100000
    numSuccesses = 0
    for _ in range(numAttempts):
        rolls = [rollDie() for _ in range(dice)]
        successRolls = [roll for group in rolls for roll in group if roll > 4]
        numSuccesses = numSuccesses + 1 if len(successRolls) >= target else numSuccesses
    return round((numSuccesses / numAttempts) * 100)

def main():
    targetNumber = 3
    numDice = 5
    probability = determineProbability(targetNumber, numDice)
    print(probability)

if __name__ == "__main__":
    main()
