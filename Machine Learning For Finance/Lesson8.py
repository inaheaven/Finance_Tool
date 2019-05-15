import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo


def f(x):
    y = (x-1.5)**2 + 0.5
    print("x= {}, y={}".format(x,y))
    return y

def test_run():
    xguess = 2.0
    min_result = spo.minimize(f, xguess, method='SLSQP', options={'disp': True})
    print("minma found at:")
    print("x={}, y={}".format(min_result.x, min_result.fun))

    xplot = np.linspace(0.5, 2.5, 21)
    yplot = f(xplot)
    plt.plot(xplot, yplot)
    plt.plot(min_result.x, min_result.fun, 'ro')
    plt.title("minima of an  objective funcytion")
    plt.show()

if __name__ == "__main__":
    test_run()
