
(reset)
(clear)

(deftemplate client
	(slot name)
	(slot number)
	(slot city (default Saratov))
)

(load-facts C:/Users/LelyakinMA/SSU-Courses/ssu-ai-level-2/chapter3/facts3-1.clp)

(modify 1 (city Samara))
(modify 2 (name Lelyakin))
(duplicate 3 (number 4))

(assert (client (name Kefalic) (number 5) (city Moscow)))
(assert (client (name Marmonm) (number 6) (city Kazan)))
