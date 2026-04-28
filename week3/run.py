import datasets
import importlib
import regression
importlib.reload(regression)
X,Y = datasets.load_linear_example1()
model = regression.LinearRegression()
print(model.fit(X,Y))
print(model.theta)
