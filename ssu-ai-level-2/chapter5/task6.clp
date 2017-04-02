(defrule node
  =>
  (printout t "n1=")
  (bind ?n1 (read))
  (printout t "n2=")
  (bind ?n2 (read))
  (while TRUE do
    (if (= ?n1 ?n2) then
      (printout t "nod is: " ?n1)
      (return)
    )

    (if (> ?n1 ?n2) then
      (bind ?n1 (- ?n1 ?n2))
    else
      (bind ?n2 (- ?n2 ?n1))
    )
  )
)
