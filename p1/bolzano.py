# https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/
# https://www.codesansar.com/numerical-methods/bisection-method-python-program.htm

import matplotlib.pyplot as plt
import numpy as np

# Defining Function


def f(x):
    return x**3 - 3 * x + 1

# Implementing Bisection Method


def bisection(x0, x1, e):
    count = 1
    condition = True

    while condition:
        x2 = (x0 + x1) / 2
        print("Iteration-%d, x2 = %0.6f and f(x2) = %0.6f" %
              (count, x2, f(x2)))

        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2

        count += 1
        condition = abs(f(x2)) > e

    return x2

# # Note: You can combine above two section like this
# x0 = float(input("First Guess: "))
# x1 = float(input("Second Guess: "))
# e = float(input("Tolerable Error: "))


x0 = 1
x1 = 3
e = 0.1

# Checking Correctness of initial guess values and bisecting
if f(x0) * f(x1) > 0.0:
    print("Given values do not bracket the root.")
    print("Try Again with different guess values.")
else:
    root = bisection(x0, x1, e)
    print("\nRequired Root is : %0.8f" % root)

x = np.arange(x0, x1, e)
y = f(x)


def buildGraph():
    plt.plot(x, y, color = "#FF00FF", label = "f(x)", zorder = 0)
    plt.axvline(x = root, ymin = 0, ymax = 1, color = "green", zorder = 1)
    plt.scatter(root, f(root), color = "green",
                linewidths = 0.5, label = "Root", zorder = 2)
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.title("Bolzano Method")
    plt.legend()
    plt.show()


buildGraph()