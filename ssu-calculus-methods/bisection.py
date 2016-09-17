def bisection (f, a, b, eps, k=0):
	if abs(f(a)) + abs(f(b)) < 2 * eps:
		return ( (a + b) / 2, k)
	else:
		c = (a + b) / 2.0
		if f(a) < 0 and f(c) > 0:
			return bisection(f, a, c, eps, k+1)
		if f(a) > 0 and f(c) < 0:
			return bisection(f, a, c, eps, k+1)
		if f(b) > 0 and f(c) < 0:
			return bisection(f, b, c, eps, k+1)
		if f(b) < 0 and f(c) > 0:
			return bisection(f, b, c, eps, k+1)

f = lambda x : x*x - 5

print bisection(f, 0, 2.5, 0.001)[0]
print "counts:"
print bisection(f, 0, 2.5, 0.001)[1]
