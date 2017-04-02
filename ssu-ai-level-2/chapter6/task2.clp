(deffunction triangle (?a ?b ?c)
  (bind ?p (/ (+ ?a ?b ?c) 2))
  (sqrt (* ?p (- ?p ?a) (- ?p ?b) (- ?p ?c)))
)



;(deffunction compare-triangles (?a1 ?b1 ?c1 ?a2 ?b2 ?c2)
;  (> (triangle ?a1 ?b1 ?c1) (triangle ?a2 ?b2 ?c2))
;)
