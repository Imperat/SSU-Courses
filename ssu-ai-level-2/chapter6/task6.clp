(deffunction summ-iter (?n)
  (if (= ?n 1) then (return 1))
  (+ (/ 1 ?n) (summ-iter (- ?n 1)))
)
