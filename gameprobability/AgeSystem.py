
def evaluate(dc, i, j, k):
    result = i + j + k + 3
    success = result >= dc
    hasStunts = i == j or j == k or i == k
    return success, hasStunts, i + 1

def runAllDice(dc):
    numFailures = 0
    numSuccesses = 0
    arrStunts = []
    for i in range(6):
        for j in range(6):
            for k in range(6):
                success, hasStunts, stunts = evaluate(dc, i, j, k)
                if success:
                    numSuccesses += 1
                    if hasStunts:
                        arrStunts.append(stunts)
                else:
                    numFailures += 1
    numStunts = len(arrStunts)
    total = numFailures + numSuccesses
    stuntPercent = round(numStunts / total * 100, 2)
    successPercent = round(numSuccesses / total * 100, 2)
    averageStunts = sum(arrStunts) / numStunts
    return successPercent, stuntPercent, averageStunts

def main():
    for dc in range(2, 18):
        successPercent, stuntPercent, averageStunts = runAllDice(dc + 1)
        print(f"DC: {dc + 1}")
        print(f"Successes: {successPercent}%")
        print(f"Stunt Percent: {stuntPercent}%")
        print(f"Average Stunts: {averageStunts}")
        print("-------------------------")

if __name__ == '__main__':
    main()
