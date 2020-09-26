import numpy as np

def testlocalfunction(number):
    result = number * 2
    return result

def testlocalfunction2(dim, number):
    V = np.ones(dim)
    result = V * testlocalfunction(number) * 40
    return result
