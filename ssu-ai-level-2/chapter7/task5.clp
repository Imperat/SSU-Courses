(deffunction trim (?str)
    (bind ?str2 "")
    (bind ?space True)
    (bind ?n (str-length ?str))
    (bind ?i 0)
    (while (< ?i ?n) do
        (bind ?c1 (sub-string ?i ?i ?str))

        (if (= 0 (str-compare ?c1 " ")) then
            (if (and (?space True)) then
                (printout t "kefal")
                (bind ?space False)
                (bind ?str2 (str-cat ?str2 ?c1))
            )

        else

            (bind ?space True)
            (bind ?str2 (str-cat ?str2 ?c1))
        )
        (bind ?i (+ ?i 1))
    )
    ?str2
)
