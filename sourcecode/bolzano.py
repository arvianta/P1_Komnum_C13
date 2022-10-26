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