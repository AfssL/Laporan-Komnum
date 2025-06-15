python
import numpy as np

def f(x):
    return np.sin(x)

def romberg(f, a, b, n):
    R = np.zeros((n, n))
    h = b - a
    R[0, 0] = 0.5 * h * (f(a) + f(b))
    
    for i in range(1, n):
        h /= 2
        sum_f = sum(f(a + (2*k - 1)*h) for k in range(1, 2**(i-1) + 1))
        R[i, 0] = 0.5 * R[i-1, 0] + h * sum_f
        for k in range(1, i + 1):
            R[i, k] = R[i, k-1] + (R[i, k-1] - R[i-1, k-1]) / (4**k - 1)

    return R

a = 0
b = np.pi
n = 5
R = romberg(f, a, b, n)

print("Tabel Romberg:")
print(R)
print(f"\nHasil integrasi sin(x) dari 0 sampai pi: {R[n-1, n-1]}")
