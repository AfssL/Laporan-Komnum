#Laporan Praktikum
# Praktikum 2 – Penerapan Integrasi Romberg untuk Meningkatkan Akurasi

## Anggota Kelompok
- Antonius Andy Martono  
- Afsal Murtaza  
- Bima Novrifa  

---

## Deskripsi Soal

Salah satu kelemahan metode Trapezoidal adalah harus menggunakan jumlah interval yang besar untuk mendapatkan hasil yang akurat.  
Untuk mengatasi kelemahan tersebut, digunakan Metode Romberg, yang menggabungkan pendekatan Trapezoidal dan eksstrapolasi Richardson.  
Tugas Anda adalah mengimplementasikan metode Romberg dalam bentuk program komputer untuk menunjukkan:

- Peningkatan akurasi dari integrasi numerik
- Hasil tabel Romberg secara lengkap

---

## Kode Program
```
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
```

---

## Penjelasan Kode

* Fungsi f(x) adalah fungsi yang ingin diintegrasikan, yaitu sin(x) dari 0 hingga π.
* Fungsi romberg() menghitung nilai integral menggunakan metode Romberg, dengan pendekatan awal menggunakan metode Trapezoidal.
* Setiap iterasi menambahkan jumlah titik pembagi dan melakukan eksstrapolasi Richardson untuk meningkatkan akurasi.
* Nilai akhir yang paling akurat berada di pojok kanan bawah dari matriks hasil Romberg.
* Parameter n menyatakan tingkat iterasi maksimum (kedalaman eksstrapolasi).

---

## Contoh Output Terminal

Tabel Romberg:
```````````````````````````````````````````````````````````````````````````````
[[1.92367096e-16 ``` 0.00000000e+00 ``` 0.00000000e+00 ``` 0.00000000e+00 ``` 0.00000000e+00]
 [1.57079633e+00 ``` 2.09439510e+00 ``` 0.00000000e+00 ``` 0.00000000e+00 ``` 0.00000000e+00]
 [1.89611890e+00 ``` 2.00455975e+00 ``` 1.99857073e+00 ``` 0.00000000e+00 ``` 0.00000000e+00]
 [1.97423160e+00 ``` 2.00026917e+00 ``` 1.99998313e+00 ``` 2.00000000e+00 ``` 0.00000000e+00]
 [1.99357034e+00 ``` 2.00001659e+00 ``` 2.00000024e+00 ``` 2.00000000e+00 ``` 1.99999999e+00]]

Hasil integrasi sin(x) dari 0 sampai pi: 1.9999999945872902
```````````````````````````````````````````````````````````````````````````````

---

## Screenshot Output
![WhatsApp Image 2025-06-15 at 19 42 34_72e5c1fb](https://github.com/user-attachments/assets/0a70f77b-bc3f-4e6f-a758-dfda9da90a35)

---

## Kesimpulan

- Metode Romberg secara efektif mengatasi kelemahan metode Trapezoidal yang membutuhkan banyak interval untuk mencapai akurasi tinggi.
- Dengan eksstrapolasi Richardson, hasil integrasi dapat dicapai dengan akurasi sangat tinggi hanya dalam beberapa iterasi.
- Dalam kasus integrasi fungsi sin(x) dari 0 hingga π, hasil mendekati angka eksak 2 tercapai dengan cepat.

```
