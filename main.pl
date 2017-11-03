:- initialization(main).

main :-
  consult('database.pl'),
  consult('rules.pl'),
  nthcousinkremoved_eval,
  kthchild_eval,
  nthcousin_eval,
  sibling_eval,
  halt.

% Nth Cousin K Times Removed Evaluation
nthcousinkremoved_eval :-
  findall(X,    setof(Y, nthcousinkremoved(X,Y,N,K), List), Xs),
  findall(List, setof(Y, nthcousinkremoved(X,Y,N,K), List), Lists),
  findall(N,    setof(Y, nthcousinkremoved(X,Y,N,K), List), Ns),
  findall(K,    setof(Y, nthcousinkremoved(X,Y,N,K), List), Ks),
  writeln('Nth Cousin K Times Removed Evaluation:'),
  kremoved_records(Xs,Ns,Ks,Lists),
  writeln('').

kremoved_records([],[],[],[]).
kremoved_records([A|B], [C|D], [E|F], [G|H]) :-
  format('\t~w\t~dth cousin ~d removed: ~p~n', [A, C, E, G]),
  kremoved_records(B,D,F,H).

% Nth Cousin Evaluation
nthcousin_eval :-
  findall(X,    setof(Y, nthcousin(X,Y,N), List), Xs),
  findall(List, setof(Y, nthcousin(X,Y,N), List), Lists),
  findall(N,    setof(Y, nthcousin(X,Y,N), List), Ns),
  writeln('Nth Cousin Evaluation:'),
  nthcousin_records(Xs,Ns,Lists),
  writeln('').

nthcousin_records([],[],[]).
nthcousin_records([A|B], [C|D], [E|F]) :-
  format('\t~w\t~dth cousin: ~p~n', [A, C, E]),
  nthcousin_records(B,D,F).

% Kth Child Evaluation
kthchild_eval :-
  findall(P,    setof(C, kthchild(C,P,K), List), Ps),
  findall(List, setof(C, kthchild(C,P,K), List), Lists),
  findall(K,    setof(C, kthchild(C,P,K), List), Ks),
  writeln('Kth Child Evaluation:'),
  kthchild_records(Ps,Ks,Lists),
  writeln('').

kthchild_records([],[],[]).
kthchild_records([A|B], [C|D], [E|F]) :-
  format('\t~w\t~dth child: ~p~n', [A, C, E]),
  kthchild_records(B,D,F).

% Sibling Evaluation
sibling_eval :-
  findall(A,    setof(B, sibling(A,B), List), As),
  findall(List, setof(B, sibling(A,B), List), Lists),
  writeln('Sibling Evaluation:'),
  sibling_records(As,Lists),
  writeln('').

sibling_records([],[]).
sibling_records([A|B], [C|D]) :-
  format('\t~w\t siblings: ~p~n', [A, C]),
  sibling_records(B,D).
