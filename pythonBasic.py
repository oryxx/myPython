# learning numpy
import pandas as pd
import numpy as np
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)
a = 10
b = 10
c = np.array([1, 2, 3])
d = a + b
