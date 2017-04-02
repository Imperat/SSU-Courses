(deffacts employees
    (employee Lelyakin 10 2 100000)
    (employee Lelyakina 11 2 100000)
    (employee Timkaev 12 3 110000)
    (employee Timkaeva 13 3 110000)
    (employee Kisurin 13 3 111000)
    (employee Oldmann 31 3 111991)
)

(defrule prem
    (employee ?name ?expierence ?children ?salary)

    (test (or (> ?children 2)
              (>= ?expierence 5)
          )
    )
      =>
    (assert (premia ?name (* ?salary 0.2)))
)

(defrule all_empl_prem
    (forall (employee ?name ?expierence ?children ?salary)
            (prem ?name))
      =>
    (printout t "All employees has prem")
)

(defrule veteran
    (employee ?name ?expierence ?children ?salary)

    (test (> ?expierence 20))
      =>
    (printout t "There are veterans" crlf)
)
