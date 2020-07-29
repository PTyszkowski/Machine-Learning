# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 11:52:41 2020

@author: piotr
"""
import numpy as np
import random as rd 

#FUNKCJA ATYWACJI (PROGOWA UNIPOLARNA)   
def f(s):
    if s >= 0:
        return 1
    if s < 0:
        return 0

#FUNKCJA LOGICZNA DO NAUCZENIA SIĘ   XOR(d=[0,1,1,0]) XNOR(d=[1,0,0,1]) nie jest liniowo separowalne
A=np.array([0,0,1,1])
B=np.array([0,1,0,1])
d=np.array([1,1,0,0])  

#WAGI
W=np.array([1.,0,1.])

#LICZNIK EPOK
j=0

#WSPÓŁCZYNNIK UCZENIA SIĘ
alpha=0.4

while j <= 25:
    print("\n", "epoka", j+1)
    a=[0,1,2,3]
    rd.shuffle(a)
    poprawne = 0
    for i in a: 
        #WEJŚCIA 
        X = np.array([1,A[i],B[i]])
      
        #POBUDZENIE
        s = np.dot(np.transpose(W),X)
        print(X[1:],f(s))
        #KOREKTA WAG
        W = W + (alpha * ((d[i] - f(s)) * X))
        if(f(s) == d[i]):
            poprawne+=1
    print("poprawnosc ", poprawne/4)
    j+=1
    if poprawne/4 == 1:
        break     
    
    
""" TESTOWANIE"""
poprawne = 0 
print("_____TESTOWANIE_____")
for q in range (101):
    i = rd.randint(0,3)
    X = np.array([1,A[i],B[i]])
    s = np.dot(np.transpose(W),X)
    if f(s) == d[i]:
        poprawne+=1
print("poprwnosc ", poprawne/(q+1))    
    