#es 2.2.1
# Memorizzare la stringa in una variabile
stringa = input("Inserisci la frase: ")  # Puoi cambiare questo valore per testare altre stringhe

# Controllare la lunghezza della stringa
lunghezza = len(stringa)

if lunghezza < 3:
    risultato = stringa  # Se la stringa è più corta di 3 caratteri, visualizza la stringa completa
elif lunghezza < 6:
    risultato = stringa  # Se la stringa è più corta di 6 caratteri, visualizza la stringa completa
else:
    # Costruire la stringa di output
    primo_terzo = stringa[:3]  # I primi tre caratteri
    ultimo_terzo = stringa[-3:]  # Gli ultimi tre caratteri
    risultato = f"{primo_terzo}...{ultimo_terzo}"  # Formato finale

# Visualizzare il risultato
print(risultato)