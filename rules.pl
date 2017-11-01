parent(P,C) :- child(C,P).

married(A,B) :- parent(A,C), parent(B,C), A \== B.

sibling(A,B) :- parent(C,A), parent(C,B), A \== B.

% http://www.cs.utexas.edu/~cannata/cs345/Class%20Notes/12%20prolog_intro.pdf
grandparent(A,B) :- parent(A,C), parent(C,B).

% https://stackoverflow.com/questions/30497704/prolog-general-rule-for-finding-cousins-etc
ancestor(A,B,L) :-
  parent(A,C),
  ancestor(C,B,L),
  L is L + 1.
