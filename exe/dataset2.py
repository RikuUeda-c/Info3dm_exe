import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

def true_function(x):
    return np.sin(np.pi * x * 0.8) * 10

np.random.seed(0)       
n = 20                  
x_sample = np.random.uniform(-1, 1, n)  

y_sample = true_function(x_sample)


df = pd.DataFrame({
    "観測点": x_sample,
    "真値": y_sample
})

print(df) 


x = np.linspace(-1, 1, 100)
y = true_function(x)

plt.figure(figsize=(8, 5))  

plt.plot(x, y, label="True function", color="blue")

plt.scatter(df["観測点"], df["真値"], label="Samples", color="red")

plt.legend()

plt.savefig("week3/exe/ex1.2.png")

plt.show()