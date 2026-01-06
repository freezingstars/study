d = lambda f: f(4)
def square(x):
    return x*x
print(d(square))
higher_order_lambda = lambda f: lambda x: f(x)
g = lambda x: x * x
print(higher_order_lambda(g)(2))

