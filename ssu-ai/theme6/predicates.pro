make_list(_, 0, _, []).
make_list(N, M, S, [N|L]) :- 
    N1 is N + S, 
    M1 is M - 1, 
    make_list(N1, M1, S, L).

remove(A, [A|B], B).
remove(A, [B, C|D], [B|E]) :-
    remove(A, [C|D], E).

insert(A, L, 1, [A|L]).
insert(A, [H|L], M, [H|L1]) :- 
    M > 1,
    M1 is M - 1, 
    insert(A, L, M1, L1). 

sum([L], L).
sum([H1, H2|T], S) :-
    S1 is H1 + H2,
    sum([S1|T], S).

prod([L], L).
prod([H1, H2|T], S) :-
    S1 is H1 * H2,
    prod([S1|T], S).

append([], L, L).
append([H|T], L2, [H|L3]) :- 
    append(T, L2, L3).
