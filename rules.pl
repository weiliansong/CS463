parent(P,C) :- child(C,P).

older(X,Y) :- age(X,A), age(Y,B), A > B.

sibling(A,B) :- 
  parent(C,A), parent(C,B), 
  parent(D,A), parent(D,B),
  A \== B, older(C,D).

% https://stackoverflow.com/questions/30497704/prolog-general-rule-for-finding-cousins-etc
cousin(A,B) :- parent(C,A), parent(D,B), sibling(C,D).

kthchild(C,P,1) :- child(C,P).
kthchild(C,P,K) :- M is K-1, child(C_new, P), kthchild(C,C_new,M).

nthcousin(A,B,1) :- cousin(A,B).
nthcousin(A,B,N) :- 
  M is N-1, 
  parent(P_1,A), 
  parent(P_2,B), 
  nthcousin(P_1,P_2,M).

nthcousinkremoved(X,Y,N,K) :- nthcousin(X,Z,N), kthchild(Y,Z,K).
