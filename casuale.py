import random

minimo = 0
massimo = 2000
numero_da_indovinare = random.randint(minimo, massimo)
tentativi = 0

while True:
    tentativi = tentativi + 1
    print("--- Tentativo numero " + str(tentativi) + ".")
    tentativo = input("Inserisci un numero tra " + str(minimo) + " e " + str(massimo) + ":")
    numero_provato = int(tentativo)
    if numero_provato == numero_da_indovinare:
        print("BRAVO!!!! Hai indovinato in " + str(tentativi) + " tentativi.")
        import sys
        sys.exit()
    messaggio_riprova = "Peccato non hai indovinato... prova ancora con un numero più "
    if numero_provato > numero_da_indovinare:
        messaggio_riprova = messaggio_riprova + "basso"
    if numero_provato < numero_da_indovinare:
        messaggio_riprova = messaggio_riprova + "alto"
    print(messaggio_riprova + ".")
