(defrule easy_summ
  =>
  (printout t "n=")
  (bind ?n (read))
  (bind ?s 0)
  (bind ?i 2)
  (while (<= ?i (* 2 ?n)) do
   (bind ?s (+ ?s (/ 1 (* ?i ?i))))
   (bind ?i (+ ?i 2))
  )
  (printout t "summ is:")
  (printout t ?s)
  (printout t "")
)
