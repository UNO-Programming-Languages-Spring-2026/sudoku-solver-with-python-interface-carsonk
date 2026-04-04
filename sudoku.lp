% Define the domain of rows, columns, and values
row(1..9).
column(1..9).
value(1..9).

% Assign exactly one value to each cell
1 { sudoku(R,C,V) : value(V) } 1 :- row(R), column(C).

% Keep the given clues
sudoku(R,C,V) :- initial(R,C,V).

% No repeated value in a row
:- sudoku(R,C1,V), sudoku(R,C2,V), C1 != C2.

% No repeated value in a column
:- sudoku(R1,C,V), sudoku(R2,C,V), R1 != R2.

% Define 3x3 block ids safely
block_id(R,C,B) :- row(R), column(C), B = ((R-1)/3)*3 + ((C-1)/3).

% No repeated value in the same 3x3 block
:- sudoku(R1,C1,V), sudoku(R2,C2,V),
   block_id(R1,C1,B), block_id(R2,C2,B),
   (R1,C1) != (R2,C2).

#show sudoku/3.