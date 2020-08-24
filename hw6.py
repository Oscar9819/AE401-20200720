# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 16:35:53 2020

@author: user
"""

names=[]
total = 0



n = input('有幾位同學')
n = int(n)

for i in range(n):
    name = input('同學名字')
    names.append(name)
    
    name = input('同學數學成績')
    name = int(name)
    names.append(name)


for i in range(1,2*n,2):
    total = total+names[i]

print("平均分:",(total/n))

highest=0
for i in range(1,2*n,2):
    if names[i] > highest:
        highest = names[i]
        highestname = names[i-1]
print(highestname, '最高分:',highest)        
 
lowest=100
for i in range(1,2*n,2):
    if names[i] < lowest:
        lowest = names[i]
        lowestname = names[i-1]
print(lowestname, '最低分:',lowest)



