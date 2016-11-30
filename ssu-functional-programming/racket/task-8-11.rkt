#lang racket

(define (y N)
  (define (ij-func i j)
    (+ (/ (log i) (log 10)) (log j)))
  (define (y-iter i j sum)
    (cond ((> i N) sum)
          ((> j N) (y-iter (+ i 1) 1 sum))
          (else   (y-iter i (+ j 1) (+ sum (ij-func i j))))))
  (y-iter 1 1 0))

(y 5)
