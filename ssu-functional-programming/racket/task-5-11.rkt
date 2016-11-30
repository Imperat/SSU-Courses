#lang racket

(let ((L1 '(PRIM SD FLAG () (GHG)))
      (L2 '(1 56 98 52))
      (L3 '(T Y H)))
  (append
    (list (car L1) (cadr L1) (caddr L1) (caddr (cdr L1)))
    (list (car L2) (cadr L2) (caddr (cdr L2)))
    (list (car L3) (caddr L3))))
