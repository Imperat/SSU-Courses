(deftemplate employee
	(slot name)
	(slot department (default CS))
	(slot st)
)

(employee (name Ivanov) (department CS) (st 20))
(employee (name Petrov) (department CS) (st 15))
(employee (name Zaizev) (department HS) (st 40))

(modify 1 (department HS))
(modify 3 (st 99))
(dublicate 2 (name Utkin))

(assert employee (name Kefalic) (department MT) (st 10))
(assert employee (name Marmonm) (department MT) (st 15))

(retract 2 4)
