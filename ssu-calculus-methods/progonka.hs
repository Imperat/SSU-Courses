f q_pred p_pred my_tail accumulate = 
	if tail == [] then
		accumulate
	else
		f q p tail my_tail accumulate ++ [p, q]
			where
						cort = head my_tail
						a = cort !! 0
						b = cort !! 1
						c = cort !! 2
						d = cort !! 3
						p = c / b - a*p_pred
						q = (a*q_pred - d) / b - a*p_pred
