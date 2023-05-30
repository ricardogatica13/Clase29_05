import numpy as np
import random

#1
array = np.arange(100)
for i in array:
    array[i] = random.randint(0,10)
    
print (array)

for i in range(len(array)):
    if i %2 == 0 :
        print(array[i])
    


print (array.max())
print("")

for i in range(len(array)):
   