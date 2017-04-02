(defrule bank
  =>
  (printout t "p=")
  (bind ?p (read))
  (printout t "You need wait: " (max (round (/ (log 2) (log (+ 1 ?p)))) (round (+ 0.5 (/ (log 2) (log (+ 1 ?p)))))))
)
