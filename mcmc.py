import numpy as np
import np.random
import matplotlib.pyplot as plt

def mh_one(f, x, jump):
    x_next = jump(x)
    a = f(x_next) / f(x)
    if a >= 1:
        return x_next
    elif np.random.rand() <= a:
        return x_next
    else:
        return x_prev

def mh(f, x):
    sigma = 5
    def gauss_jump(x):
        return np.random.normal(x, sigma ** 2)

    for _ in range(100):
        x = mh_one(f, x, gauss_jump)

    total = 0
    count = 0
    for i in range(1000):
        x = mh_one(f, x, gauss_jump)
        if i % 3 == 0:
            total += f(x)
            count += 1

    return total / count

if __name__ == "__main__":
    def gauss(x):
        return exp(-(x ** 2) / 2)

    print(mh(gauss, 0))
