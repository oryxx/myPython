import numpy as np
import timeit

a = np.arange(10000)

b = range(10000)

t = timeit.Timer('x=(i for i in range(100))')
ts = t.timeit()
print(ts)



