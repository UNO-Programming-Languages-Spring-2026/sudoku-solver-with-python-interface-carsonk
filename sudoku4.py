import sys
import clingo
from clingo.application import Application, clingo_main
from sudoku_board import Sudoku


class SudokuFormatterApp(Application):
    def main(self, ctl, files):
        try:
            ctl.load("sudoku.lp")

            if files:
                for path in files:
                    ctl.load(path)
            else:
                ctl.load("-")

            ctl.ground([("base", [])])
            ctl.solve()

        except RuntimeError as exc:
            print("*** ERROR: (clingo):", exc)
            sys.stdout.flush()

    def print_model(self, model, printer) -> None:
        solved = Sudoku.from_model(model)
        print(str(solved))
        sys.stdout.flush()


if __name__ == "__main__":
    clingo_main(SudokuFormatterApp())