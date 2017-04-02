(deffunction fx (?x ?a)
  (if (< ?x 0) then (return (/ (abs (- ?x ?a)) (* ?x ?x))))
  (if (> ?x 0) then (return (sin (abs (+ ?x ?a)))))
  0
)
