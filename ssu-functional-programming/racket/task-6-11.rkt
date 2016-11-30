#lang racket

(let ((L1 '(PRIM SD FLAG () (GHG)))
      (L2 '(1 56 98 52))
      (L3 '(T Y H)))
  (and
    (number? (car (cdr (cdddr L1))))
    (not (pair? (car (cddr (L2)))))
    (list? (car (cdr L3)))))
