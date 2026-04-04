import sys
import clingo
from clingo.application import Application, clingo_main


class SudokuApp(Application):
    def print_model(self, model, printer) -> None:
        symbols = sorted(model.symbols(shown=True))
        print(" ".join(str(symbol) for symbol in symbols))
        sys.stdout.flush()

    def main(self, ctl, files):
        try:
            ctl.load("sudoku.lp")

            for file_name in files:
                ctl.load(file_name)

            if not files:
                ctl.load("-")

            ctl.ground([("base", [])])

        except RuntimeError as error:
            print("*** ERROR: (clingo):", error)
            sys.stdout.flush()
            return

        ctl.solve()


if __name__ == "__main__":
    clingo_main(SudokuApp())