parent(P,C) :- child(C,P).

older(X,Y) :- age(X,A), age(Y,B), A > B.

sibling(A,B) :- parent(C,A), parent(C,B), 
                parent(D,A), parent(D,B),
                A \== B, older(C,D).

% http://www.cs.utexas.edu/~cannata/cs345/Class%20Notes/12%20prolog_intro.pdf
grandparent(A,B) :- parent(A,C), parent(C,B).

% https://stackoverflow.com/questions/30497704/prolog-general-rule-for-finding-cousins-etc
cousin(A,B) :- parent(C,A), parent(D,B), sibling(C,D).

nthchild(P,C,N) :- 
