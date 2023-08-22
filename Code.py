import numpy as np
import matplotlib.pyplot as plt

# Generate random data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 4, 5, 6])

# Initialize variables
a = 0
c = 0
alpha = 0.0001
iterationCount = 9000

# Iterate through the data and update the values of a and c
for w in range(iterationCount):
    diffVal_1 = 0
    diffVal_2 = 0
    for i in range(len(x)):
        y_val = (a * x[i]) + c
        diffVal_1 = diffVal_1 + ((y_val - y[i]))
        diffVal_2 = diffVal_2 + ((y_val - y[i]) * x[i])
    a = a - (alpha / len(x)) * diffVal_1
    c = c - (alpha / len(x)) * diffVal_2

# Predict the output for the training data
y_pred = (a * x) + c

# Create a scatter plot with a line to compare the real value and the expected value
plt.scatter(x, y, color="blue")
plt.plot(x, y_pred, color="red")

# Show the scatter plot
plt.show()