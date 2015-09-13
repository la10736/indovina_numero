import random

minimo = 0
massimo = 2000
numero_da_indovinare = random.randint(minimo, massimo)
tentativi = 0


def dentro_intervallo(numero, min_val, max_val):
    return min_val <= numero <= max_val


def fuori_intervallo(numero, min_val, max_val):
    return not dentro_intervallo(numero, min_val, max_val)


while True:
    tentativi = tentativi + 1
    print("--- Tentativo numero " + str(tentativi) + ".")
    numero_provato = minimo - 1
    while fuori_intervallo(numero_provato, minimo, massimo):
        tentativo = input("Inserisci un numero tra " + str(minimo) + " e " + str(massimo) + ":")
        try:
            numero_provato = int(tentativo)
        except:
            print("Ma chi vuoi prendere in giro? '" + tentativo + "' non è un numero!")
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
