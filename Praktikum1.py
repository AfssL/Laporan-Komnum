python
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 4*x - 9

def regula_falsi(a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        print("Metode gagal: f(a) dan f(b) harus beda tanda.")
        return None

    iterasi = 0
    data_iterasi = []

    while iterasi < max_iter:
        x = b - f(b) * (b - a) / (f(b) - f(a))
        fx = f(x)
        data_iterasi.append((iterasi + 1, a, b, x, fx))

        if abs(fx) < tol:
            break

        if f(a) * fx < 0:
            b = x
        else:
            a = x

        iterasi += 1

    return x, data_iterasi

def plot_fungsi(f, a, b, akar):
    x_vals = [i for i in range(int(a) - 1, int(b) + 2)]
    y_vals = [f(x) for x in x_vals]
    plt.axhline(0, color='black', linewidth=0.5)
    plt.plot(x_vals, y_vals, label='f(x)')
    plt.plot(akar, f(akar), 'ro', label=f'Akar ≈ {akar:.4f}')
    plt.legend()
    plt.grid()
    plt.title('Grafik Fungsi dan Akar dengan Regula Falsi')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.show()

a = 2
b = 3
akar, hasil_iterasi = regula_falsi(a, b)

print("Iterasi\t a\t\t b\t\t x\t\t f(x)")
for row in hasil_iterasi:
    print(f"{row[0]}\t {row[1]:.6f}\t {row[2]:.6f}\t {row[3]:.6f}\t {row[4]:.6f}")

plot_fungsi(f, a, b, akar)
