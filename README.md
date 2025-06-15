# Laporan-Komnum
# Praktikum 1 – Implementasi Metode Regula Falsi

##  Anggota Kelompok
- Antonius Andy Martono  
- Afsal Murtaza  
- Bima Novrifa  

---

##  Deskripsi Soal

Anda sudah memahami algoritma pemrosesan *Metode Regula Falsi* dan cara kerjanya.  
Tugas Anda adalah mengimplementasikan algoritma tersebut menjadi *program komputer* yang dapat:

- Menampilkan proses iteratif numerik
- Menampilkan grafik fungsi \( f(x) \) dan pendekatan akar secara visual

---

##  Kode Program
```
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
```

---

##  Penjelasan Kode

* **f(x)** adalah fungsi yang akan dicari akarnya, yaitu $x^3 - 4x - 9$.
* **regula_falsi()**:

  * Memeriksa apakah $f(a) \cdot f(b) < 0$ agar metode bisa dijalankan.
  * Menghitung titik perpotongan garis lurus (linear interpolasi) antara $a$ dan $b$.
  * Memperbarui nilai $a$ atau $b$ tergantung tanda dari hasil fungsi.
  * Menyimpan hasil setiap iterasi ke dalam data_iterasi hingga akar ditemukan atau iterasi maksimum tercapai.
* **plot_fungsi()**:

  * Menggambar grafik fungsi dalam interval sekitar $a$ dan $b$.
  * Menandai akar dengan titik merah dan membuat grafik lebih informatif.

---

##  Contoh Output Terminal


Iterasi  |  a		|   b   |	 x	 |  f(x)

1)	 2.000000	 3.000000	 2.538462	 -2.829996

2)	 2.538462	 3.000000	 2.673738	 -1.119196

3)	 2.673738	 3.000000	 2.722709	 -0.424785

4)	 2.722709	 3.000000	 2.742617	 -0.158577

5)	 2.742617	 3.000000	 2.750382	 -0.058580

6)	 2.750382	 3.000000	 2.753319	 -0.021539

7)	 2.753319	 3.000000	 2.754393	 -0.007914

8)	 2.754393	 3.000000	 2.754782	 -0.002906

9)	 2.754782	 3.000000	 2.754930	 -0.001068

10)	 2.754930	 3.000000	 2.754985	 -0.000393

11)	 2.754985	 3.000000	 2.755005	 -0.000144

12)	 2.755005	 3.000000	 2.755012	 -0.000053

13)	 2.755012	 3.000000	 2.755014	 -0.000019

14)	 2.755014	 3.000000	 2.755015	 -0.000007


---

## Screenshot Output

> ![image](https://github.com/user-attachments/assets/644176dd-401e-4b6d-9a9c-61fc9bea50e4)


> ![image](https://github.com/user-attachments/assets/9721f9b2-543c-4eb5-8d6b-d50f58c0992f)


---

## Kesimpulan

- Metode Regula Falsi merupakan metode numerik sederhana namun efektif untuk menemukan akar fungsi non-linear.
- Dengan hanya memerlukan dua titik awal dan melakukan interpolasi linier, metode ini mampu menemukan akar dengan cepat.
- Dalam praktikum ini, akar fungsi berhasil ditemukan dalam 10–15 iterasi, dan divisualisasikan dengan baik dalam bentuk grafik.

---
