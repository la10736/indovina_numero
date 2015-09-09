numero_da_indovinare = 1234
tentativi = 0

while True:
    tentativi = tentativi + 1
    print("--- Tentativo numero " + str(tentativi) + ".")
    tentativo = input("Inserisci un numero: ")
    numero_provato = int(tentativo)
    if numero_provato == numero_da_indovinare:
        print("BRAVO!!!! Hai indovinato in " + str(tentativi) + " tentativi.")
        import sys
        sys.exit()
    print("Peccato non hai indovinato... prova ancora!")
