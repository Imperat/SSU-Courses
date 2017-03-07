
(reset)
(clear)

(deftemplate employee
	(slot name)
	(slot department (default CS))
	(slot st)
)

(load-facts C:/Users/LelyakinMA/SSU-Courses/ssu-ai-level-2/chapter3/facts3-2.clp)

(modify 1 (department HS))
(modify 3 (st 99))
(duplicate 2 (name Utkin))

(assert (employee (name Kefalic) (department MT) (st 10)))
(assert (employee (name Marmonm) (department MT) (st 15)))

(retract 2 4)
