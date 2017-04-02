(deffunction summ-iter (?n)
  (if (= ?n 1) then (return (/ 1 3)))
  (+ (/ 1 (+ (* 2 ?n) 1)) (summ-iter (- ?n 1)))
)
