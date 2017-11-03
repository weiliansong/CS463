:- initialization(main).

main :-
  consult('database.pl'),
  consult('rules.pl'),
  process,
  halt.

process :-
  findall(A, bagof(B, sibling(A,B), List), As),
  findall(List, bagof(B, sibling(A,B), List), Lists),
  show_records(As,Lists).

show_records([],[]).
show_records([A|B], [C|D]) :-
  format('~w\tCousin: ', A),
  writeln(C),
  show_records(B,D).
