import math

func_glob =  lambda x: 2 * x ** 3 - 3 * x ** 2 - 12 * x - 5
func_first = lambda x: 6 * x ** 2 - 6 * x - 12

a1, b1 = 0.0, 10.0

e = 0.001

def half_divide_method(a, b, f):
    x = (a + b) / 2
    while math.fabs(f(x)) >= e:
        x = (a + b) / 2
        a, b = (a, x) if f(a) * f(x) < 0 else (x, b)
    return (a + b) / 2

# import pylab
# import numpy

# X = numpy.arange(-2.0, 4.0, 0.1)
# pylab.plot([x for x in X], [func_glob(x) for x in X])
# pylab.grid(True)
#pylab.show()
