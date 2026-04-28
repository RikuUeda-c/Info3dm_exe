import datasets
import importlib
import regression
importlib.reload(regression)
X,Y = datasets.load_linear_example1()
model = regression.LinearRegression()
model.fit(X,Y)
#print(model.theta)
#print(model.predict(X))
print(model.score(X,Y))