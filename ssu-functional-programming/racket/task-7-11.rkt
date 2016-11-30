#lang racket
(define (func l1 l2) 
  (car l1))

(func '(4 5 4) '(4 5 4 3))
