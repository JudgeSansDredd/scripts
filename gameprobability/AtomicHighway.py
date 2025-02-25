from itertools import product

from tabulate import tabulate


def createDiceArray(numDice):
    rolls = product(range(1, 7), repeat=numDice)
    return [list(sorted(x, reverse=True)) for x in rolls]

def addSkill(diceRoll, skillScore):
    newDiceRoll = []
    for die in diceRoll:
        modified = die + skillScore
        skillScore = modified - 6 if modified > 6 else 0
        modified = 6 if modified > 6 else modified
        newDiceRoll.append(modified)
    return newDiceRoll

def getNumSuccesses(diceRoll, skillScore):
    modifiedRoll = addSkill(diceRoll, skillScore)
    return len([x for x in modifiedRoll if x == 6])

def calculateForStatArray(target, mutantsScore, skillScore):
    # How many successes in each possible roll?
    successesPerRoll = [
        getNumSuccesses(diceRoll, skillScore)
        for diceRoll
        in createDiceArray(mutantsScore)
    ]
    # How many rolls did we make?
    numRolls = len(successesPerRoll)

    # Number that met target
    numSuccesses = len([
        x
        for x
        in successesPerRoll
        if x >= target
    ])
    return f'{round(numSuccesses / numRolls * 100, 1)}%'

def printTargetChart(target):
    headers = ['Skill']
    headers.extend(range(6))
    tableData = [['MUTANTS Score', *[''] * 6]]
    for mutantsScore in range(1, 6):
        row = [mutantsScore]
        for skillScore in range(6):
            cell = calculateForStatArray(target, mutantsScore, skillScore)
            row.append(cell)
        tableData.append(row)
    print(tabulate(tableData, headers))


if __name__ == '__main__':
    for i in range(1, 6):
        successString = 'successes' if i > 1 else 'success'
        formattedString = f'Target: {i} {successString}'
        print('*' * (len(formattedString) + 4))
        print(f'* {formattedString} *')
        print('*' * (len(formattedString) + 4))
        printTargetChart(i)
        print('\n\n')
