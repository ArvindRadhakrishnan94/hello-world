import math
import functools
def sum_number(a,b):
        count=0
        for i in range (a,b,1):
                if (i%2==0):
                        count+=i**2
        return count
print(sum_number(0,10))

