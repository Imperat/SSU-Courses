// First task
// Students
(deffacts students
         (student LelyakinMA 4)
         (student ArutunyaAS 4)
         (student KefalicsAI 1)
         (student BelokobylskySA 2)
)

(reset)
(facts)

(retract 2)
(retract 3)

(assert (student KefalicsAI 2))

(facts)


// Trains
(deffacts trains
          (train 11 Saratov 11)
          (train 22 Engels 21)
          (train 33 Kazan 22)
)

(reset)
(assert (train 44 Samara 10))
(assert (train 55 Volgograd 08))

(retract 1 4)

(retract 2 3)

(assert (train 22 Moscow 01))
(assert (train 33 Kazan 00))


// Employees
(assert (sotrudnik LelyakinMA 1)
        (sotrudnik GerasimovVD 2)
        (sotrudnik VonnegutKG 3)
        (sotrudnik PushkinAS 3)
)

(reset)
(retract 1)

(retract 3)
(assert (sotrudnik VasilevKD 3))


// Products
(assert (IceCream Russia 10 1)
		(ApelsineJuce Russia 20 2)
		(WaterMelone Russia 30 3)
		(Liberty USA 1000 99)
)

(reset)
(facts)

(retract 2)
(ApelsineJuce Russia 19 2)

(retract 4)
(Liberty USA 0 99)
