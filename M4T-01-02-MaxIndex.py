from pickletools import uint1

import numpy as np

def test_run():
    a = np.array([9,6,2,3,12,14,7,10], dtype =  np.int32)
    print(a)

    print(f'Max value: {a.max()}')
    print(f'Index of max value: {max_index(a)}')

def max_index(a):
    return np.where(a == np.max(a))[0]

if __name__ == '__main__':
    test_run()
