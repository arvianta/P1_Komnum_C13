# Praktikum 1 Komputasi Numerik 
## _Praktikum Komputasi Numerik Mengenai Pencarian Akar Persamaan dengan Metode Bolzano_

- Rayhan Arvianta Bayuputra - 5025211217
- Armadya Hermawan Sarwono - 5025211243

### SOAL
#### Anda sudah mengerti algoritma pemrosesan metode Bolzano, dan anda sudah memahami cara kerjanya. Sekarang anda tinggal mengimplementasikan algoritma tersebut menjadi sebuah program komputer metode Bolzano (yang dapat menampilkan proses iteratif numerik, lengkap dengan grafik fungsinya).

#### _Implementasi kode dalam melakukan iterasi_
```python
import numpy as np
import matplotlib.pyplot as plt

# Mendefinisikan fungsi

def f(x):
    return (x**3 - 3 * x + 1)


iterasi_maks = 50
ketelitian = 10E-6
x1 = float(input("Masukkan nilai x1: "))
x2 = float(input("Masukkan nilai x2: "))

# Memeriksa apakah value x1 dan x2 sesuai syarat
if f(x1) * f(x2) > 0:
    print('Angka tidak memenuhi kriteria bolzano (f(x1) dan f(x2) bertanda sama)')
    print("Silahkan coba kembali dengan nilai x1 dan x2 yang berbeda")
    exit()


print('-----------------------------------------------------------------------------------------------------------')
print('Iterasi \t x1\t\t x2\t\t xt\t\t f(x1)\t\t f(x2)\t\t f(xt)        ')
print('-----------------------------------------------------------------------------------------------------------')

for i in range(iterasi_maks):
    xt = (x1 + x2)/2

    # Output hasil sesuai iterasi
    print(str(i + 1)+'\t\t% 10.8f\t% 10.8f\t% 10.8f\t% 10.8f\t% 10.8f\t% 10.8f\t' %
          (x1, x2, xt, f(x1), f(x2), f(xt)))

    if np.abs(f(xt)) < ketelitian:
        print(
            '-----------------------------------------------------------------------------------------------------------')
        print('Nilai akar: ' + str(xt))
        break

    if f(x1) * f(xt) < 0:
        x2 = xt

    else:
        x1 = xt

print('-----------------------------------------------------------------------------------------------------------')
print("\n")
```

#### _Contoh output program dengan x1 = 1 dan x2 = 3_
```
-----------------------------------------------------------------------------------------------------------
Iterasi          x1              x2              xt              f(x1)           f(x2)           f(xt)
-----------------------------------------------------------------------------------------------------------
1                1.00000000      3.00000000      2.00000000     -1.00000000      19.00000000     3.00000000
2                1.00000000      2.00000000      1.50000000     -1.00000000      3.00000000     -0.12500000
3                1.50000000      2.00000000      1.75000000     -0.12500000      3.00000000      1.10937500
4                1.50000000      1.75000000      1.62500000     -0.12500000      1.10937500      0.41601562
5                1.50000000      1.62500000      1.56250000     -0.12500000      0.41601562      0.12719727
6                1.50000000      1.56250000      1.53125000     -0.12500000      0.12719727     -0.00338745
7                1.53125000      1.56250000      1.54687500     -0.00338745      0.12719727      0.06077194
8                1.53125000      1.54687500      1.53906250     -0.00338745      0.06077194      0.02841043
9                1.53125000      1.53906250      1.53515625     -0.00338745      0.02841043      0.01244122
10               1.53125000      1.53515625      1.53320312     -0.00338745      0.01244122      0.00450934
11               1.53125000      1.53320312      1.53222656     -0.00338745      0.00450934      0.00055656
12               1.53125000      1.53222656      1.53173828     -0.00338745      0.00055656     -0.00141654
13               1.53173828      1.53222656      1.53198242     -0.00141654      0.00055656     -0.00043027
14               1.53198242      1.53222656      1.53210449     -0.00043027      0.00055656      0.00006308
15               1.53198242      1.53210449      1.53204346     -0.00043027      0.00006308     -0.00018361
16               1.53204346      1.53210449      1.53207397     -0.00018361      0.00006308     -0.00006027
17               1.53207397      1.53210449      1.53208923     -0.00006027      0.00006308      0.00000140
-----------------------------------------------------------------------------------------------------------
Nilai akar: 1.5320892333984375
-----------------------------------------------------------------------------------------------------------
```

#### _Implementasi kode dalam menampilkan grafik_

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100) 

y = (x**3 - 3 * x + 1)

# mengatur axis di pusat
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')


plt.plot(x, y, 'g', color = "#FF00FF")
plt.title("Grafik Fungsi f(x)")
# show the plot
plt.show()
```

#### _Output Grafik Fungsi f(x)_
![image](https://user-images.githubusercontent.com/88714570/198074332-f1a539e6-0d29-48a1-ae4e-b8ce5cb42091.png)
