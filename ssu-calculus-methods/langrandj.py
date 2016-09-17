def Fi(i, xi, x):
    res = 1
    for j in range(0, n):
        if j != i:
            res *= xi - x[j]
            res /= x[i] - x[j]
    return res

def Ln(xi, n, x, y):
    res = 0
    for i in range(0, n):
        res += y[i] * Fi(i, xi, x)
    return res

n = 3
x = [-1.0, 0.0, 1.0]
y = [10.0, 5.0, 20.0]

xs, ys = [], []
s = x[0]
while s <= x[n-1]:
    xs.append(s)
    s += 0.05
for xi in xs:
    ys.append(Ln(xi, n, x, y))
