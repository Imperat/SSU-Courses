#lang racket

(let ((L1 '(PRIM SD FLAG () (GHG)))
      (L2 '(1 56 98 52))
      (L3 '(T Y H)))
  (list
    (car (cddddr L1))
    (car (cdr (cdr L2)))
    (car (cdr L3))))
