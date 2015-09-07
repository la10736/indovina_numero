numero_da_indovinare = 1234

while True:
    tentativo = input("Inserisci un numero: ")
    numero_provato = int(tentativo)
    if numero_provato == numero_da_indovinare:
        print("BRAVO!!!! Hai indovinato")
        import sys
        sys.exit()
    print("Peccato non hai indovinato... prova ancora!")
