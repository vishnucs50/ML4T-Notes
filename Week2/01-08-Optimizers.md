1. An optimizer help you identify what percentage of funds should be allocated to each stock.
2. How to use optimizer: 3 key steps
    1. Provide a function you want to minimize.
        - Ex: f(x) = x<sup>2</sup>+x<sup>3</sup>+ 5
        - Identify the value of x that minimizes this function.
    2. Provide an initial guess for x that you think is close to x.
        - choose random value if you don't know.
    3. call the optimizer.
    4. Gradiant Descent is a minimizer.
3. Optimizer using ***scipy***
```py
import scipy.optimize as spo

def f(X):
	"""Given a scalar X, return some value (a real number)."""
	Y = (X - 1.5)**2 + 0.5
	print ("X = {}, Y = {}".format(X, Y)) # for tracing
	return Y
	
def test_run():
	Xguess = 2.0
	min_result = spo.minimize(f, Xguess, method='SLSQP', options={'disp': True}) #This would call f(x) multiple times until a minima is found
	print ("Minima found at:")
	print ("X = {}, Y = {}".format(min_result.x, min_result.fun))
```
4. Use Scipy to minimize linear regression co-efficients.
