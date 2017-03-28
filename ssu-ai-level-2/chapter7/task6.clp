(deffunction reflect (?s)
 (bind ?s1 "")
 (bind ?n (length ?s))
 (loop-for-count (?i 0 ?n) do
 (bind ?c (sub-string (- ?n ?i) (- ?n ?i) ?s))
 (bind ?s1 (str-cat ?s1 ?c)))
 ?s1)
