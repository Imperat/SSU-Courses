#lang racket

(let ((L '((A B) ((X C D) E F) (G H))))
  (caaar (cdr L)))
