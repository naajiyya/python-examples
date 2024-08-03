# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

data=input()
data
print(data)
upper=0
for value in data:
    if value.isupper() :
        upper=upper+1
        #upper+=1
print(upper)
dir(data)
 
lower=0
for value in data:
    if value.islower():
        lower=lower+1
print(lower)        

upper=0
lower=0 
for value in data:
    if value.isupper():
        upper=upper+1
    else:               
        lower=lower+1
print(lower)
print(upper)

data=input("enter a string contains upper,lower,numbers")
upper=0
lower=0 
other=0
for value in data:
    if value.isupper():
        upper=upper+1
    elif value.islower():               
        lower=lower+1
    else:
        other=other+1
print(lower)
print(upper)
print(other)

import numpy as np
a=np.random.randint(0,100,10)
a        
type(a)
list1=list(a)
list1
dir(a)
maximum=list1[0]
for value in a:
    if maximum >value:
        pass
    else:
        maximum=value
print(maximum)
list2=list(a)
list2
minimum=list2[0]

for value in list2:
    if minimum<value:
        pass
    else:
        minimum=value
print(minimum)        
f=['orange','apple','grapes','watermelone']
len(f)
print(f[0])
(f[1])
(f[2])
len(f[0])
len(f[1])
len(f[2])
len(f[3])
g=[]
for value in f:
    g.append(len(value))
print(g) 
h=[34,56.98,-76,2+3j,10,45.7,'true','false','bot','cat']   
dir(list)
for value in h:
   h.pop()
   if len(h)==0:
        print('succsessfully completed')
        
