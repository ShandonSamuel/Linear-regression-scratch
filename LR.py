import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,3,5,7,9,11])
y = np.array([1,3,2,5,7,8])

f = plt.scatter(x,y,marker='o')
plt.imshow()

x_sum = sum(x)
y_sum = sum(y)

x_y = sum(x*y)
x_2 = sum(x**2)

n = len(x)

num_m = n*(x_y)-((x_sum*y_sum))

den_m = n*(x_2)-(x_sum**2)

m = num_m/den_m
num_b = y_sum - m*(x_sum)
den_b = n
b = num_b/den_b
def bf():
    y_fit = m * x + b
    print("Fitted y values:", y_fit)

    plt.scatter(x, y, color='blue', label="Data Points")
    plt.plot(x, y_fit, color='red', label="Line of Best Fit")

    plt.xlabel("X values")
    plt.ylabel("Y values")
    plt.title("Scatter Plot with Line of Best Fit")
    plt.legend()

    plt.show()

    print("Slope (m):", m)
    print("Intercept (b):", b)

    inp()

def inp():
    e = float(input("Enter a new X value to predict Y: "))

    y_new = m * e + b
    print("Predicted Y value:", y_new)

    y_fit = m * x + b
    plt.scatter(x, y, color='blue', label="Data Points")
    plt.plot(x, y_fit, color='red', label="Line of Best Fit")
    plt.scatter(e, y_new, color='green', label="New Data Point", zorder=5)

  
    plt.xlabel("X values")
    plt.ylabel("Y values")
    plt.title("Scatter Plot with Line of Best Fit and New Prediction")
    plt.legend()

    plt.show()

bf()
