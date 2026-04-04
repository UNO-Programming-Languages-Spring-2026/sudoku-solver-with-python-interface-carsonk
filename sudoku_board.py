from typing import Tuple
import clingo


class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku

    def __str__(self) -> str:
        rows = []

        for r in range(1, 10):
            parts = []

            for block_start in (1, 4, 7):
                block_values = []
                for c in range(block_start, block_start + 3):
                    block_values.append(str(self.sudoku[(r, c)]))
                parts.append(" ".join(block_values))

            rows.append("  ".join(parts))

            if r in (3, 6):
                rows.append("")

        return "\n".join(rows)

    @classmethod
    def from_str(cls, s: str) -> "Sudoku":
        sudoku = {}
        row_num = 1

        for line in s.splitlines():
            line = line.strip()

            if line == "":
                continue

            parts = line.split()
            if len(parts) != 9:
                raise ValueError("Each row must have exactly 9 entries.")

            for col_num, value in enumerate(parts, start=1):
                if value != "-":
                    sudoku[(row_num, col_num)] = int(value)

            row_num += 1

        if row_num != 10:
            raise ValueError("Sudoku input must contain exactly 9 rows.")

        return cls(sudoku)

    @classmethod
    def from_model(cls, model: clingo.solving.Model) -> "Sudoku":
        sudoku = {}

        for atom in model.symbols(shown=True):
            if atom.name == "sudoku" and len(atom.arguments) == 3:
                row = atom.arguments[0].number
                col = atom.arguments[1].number
                value = atom.arguments[2].number
                sudoku[(row, col)] = value

        return cls(sudoku)