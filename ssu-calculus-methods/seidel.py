def seidel(m, b, eps):
    n = len(m)
    r = range(n)
    x = [0 for i in r]
    conv = False
    while not conv:
        p = x.copy()
        for i in r:
            var = sum(m[i][j] * x[j] for j in range(i))
            var += sum(m[i][j] * p[j] for j in range(i+1, n))
            x[i] = (b[i] - var) / m[i][i]
        
        conv = sum((x[i]-p[i])**2 for i in r) < eps
    return x
