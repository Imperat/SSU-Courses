(deffunction trim (?str)
    (bind ?str2 "")
    (bind ?space TRUE)
    (bind ?n (str-length ?str))
    (bind ?i 0)
    (while (<= ?i ?n) do
        (bind ?c1 (sub-string ?i ?i ?str))

        (if (= 0 (str-compare ?c1 " ")) then
            (if (and ?space TRUE) then
                (bind ?space FALSE)
                (bind ?str2 (str-cat ?str2 ?c1))
            )

        else

            (bind ?space TRUE)
            (bind ?str2 (str-cat ?str2 ?c1))
        )
        (bind ?i (+ ?i 1))
    )
    ?str2
)
