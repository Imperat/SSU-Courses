(deftemplate client
	(slot name)
	(slot number)
	(slot city (default Saratov))
)

(client (name Ivanov) (number 1) (city Saratov))
(client (name Petrov) (number 2) (city Saratov))
(client (name Zaizev) (number 3) (city Vorones))

(modify 1 (city Samara))
(modify 2 (name Lelyakin))
(dublicate 3 (number 4))

(assert client (name Kefalic) (number 5) (city Moscow))
(assert client (name Marmonm) (number 6) (city Kazan))
