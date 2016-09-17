from math import sin

ys = [sin(i) for i in range(1,3.14, 0.2)]
xs = range(1, 3.14, 0.2)

def h(k):
    return xs[k] - xs[k-1]

def f_r(k):
    return (ys[k] - ys[k-1]) / h(k)

lamba1 = (3 * f_r(2) - 3 * f_r(1)) / (2 * (h(1) + h(2)))
delta1 = - h(2) / (2 * (h(1) + h(2)))

deltas = [delta1]
lambas = [lamba1]

for k in range(3,n):
    t = h(k) / (2 * h(k-1) + 2 * h(k) + h(k-1) * deltas[-1])
    deltas.append(t)

for k in range(3,n):
    t = 3 * (f_r(k) - f_r(k-1) - h(k-1)*lambas[k-2]) / (
        2 * (h(k-1) + h(k)) + h(k-1)*deltas(k-2))

c = [0]
for k in range(n,2):
    t = deltas[k-1]*c[-1] + lambas[k-1]
    c.append(t)

def c_r(k):
    c[k] - c[k-1]

d = [c_r(k) / (3 * h(k)) for k in range(1, len(xs) + 1)
b = [f_r(k) + 2.0 / 3 * h(k)c[k] + 1.0 / 3 * h(k)c[k-1]]

a = ys
