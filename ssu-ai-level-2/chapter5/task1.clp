(defrule zachisl
  =>
    (printout t "Input the count of students")
    (bind ?n (read))
    (loop-for-count (?i 1 ?n) do
      (printout t "Input the last name:")
      (bind ?lastName (read))
      (assert (student ?lastName 1))
    )
)
