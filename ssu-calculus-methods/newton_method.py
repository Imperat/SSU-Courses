def newtons_method(x0, f, f1, e):
    k = 0
    while True:
        k += 1
        x1 = x0 - (f(x0) * 1.0 / f1(x0))
        if abs(x1 - x0) < e:
            return (x1, k)
        x0 = x1

f = lambda x : x ** 5 - 1
f1 = lambda x : 5 * (x ** 4)

res = newtons_method(3+5J, f, f1, 0.001)
print res[0], "counts: ", res[1]
