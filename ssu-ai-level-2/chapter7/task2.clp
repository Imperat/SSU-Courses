;Get string, replace all spaces by "_"
(defrule replace
 =>
 (bind ?str (readline))
 (bind ?a " ")
 (bind ?b "_")
 (bind ?n (str-length ?str))
 (bind ?res "")
 (loop-for-count (?i 1 ?n) do
    (bind ?c1 (sub-string ?i ?i ?str))
    (bind ?d (str-compare ?c1 ?a))

    (if (= ?d 0) then
        (bind ?res (str-cat ?res ?b)))

    (if (<> ?d 0) then
        (bind ?res (str-cat ?res ?c1))))

 (printout t "result=" ?res crlf) 
 )
