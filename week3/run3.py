import datasets
import regression
import numpy as np
import matplotlib.pyplot as plt

X, Y = datasets.load_linear_example1()
ex_X = datasets.polynomial2_features(X)

model = regression.RidgeRegression()
print(f"{model.alpha=}")
model.fit(ex_X, Y)
print(f"{model.theta=}")