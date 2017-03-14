(defrule replace
 =>
 (bind ?str (readline))
 (bind ?a (readline))
 (bind ?b (readline))
 (bind ?n (str-length ?str))
 (bind ?k 0)
 (loop-for-count (?i 1 ?n) do
    (bind ?c1 (sub-string ?i ?i ?str))
    (bind ?d (str-compare ?c1 ?a))

    (if (= ?d 0) then
        (printout t "k=" ?k crlf))))
