#es 2.1.4

from math import *

#definisco le variabili e le costanti

q1 = float(input("Inserisci q1"))
q2 = float(input("Inserisci q2"))
r = float(input("Inserisci r"))
ε = 8.854 * 10**(-12)

#calcolo la forza di couloumb con i dati 

f = (q1*q2)/(4*pi*r**(2)*ε)
print(f)
