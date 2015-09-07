numero_da_indovinare = 42
print("#### INDOVINA IL NUMERO ####")

tentativo = input("Inserisci un numero: ")
if numero_da_indovinare == int(tentativo):
    print("Bravo hai indovinato!")
else:
    print("Peccato riprova")
