pow(_, 1, R) :- write(R).
pow(X, N, R) :-
  R1 is R * X, N1 is N - 1, pow(X, N1, R1).
pow(X, N) :- pow(X, N, X).
