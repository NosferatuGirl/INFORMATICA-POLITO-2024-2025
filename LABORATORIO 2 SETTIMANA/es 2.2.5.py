#2.2.5

matricola1 = 'S301888'
matricola2 = 'S800123'

lettera = matricola1[0]

valore1 = int(matricola1[1:])
valore2 = int(matricola2[1:])

if valore1 > valore2:
    print(valore1,valore2)
else:
    print(valore2,valore1)