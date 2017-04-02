(deffacts tovars
    (tovar TV 200 4 2015 Russia)
    (tovar Watch 199 5 2017 USA)
    (tovar Linkorn 1000 1 2010 Armenia)
    (tovar IceCream 10 99 2017 Ukraine)
    (tovar Book 1 1 2001 Vanuatu)
)

(defrule ucenk
    (tovar ?name ?cost ?count ?year ?country)

    (test (or (< ?year 2010)
              (< ?count 4)
          )
    )
     =>
     (assert (ucenka ?name (* ?cost 0.15)))
)

(defrule nacenk
    (tovar ?name ?cost ?count ?year ?country)

    (test (and (= 0 (str-compare ?country Russia))
               (= ?year 2017)
          )
    )
     =>
    (assert (nacenka ?name (* ?cost 0.07)))
)

(defrule russian
    (tovar ?name ?cost ?count ?year ?country)

    (exists  (test (= 0 (str-compare ?country Russia))))
      =>
    (printout t "There are Russian production" crlf)
)
