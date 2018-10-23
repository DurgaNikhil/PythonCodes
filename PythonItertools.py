"""
Python program dealing with the 
iteraters 

"""

import itertools

x = 0
#Infinite cycling 
for c in itertools.cycle(" Hello world "):
    print(c)
    x = x +1
    if x > 10:
        break