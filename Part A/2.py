import numpy as np
import pandas as pd

lst = np.array([12, 7, 9, 4, 15, 20, 3, 18])

print("Even Numbers:", lst[lst % 2 == 0])
print("Odd Numbers:", lst[lst % 2 != 0])




