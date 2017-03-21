(deffunction str-del (?substr ?str)
    (bind ?n1 (str-length ?substr))
    (bind ?n2 (str-length ?str))
    (bind ?k (str-index ?substr ?str))
    (while (> ?k 0) do
        (bind ?st1 (sub-string 1 (- ?k 1) ?str))
        (bind ?st2 (sub-string (+ ?k ?n1) ?n2 ?str))
        (bind ?str (str-cat ?st1 ?st2))
        (bind ?k (str-index ?substr ?str))
        (if (not ?k) then 
            (bind ?k 0)
        )
    )
    ?str)
