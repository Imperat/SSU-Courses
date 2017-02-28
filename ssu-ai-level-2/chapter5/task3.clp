(defrule fact
 =>
 (printout t "n=")
 (bind ?n (read))
 (bind ?r 1)
 (loop-for-count (?i 2 ?n) do
 	(bind ?r (* ?r ?i))
 )
 (printout t "fact is:")
 (printout t ?r)
 (printout t "")
)
