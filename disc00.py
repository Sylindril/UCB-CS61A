def f(x):
    return x - 1

def g(x):
    return 2 * x

def h(x, y):
    return int(str(x) + str(y))

'''
>>> f(5) = 4, g(5) = 10, h(4, 5) = 45
h(20, 24)
'''


print(h(g(g(5)), h(f(f(f(5))), f(5))))