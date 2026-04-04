<<<<<<< HEAD
color(X)  :- X = @color().
node(X)   :- X = @node().
edge(X,Y) :- (X,Y) = @edge().

node(X) :- edge(X,Y).
=======
color(X)  :- X = @color().
node(X)   :- X = @node().
edge(X,Y) :- (X,Y) = @edge().

node(X) :- edge(X,Y).
>>>>>>> df2fe2cfd104b37a474960b5e63d055ba6527b9d
node(Y) :- edge(X,Y).