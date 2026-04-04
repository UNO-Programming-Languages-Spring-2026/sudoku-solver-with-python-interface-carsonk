import sys
import clingo
from clingo.application import Application, clingo_main
from sudoku_board import Sudoku


class Context:
    def __init__(self, puzzle: Sudoku):
        self.puzzle = puzzle

    def initial(self) -> list[clingo.Symbol]:
        symbols = []

        for (row, col), value in self.puzzle.sudoku.items():
            symbols.append(
                clingo.Tuple_(
                    (
                        clingo.Number(row),
                        clingo.Number(col),
                        clingo.Number(value),
                    )
                )
            )

        return symbols


class SudokuTextApp(Application):
    def print_model(self, model, printer) -> None:
        solved_puzzle = Sudoku.from_model(model)
        print(solved_puzzle)
        sys.stdout.flush()

    def main(self, ctl, files):
        try:
            ctl.load("sudoku.lp")
            ctl.load("sudoku_py.lp")

            if not files:
                ctl.load("-")
                ctl.ground([("base", [])])
            else:
                input_path = files[0]

                with open(input_path, "r", encoding="utf-8") as source:
                    puzzle_text = source.read()

                starting_board = Sudoku.from_str(puzzle_text)
                context = Context(starting_board)

                ctl.ground([("base", [])], context=context)

            ctl.solve()

        except RuntimeError as err:
            print("*** ERROR: (clingo):", err)
            sys.stdout.flush()


if __name__ == "__main__":
    clingo_main(SudokuTextApp())