"""
This does stuff
"""
from pandas import DataFrame


class Sudoku:
    """
    This class handles the sudoku puzzle, and helper methods for handling it
    """
    def __init__(self, raw):
        values = [[int(cell) for cell in list(row.replace(" ", "0"))] for row in raw]
        self.status = DataFrame(values)
        self.possible = DataFrame([[[] for y in range(9)] for x in range(9)])
        for row_index in range(9):
            for col_index in range(9):
                self.possible.iat[row_index, col_index] = self.get_initial_possibles(
                    row_index,
                    col_index
                )

    def remove_possible(self, val, row_index, column_index):
        """Removes the value from the possible values at the given index"""
        if val in self.possible.iat[row_index, column_index]:
            self.possible.iat[row_index, column_index].remove(val)

    def remove_possible_related(self, val, row_index, column_index):
        """Removes possible value from all related squares"""
        for x in range(9):
            self.remove_possible(val, row_index, x)
            self.remove_possible(val, x, column_index)
        row_start, row_end = self.get_indices_for_section(row_index)
        col_start, col_end = self.get_indices_for_section(column_index)
        for row in range(row_start, row_end):
            for col in range(col_start, col_end):
                self.remove_possible(val, row, col)
        self.possible.iat[row_index, column_index] = [val]

    def out(self):
        """Prints the current state of the puzzle to the console"""
        print(("+---" * 9) + "+")

        for row_index in range(9):
            line = "|"
            for col_index in range(9):
                value = self.get_pretty_value(row_index, col_index)
                line += f" {value} "
                if col_index % 3 == 2:
                    line += "|"
                else:
                    line += " "
            print(line)
            if row_index % 3 == 2:
                print(("+---" * 9) + "+")
            else:
                print(("+   " * 9) + "+")

    def get_pretty_value(self, row_index, col_index):
        """Escapes 0's and returns a string for the value at the given index"""
        value = self.get_value(row_index, col_index)
        return " " if value == 0 else str(int(value))

    def in_row(self, val, index):
        """Returns True if the value is in the row at the given index, False otherwise"""
        return val in self.get_row(index).values

    def in_column(self, val, index):
        """Returns True if the value is in the column at the given index, False otherwise"""
        return val in self.get_col(index).values

    def in_section(self, val, row_index, column_index):
        """Returns True if the value is in the section at the given index, False otherwise"""
        return val in self.get_section(row_index, column_index).values

    def get_value(self, row_index, column_index, possibles=False):
        """Returns the value at the given index"""
        if row_index not in range(0, 9):
            raise IndexError(f"Row index {row_index} is not in range")
        if column_index not in range(0, 9):
            raise IndexError(f"Column index {column_index} is not in range")
        return (
            self.possible.iat[row_index, column_index]
            if possibles
            else self.status.iat[row_index, column_index]
        )

    def get_initial_possibles(self, row_index, column_index):
        """Returns the initial possible values based on presence in row, col, section"""
        if self.get_value(row_index, column_index) != 0:
            return [self.get_value(row_index, column_index)]
        else:
            return [
                x
                for x
                in range(1, 10)
                if not (
                    self.in_row(x, row_index)
                    or self.in_column(x, column_index)
                    or self.in_section(x, row_index, column_index)
                )
            ]

    def set_value(self, val, row_index, column_index):
        """Sets the value at the given index to the given value"""
        self.status.iat[row_index, column_index] = val
        self.remove_possible_related(val, row_index, column_index)

    def is_possible(self, val, row_index, column_index):
        """Returns True if the value is possible at the given index, False otherwise"""
        return val in self.get_value(row_index, column_index, possibles=True)

    def get_naked_single(self, row_index, column_index):
        """Returns the naked single at the given index"""
        possible = self.get_value(row_index, column_index, possibles=True)
        return possible[0] if len(possible) == 1 else 0

    def is_hidden_single_section(self, val, row_index, column_index):
        """Returns True if the value is a hidden single in the section"""
        is_possible = []
        for row in range(*self.get_indices_for_section(row_index)):
            for col in range(*self.get_indices_for_section(column_index)):
                is_possible.append(self.is_possible(val, row, col))
        return is_possible.count(True) == 1

    def is_hidden_single_row_column(self, val, index, is_row):
        """Returns True if the value is a hidden single in the row or column"""
        is_possible = [
            self.is_possible(
                val,
                index if is_row else x,
                index if not is_row else x
            ) for x in range(9)
        ]
        return is_possible.count(True) == 1

    def is_hidden_single(self, val, row_index, column_index):
        """Returns True if the value is a hidden single"""
        section = self.is_hidden_single_section(val, row_index, column_index)
        row = self.is_hidden_single_row_column(val, row_index, True)
        col = self.is_hidden_single_row_column(val, column_index, False)
        return section or row or col

    def get_row(self, index, possibles=False) -> DataFrame:
        """Returns the row at the given index"""
        if index not in range(0, 9):
            raise IndexError(f"Index {index} not in range")
        return (
            self.possible.iloc[index : index + 1]
            if possibles
            else self.status.iloc[index : index + 1]
        )

    def get_col(self, index, possibles=False) -> DataFrame:
        """Returns the column at the given index"""
        if index not in range(0, 9):
            raise IndexError(f"Index {index} not in range")
        return self.possible[index] if possibles else self.status[index]

    def get_section(self, row_index, column_index, possibles=False) -> DataFrame:
        """Returns the section at the given index"""
        if row_index not in range(0, 9):
            raise ValueError(f"Row index {row_index} is not in range")
        if column_index not in range(0, 9):
            raise ValueError(f"Column index {column_index} is not in range")

        row_start, row_end = self.get_indices_for_section(row_index)
        col_start, col_end = self.get_indices_for_section(column_index)

        return (
            self.possible.iloc[row_start:row_end, col_start:col_end]
            if possibles
            else self.status.iloc[row_start:row_end, col_start:col_end]
        )

    def get_indices_for_section(self, index):
        """Returns the row and column indices for the section at the given index"""
        if index in [0, 1, 2]:
            return 0, 3
        elif index in [3, 4, 5]:
            return 3, 6
        else:
            return 6, 9

    def is_solved(self):
        """Returns True if the puzzle is solved, False otherwise"""
        return not self.status.eq(0).any().any()

    def naked_single_pass(self):
        """Performs a naked single pass on the puzzle"""
        print("0: Performing naked single pass")
        effective = False
        for row_index in range(9):
            for column_index in range(9):
                if self.get_value(row_index, column_index) == 0:
                    naked_single = self.get_naked_single(row_index, column_index)
                    if naked_single != 0:
                        self.set_value(naked_single, row_index, column_index)
                        effective = True
        return effective

    def hidden_single_pass(self):
        """Performs a hidden single pass on the puzzle"""
        print("1: Performing hidden single pass")
        effective = False
        for row_index in range(9):
            for column_index in range(9):
                if self.get_value(row_index, column_index) == 0:
                    possible = self.get_value(row_index, column_index, possibles=True)
                    for val in possible:
                        if self.is_hidden_single(val, row_index, column_index):
                            self.set_value(val, row_index, column_index)
                            effective = True
        return effective

    def naked_pairs_triples_pass(self):
        """Look for naked pairs and triples"""
        print("2: Performing naked pairs and triples pass")
        effective = False
        for row_index in range(9):
            for col_index in range(9):
                if self.naked_pairs_triples(row_index, col_index):
                    effective = True
        return effective

    def naked_pairs_triples(self, row_index, col_index):
        """Look for naked pairs and triples in the row or column"""
        effective = False
        row = [set(x) for x in self.get_row(row_index, True).values.flatten().tolist()]
        col = [set(x) for x in self.get_col(col_index, True).values.flatten().tolist()]
        row_start, row_end = self.get_indices_for_section(row_index)
        col_start, col_end = self.get_indices_for_section(col_index)
        section = [
            set(x)
            for x
            in self.get_section(row_index, col_index, True).values.flatten().tolist()
        ]
        for cell in row:
            num_possible = len(cell)
            if row.count(cell) == num_possible:
                for remove_index in range(9):
                    examined = set(self.get_value(row_index, remove_index, possibles=True))
                    if cell != examined:
                        for val in cell:
                            if val in self.get_value(row_index, remove_index, possibles=True):
                                self.remove_possible(val, row_index, remove_index)
                                effective = True
        for cell in col:
            num_possible = len(cell)
            if col.count(cell) == num_possible:
                for remove_index in range(9):
                    examined = set(self.get_value(remove_index, col_index, possibles=True))
                    if cell != examined:
                        for val in cell:
                            if val in self.get_value(remove_index, col_index, possibles=True):
                                self.remove_possible(val, remove_index, col_index)
                                effective = True
        for cell in section:
            num_possible = len(cell)
            if section.count(cell) == num_possible:
                for row in range(row_start, row_end):
                    for col in range(col_start, col_end):
                        examined = set(self.get_value(row, col, possibles=True))
                        if cell != examined:
                            for val in cell:
                                if val in self.get_value(row, col, possibles=True):
                                    self.remove_possible(val, row, col)
                                    effective = True

        return effective

    def hidden_pairs_triples_pass(self):
        """Look for hidden pairs and triples"""
        print("3: Performing hidden pairs and triples pass")

        return False

    def pointing_pair_pass(self):
        """Looks for pointing pairs"""
        print("5: Performing pointing pair pass")
        return False

    def solve(self):
        """Solves the puzzle and prints the solution to the console"""
        while True:
            self.out()
            if self.naked_single_pass():
                continue
            if self.hidden_single_pass():
                continue
            if self.naked_pairs_triples_pass():
                continue
            if self.hidden_pairs_triples_pass():
                continue
            break
        self.out()

def main():
    """Main line logic"""
    print("Input a puzzle")
    print("Use spaces or 0's for blanks, non-zero numbers for filled in squares")
    print("At the end of each row, press [Enter]")
    print("There should be 9 characters in each line.")
    print("In other words, your line (including the prompt), whould end up")
    print("this long:")
    print("        -------->")
    row1 = "000000000"
    row2 = "904607000"
    row3 = "076804100"
    row4 = "309701080"
    row5 = "008000300"
    row6 = "050308702"
    row7 = "007502610"
    row8 = "000403208"
    row9 = "000000000"
    # row1 = input("Row 1:  ")
    # row2 = input("Row 2:  ")
    # row3 = input("Row 3:  ")
    # row4 = input("Row 4:  ")
    # row5 = input("Row 5:  ")
    # row6 = input("Row 6:  ")
    # row7 = input("Row 7:  ")
    # row8 = input("Row 8:  ")
    # row9 = input("Row 9:  ")

    sudoku_raw = [row1, row2, row3, row4, row5, row6, row7, row8, row9]

    s = Sudoku(sudoku_raw)
    s.solve()

main()
