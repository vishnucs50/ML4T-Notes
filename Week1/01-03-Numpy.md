1. Creating random numpy arrays
```py
import numpy as np
np.random.random((5,4)) #5 rows, 4 cols
```
- This generates random numbers between 0.0 and 1.0 inclusive.
2. To sample from a normal distribution using numpy
```py
np.random.normal(size = (2,3))
```
- This creates a "standard normal" model with ***mean = 0*** and ***std =1***
- To change mean and std above
```py
np.random.normal(50, 10, size = (2,3))
```
- here mean = 50 and std = 10.
3. To generate random integers.
```py
np.random.randint(0, 10) # single integer between 0 and 10
np.random.randint(0, 10, size = (2, 3)) # 2 x 3 matrix 
np.random.randint(0, 10, size = 5) # 1D array
```