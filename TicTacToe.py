# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 09:47:28 2020

@author: piotr
"""
import random
import numpy as np
import copy

''' KÓŁKO I KRZYŻYK '''

def plansza(znak_pola):
    pola = [(0,0), (0,2), (0,4), (2,0), (2,2), (2,4), (4,0), (4,2), (4,4)]
    
    for j in range(5): 
        for i in range(5):
            if (j,i) in pola:
                if znak_pola[pola.index((j,i))] == 1:
                    print('X', end='')
                if znak_pola[pola.index((j,i))] == 2: 
                    print('O', end='')
                if znak_pola[pola.index((j,i))] == 0: 
                    print(' ', end='')

            if j%2 == 0:
                if i%2 == 1:
                    print('|', end='')
            else: 
                print('_', end ='')
        print('')
    print('')

def ruch(gracz, znak_pola):
    r=random.randint(0,8)
    while znak_pola[int(r)] != 0:
        r=random.randint(0,8)
    znak_pola[int(r)] = gracz
    return r

def czlowiek(gracz, znak_pola):
    plansza(znak_pola)
    r=input()
    while znak_pola[int(r)] != 0:
        r=input()
    znak_pola[int(r)] = gracz
    return r
       
def kto_wygral (X, gracz):
    wygrane=[(0,4,8), (0,3,6), (0,1,2), (2,5,8), (2,4,6), (6,7,8), (3,4,5), (1,4,7)]
    for i in wygrane:
        x,y,z = i
        if (x in X) and (y in X) and (z in X):
            #print ('wygrywa gracz', gracz, i)
            return True
    
def ruchQ(gracz, znak_pola, ind):
    if random.randint(0,9) == 9 :
        r=random.randint(0,8)
        znak_pola[int(r)] = gracz
    else:
        maxQ=max(Q[ind])
        i=Q[ind].index(maxQ)
        r=akcje[ind][i]
        znak_pola[int(r)] = gracz
    return r
           
znak_pola = [0, 0, 0, 0, 0, 0,0, 0, 0]
O=[]
X=[]
nagroda = 0
a = 0.2
y = 0.9 
licz=0

#STANY I MOZLiWE AKCJE
stany=[]

for a in range (3):
    for b in range (3):
        for c in range (3):
            for d in range (3):
                    for e in range (3):
                            for f in range (3):
                                    for g in range (3):
                                            for h in range (3):
                                                    for i in range (3):
                                                        stany.append([a,b,c,d,e,f,g,h,i])
                                                        

akcje=[]
for i in range(19683):
    akcje.append([])
    for j in range(9):
        if stany[i][j] == 0:
            akcje[i].append(j)
 
Q=[]
Q=copy.deepcopy(akcje)

for i in range(len(Q)):
    for j in range(len(Q[i])):
        if Q[i][j] != None: 
            Q[i][j]= 1 #random.uniform(-1,0)
###
for j in range(1000):            
    O=[]
    X=[]
    ruchy=[]
    nagroda = 0
    a = 0.2
    y = 0.95    
    znak_pola = [0, 0, 0, 0, 0, 0,0, 0, 0]        
    for i in range(9):
            if i%2 == 0: #GRACZ LOSOWY
                gracz = 1
                O.append(ruch(gracz, znak_pola))
                #plansza(znak_pola)
            else:
                gracz = 2 #Q LEARNING
                ind=stany.index(znak_pola)
                X.append(ruchQ(gracz, znak_pola, ind))
                n_ind=stany.index(znak_pola)
                ruchy.append(n_ind)
            if kto_wygral(X,gracz) == True or kto_wygral(O,gracz) == True :
                if gracz == 1:
                    nagroda = -1
                    id_max=Q[ind].index(max(Q[ind]))
                    Qmax=Q[ind][id_max]
                    max_future_q = max(Q[n_ind])
                    new_Q = Qmax + a*(nagroda + y* max_future_q - Qmax)
                    Q[ind][id_max] = new_Q  
                else:
                    nagroda = 1
                    licz+=1
                    id_max=Q[ind].index(max(Q[ind]))
                    Qmax=Q[ind][id_max]
                    max_future_q = max(Q[n_ind])
                    new_Q = Qmax + a*(nagroda + y* max_future_q - Qmax)
                    Q[ind][id_max] = new_Q 
                break
            if i == 8:
                nagroda = 0
                licz+=1
                break
        
    for ind in ruchy:
        #print(j,gracz,stany[ind])
        id_max=Q[ind].index(max(Q[ind]))
        Qmax=Q[ind][id_max]
        max_future_q = max(Q[n_ind])
        new_Q = Qmax + a*(nagroda + y* max_future_q - Qmax)
        Q[ind][id_max] = new_Q  
    
print(licz)


for i in range(9):
            if i%2 == 0: #GRACZ LOSOWY
                gracz = 1
                O.append(czlowiek(gracz, znak_pola))
                plansza(znak_pola)
            else:
                gracz = 2 #Q LEARNING
                ind=stany.index(znak_pola)
                X.append(ruchQ(gracz, znak_pola, ind))
                n_ind=stany.index(znak_pola)
                ruchy.append(n_ind)
            if kto_wygral(X,gracz) == True or kto_wygral(O,gracz) == True :
                if gracz == 1:
                    nagroda = -1
                    id_max=Q[ind].index(max(Q[ind]))
                    Qmax=Q[ind][id_max]
                    max_future_q = max(Q[n_ind])
                    new_Q = Qmax + a*(nagroda + y* max_future_q - Qmax)
                    Q[ind][id_max] = new_Q  
                else:
                    nagroda = 1
                    licz+=1
                    id_max=Q[ind].index(max(Q[ind]))
                    Qmax=Q[ind][id_max]
                    max_future_q = max(Q[n_ind])
                    new_Q = Qmax + a*(nagroda + y* max_future_q - Qmax)
                    Q[ind][id_max] = new_Q 
                break
            if i == 8:
                nagroda = 0
                licz+=1
                break 