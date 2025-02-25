from pandas import DataFrame


class Sudoku:
    def __init__(self, raw):
        values = [[int(cell) for cell in list(row.replace(" ", "0"))] for row in raw]
        self.status = DataFrame(values)

    def out(self):
        print(("+---" * 9) + "+")

        for rowIndex in range(9):
            line = "|"
            for colIndex in range(9):
                value = self.getPrettyValue(rowIndex, colIndex)
                line += f" {value} "
                if colIndex % 3 == 2:
                    line += "|"
                else:
                    line += " "
            print(line)
            if rowIndex % 3 == 2:
                print(("+---" * 9) + "+")
            else:
                print(("+   " * 9) + "+")

    def getPrettyValue(self, rowIndex, colIndex):
        value = self.getValue(rowIndex, colIndex)
        return " " if value == 0 else str(int(value))

    def inRow(self, val, index):
        return val in self.getRow(index).values

    def inColumn(self, val, index):
        return val in self.getCol(index).values

    def inSection(self, val, rowIndex, columnIndex):
        return val in self.getSection(rowIndex, columnIndex).values

    def getValue(self, rowIndex, columnIndex):
        return self.status.at[rowIndex, columnIndex]

    def setValue(self, val, rowIndex, columnIndex):
        self.status.at[rowIndex, columnIndex] = val

    def isPossible(self, val, rowIndex, columnIndex):
        inRow = self.inRow(val, rowIndex)
        inColumn = self.inColumn(val, columnIndex)
        inSection = self.inSection(val, rowIndex, columnIndex)
        return not inRow and not inColumn and not inSection

    def getRow(self, index):
        if index not in range(0, 9):
            raise Exception("Index {} not in range".format(index))
        return self.status.iloc[index : index + 1]

    def getCol(self, index):
        if index not in range(0, 9):
            raise Exception("Index {} not in range".format(index))
        return self.status[index]

    def getSection(self, rowIndex, columnIndex):
        if rowIndex not in range(0, 9):
            raise Exception("Index {} not in range".format(rowIndex))
        if columnIndex not in range(0, 9):
            raise Exception("Index {} not in range".format(columnIndex))

        rowStart, rowEnd = self.getIndicesForSection(rowIndex)
        colStart, colEnd = self.getIndicesForSection(columnIndex)

        return self.status.iloc[rowStart:rowEnd, colStart:colEnd]

    def getIndicesForSection(self, index):
        if index in [0, 1, 2]:
            return 0, 3
        elif index in [3, 4, 5]:
            return 3, 6
        else:
            return 6, 9

    def _getColIndicesForSection(self, index):
        if index in [0, 3, 6]:
            return 0, 3
        elif index in [1, 4, 7]:
            return 3, 6
        else:
            return 6, 9

    def isSolved(self):
        return not self.status.eq(0).any().any()

    def solve(self):
        self.out()
        solution = self.recursive_solve()
        if solution:
            print("Solved!")
            self.out()
        else:
            print("No solution found!")

    def recursive_solve(self):
        if self.isSolved():
            return True
        for rowIndex in range(9):
            for columnIndex in range(9):
                if self.getValue(rowIndex, columnIndex) != 0:
                    continue
                else:
                    for attempt in range(1, 10):
                        if self.isPossible(attempt, rowIndex, columnIndex):
                            self.setValue(attempt, rowIndex, columnIndex)
                            if self.recursive_solve():
                                return True
                            else:
                                self.setValue(0, rowIndex, columnIndex)
                    return False


#############################################
# This is the code that runs, and calls the
# Sudoku class
#############################################
print("Input a puzzle")
print("Use spaces or 0's for blanks, non-zero numbers for filled in squares")
print("At the end of each row, press [Enter]")
print("There should be 9 characters in each line.")
print("In other words, your line (including the prompt), whould end up")
print("this long:")
print("        -------->")
row1 = input("Row 1:  ")
row2 = input("Row 2:  ")
row3 = input("Row 3:  ")
row4 = input("Row 4:  ")
row5 = input("Row 5:  ")
row6 = input("Row 6:  ")
row7 = input("Row 7:  ")
row8 = input("Row 8:  ")
row9 = input("Row 9:  ")

sudokuRaw = [row1, row2, row3, row4, row5, row6, row7, row8, row9]

s = Sudoku(sudokuRaw)
s.solve()
