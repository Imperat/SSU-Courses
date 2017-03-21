(deffunction str-stars (?str ?n)
    (while (> ?n 0) do
        (bind ?str (str-cat ?str "*"))
        (bind ?n (- ?n 1))
    )
    ?str
)

(defrule str_start
=>
(bind ?str1 (read))
(bind ?str2 (read))
(if (> (str-length ?str1) (str-length ?str2)) then
    (bind ?diff (- (str-length ?str1) (str-length ?str2)))
    (printout t ?str1 crlf)
    (printout t (str-stars ?str2 ?diff) crlf)
else
    (bind ?diff (- (str-length ?str2) (str-length ?str1)))
    (printout t (str-stars ?str1 ?diff) crlf)
    (printout t ?str2 crlf)
))
