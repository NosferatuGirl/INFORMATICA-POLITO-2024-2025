from math import *

#es 2.1.2

#faccio inserire all'utente le resistenze

resistenza1 = int(input("Inserisci R1"))
resistenza2 = int(input("Inserisci R2"))
resistenza3 = int(input("Inserisci R3"))

#calcolo la 23 in parallelo

r23 = resistenza2*resistenza3
sumr23 = resistenza2+resistenza3

resistenza23 = r23/sumr23

#calcolo rtot

rtot = resistenza23 + resistenza1

print(rtot)