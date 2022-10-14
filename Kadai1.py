'''
Created on 2022/10/14

@author: t20cs030
'''
import random

a = random.randint(0,2)
b = random.randint(0,2)
print(a)
print(b)

if a == b:
    print('あいこ')
elif (a == 0 and b == 1)or(a == 1 and b == 2)or(a == 2 and b == 0):
    print('aの勝ち')
else:
    print('bの勝ち')
    

