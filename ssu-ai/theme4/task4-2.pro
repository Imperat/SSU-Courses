fib(1, _, Y2) :- write(Y2).
fib(N, Y1, Y2) :-
  N > 1,
  N1 is N - 1, 
  Y11 is Y2,
  Y22 is Y1 + Y2,
  fib(N1, Y11, Y22).
fib(N) :- fib(N, 0, 1).
