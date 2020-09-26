# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 10:11:58 2020

@author: Casper
"""
# %%
import sympy
import math
from datetime import datetime
#print(dir(sympy))
'''
p=sympy.randprime(2**1023,2**1024)
print(len(bin(p)))
print(p)
p_bit=bin(p)
p_bit_s=p_bit[2:]
print(len(p_bit))
print(len(p_bit_s))


q=sympy.randprime(2**1023,2**1024)
print(len(bin(q)))
print(q)
q_bit=bin(q)
q_bit_s=q_bit[2:]
print(len(q_bit))
print(len(q_bit_s))


n_bit=int(p_bit_s)*int(q_bit_s)
print(len(str(n_bit)))
'''
# %%
basla=datetime.now()
p=sympy.randprime(2**1023,2**1024)
#print(len(bin(p)))
q=sympy.randprime(2**1023,2**1024)
#print(len(bin(q)))
#p=61
#q=53
n=p*q
print(len(bin(n)))
# %%

phi_n=(p-1)*(q-1)
print(len(bin(phi_n)))

# %%
#e=sympy.randprime(1,phi_n)
e=65537
print(sympy.isprime(e))
# %%
"""
for i in range(phi_n):
    print(i)
    if (phi_n*i+1)%e==0:
        d=((phi_n*i)+1)/e
 """       

# %%
# Extended Euclidean Algorithm
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b % a, a)
    return (g, x - (b // a) * y, y)

# application of Extended Euclidean Algorithm to find a modular inverse
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    return x % m
# %%
"""
def dCalculate(phi_n,e):
    for i in range(phi_n):
        if ((phi_n*i+1)%e)==0:
            return (((phi_n*i)+1)/e)
"""
# %%
#d=dCalculate(phi_n, e)
d=modinv(e,phi_n)
# %%
"""
def ASCII(s):
    x = 0
    for i in range(len(s)):
        x += ord(s[i])*2**(8 * (len(s) - i - 1))
    return x
"""
# %%
"""
import numpy as np
a = np.fromstring('hi', dtype=np.uint8)
"""
# %% encrypto
import numpy as np
ss=input("mesajınızı giriniz")
#ss="intelprobe"
a = np.fromstring(ss,dtype=np.uint8)
a=list(a)
sifreli_metin=[]
for i in range(len(a)):
    ll=int(a[i])
    lls=pow(ll,e,n)    
    sifreli_metin.append(lls)
    print(lls)



# %% dencrpyto
cozulmus=[]
for j in range(len(sifreli_metin)):
    df=pow(sifreli_metin[j],d,n)
    cozulmus.append(df)


print(''.join(chr(i) for i in a))
stop=datetime.now()

print(stop-basla)