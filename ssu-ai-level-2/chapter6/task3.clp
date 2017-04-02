(deffunction fx (?x ?c ?d)
  (if (< ?x ?c) then
    (return (- 1 (* ?x ?x))))
  (if (>= ?x ?d) then
    (return (+ 1 (* ?x ?x))))
  0
)
