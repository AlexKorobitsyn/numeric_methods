import math

epsilon = 0.5 * 10**-5

def f(x):
    return math.sin(x) - x + 2.7


def df(x):
    return math.cos(x) - 1


def dichotomies(a, b):
    n = 0
    while abs(b-a) > epsilon:
        x0 = (a+b)/2
        if f(a)*f(x0) < 0:
            b = x0
        elif f(b)*f(x0) < 0:
            a = x0
        n += 1
    x = (a+b)/2
    return x, n

# c, t = dichotomies(2, math.pi)
# print(c, t)


def methods_newton(a, b):
    m = 2
    x = a
    x1 = x - f(x) / df(x)
    x2 = 0
    n = 0
    while abs(f(x))/m > epsilon:
        x2 = x1 - f(x1)/df(x1)
        x = x1
        x1 = x2
        n += 1
    return x2, n

# print(methods_newton(2, math.pi))

def modified_newton_method(a, b):
    m = 2
    x = a
    x0 = a
    x1 = x - f(x) / df(x)
    x2 = 0
    n = 0
    while abs(f(x))/m > epsilon:
        x2 = x1 - f(x1)/df(x0)
        x = x1
        x1 = x2
        n += 1
    return x2, n

# print(modified_newton_method(2, math.pi))


def chord(a, b):
    n = 0
    m = 2
    x0 = a
    x1 = b
    x2 = 0
    while abs(f(x1))/m > epsilon:
        x2 = x1 - f(x1)/(f(x1) - f(x0)) * (x1 - x0)
        x1 = x2
        n += 1
    return x2, n

# print(chord(2, math.pi))


def movable_chord(a, b):
    n = 0
    m = 2
    x1 = a
    x2 = b
    while abs(f(x1)) / m > epsilon:
        x1, x2 = x2, x2 - f(x2) / (f(x2) - f(x1)) * (x2 - x1)
        n += 1
    return x2, n

# print(movable_chord(2, math.pi))


def simple_iteration(a, b):
    n = 0
    x0x = (a+b)/2
    sigm = math.sin(x0x) + 2.7
    while abs(f(sigm)/df(sigm)) > epsilon:
        sigm = math.sin(sigm) + 2.7
        n += 1
    return sigm, n

print(simple_iteration(2, math.pi))