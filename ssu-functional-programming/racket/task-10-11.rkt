#lang racket

;Сколько раз повторяется данный атом в списке
(define (whatcount L atom count)
  (if (not (null? (cdr L)))
    (if (= (car L) atom) 
      (whatcount (cdr L) atom (+ count 1)) 
      (whatcount (cdr L) atom count))
    (if (= (car L) atom)
        (+ count 1)
        count)))

(whatcount '(1 1 3 4 1) 1 0)

(define (func L first_iter second_iter first_result second_result)
  (if (not (null? (cdr second_iter)))
    (if (= (whatcount L (car second_iter) 0) first_iter)
      (func L first_iter (cdr second_iter) first_result (append second_result (car second_iter)))
      (func L first_iter (cdr second_iter) first_result second_result))
    (second_result)))

(func '(2 2 3 1 1 1) 0 '(2 2 3 1 1 1) 0 '())
