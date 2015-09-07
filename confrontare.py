numero_da_indovinare = 42
print("#### INDOVINA IL NUMERO ####")

tentativo = input("Inserisci un numero: ")
numero_provato = int(tentativo)
if numero_da_indovinare == numero_provato:
    print("BRAVO!!!! Hai indovinato")
else:
    print("Peccato non hai indovinato... prova ancora!")
