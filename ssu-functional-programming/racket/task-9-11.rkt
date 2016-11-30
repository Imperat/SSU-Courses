#lang racket

(define (set? lst)
  (if (null? lst)
    #t
    (and (not (member (car lst) (cdr lst)))
         (set? (cdr lst)))))

(set? '(1 2 3 4 5))
(set? '(1 2 3 4 4))

