#https://www.hackerrank.com/challenges/np-arrays/problem
import numpy as np

def arrays(arr):
    a =  np.array(arr, float)
    b = np.array(a)
    for i in range(len(a)):
        temp = a[i]
        b[len(a)-1-i] = temp  
    return b

arr = input().strip().split(' ')
result = arrays(arr)
print(result)