#Subtask 1
# Y = (X^2 + 1) / (X - 2)
expr(X) :-
  X =\= 2, Y is (X * X + 1)/(X - 2), write(Y);
  write("Error: /0").

#Subtask 2
# S = 2(X^2 + Y^2)/(X + Y)
expr(X, Y) :-
  X + Y =\= 0, S is 2 * (X*X + Y*Y) / (X + Y), write(S);
  write("Error: /0").
  
#Subtask 3
Middle Arithmetic
expr(X, Y) :-
  S is ((X + Y) / 2), write(S). 
  
#Subtask 4
No comments
is_even(X) :-
  S is (X mod 2), S == 0.
  
#Subtask 5
Predefined interval
belongs(X, A, B) :-
  X >= A, X =< B.
  
#Subtask 6
Minimum of threes
min(A, B, C) :- 
  A =< B, A =< C, write(A);
  B =< A, B =< C, write(B);
  write(C).
  
Subtask 7
Maximum of threes
max(A, B, C) :-
  A >= B, A >= C, write(A);
  B >= A, B >= C, write(B);
  write(C).
