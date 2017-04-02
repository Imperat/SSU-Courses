(defrule spisok-sotr
  =>
    (printout t "Input the count of employees")
    (bind ?n (read))
    (loop-for-count (?i 1 ?n) do
      (printout t "Input the last name:")
      (bind ?lastName (read))
      (printout t "Input the doljnost:")
      (bind ?doljn (read))
      (assert (sotr ?lastName ?doljn))
    )
)
