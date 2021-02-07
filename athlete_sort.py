#https://www.hackerrank.com/challenges/python-sort-sort/problem
import math
import os
import random
import re
import sys

if __name__ == '__main__':
   nm = input().split()

   n = int(nm[0])

   m = int(nm[1])

   arr = []

   for _ in range(n):
      arr.append(list(map(int, input().rstrip().split())))

   k = int(input())
   """
   def sort(array, z):
      for i in range(z-1):
         temp = array[i][k]
         temp2 = array[i]
         if temp > array[i+1][k]:
            array[i] = array[i+1]
            array[i+1] = temp2 
         elif array[i-1][k] > temp:
            array[i] = array[i-1]
            arr[i-1] = temp2 
   """      
   new = sorted(arr, key=lambda x: x[k])

   for element in new:
      for i in element:
         print(i, end=' ')
      print()