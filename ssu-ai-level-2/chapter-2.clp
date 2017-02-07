// First task
(deffacts students
         (student LelyakinMA 4)
         (student ArutunyaAS 4)
         (student KefalicsAI 1)
         (student BelokobylskySA 2)
)

(facts)

(retract 2)
(retract 3)

(assert (student KefalicsAI 2))

(facts)
