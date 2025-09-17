#esercizio 1.2.6
# Definiamo le variabili iniziali
saldo_iniziale = 1000  # Saldo iniziale in dollari
tasso_interesse = 0.05  # Tasso di interesse annuale (5%)

# Calcoliamo il saldo per i primi tre anni
saldo_anno1 = saldo_iniziale * (1 + tasso_interesse)
saldo_anno2 = saldo_anno1 * (1 + tasso_interesse)
saldo_anno3 = saldo_anno2 * (1 + tasso_interesse)

print(saldo_anno1,saldo_anno2,saldo_anno3)