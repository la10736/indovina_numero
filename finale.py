import random

minimo = 0
massimo = 2000
numero_da_indovinare = random.randint(minimo, massimo)
# numero_da_indovinare = 1234
tentativi = 0


def messaggio_intro(numero_tentativo):
    return "--- Tentativo numero " + str(tentativi) + "."


def stampa_intro(numero_tentativo):
    print(messaggio_intro(numero_tentativo))


def dentro_intervallo(numero, min_val, max_val):
    return min_val <= numero <= max_val


def fuori_intervallo(numero, min_val, max_val):
    return not dentro_intervallo(numero, min_val, max_val)


def messaggio_inserisci_intervallo(min_val, max_val):
    return "Inserisci un numero tra " + str(min_val) + " e " + str(max_val) + ":"


def messaggio_inserimento_non_corretto(inserimento):
    return "Ma chi vuoi prendere in giro? '" + inserimento + "' non è un numero!"


def chiedi_numero(messaggio):
    while True:
        tentativo = input(messaggio)
        try:
            return int(tentativo)
        except:
            print(messaggio_inserimento_non_corretto(tentativo))


def chiedi_numero_in_intervallo(min_val, max_val):
    numero_provato = min_val - 1
    while fuori_intervallo(numero_provato, min_val, max_val):
        numero_provato = chiedi_numero(messaggio_inserisci_intervallo(min_val, max_val))
    return numero_provato


def messaggio_indovinato(numero_prove):
    return "BRAVO!!!! Hai indovinato in " + str(numero_prove) + " tentativi."


def esci():
    import sys
    sys.exit()


def esci_se_uguale(obbiettivo, numero):
    if numero == obbiettivo:
        esci()


def messaggio_base_indizi():
    return "Peccato non hai indovinato... prova ancora con un numero più "


def messaggio_info(numero_prove, obbiettivo, valore):
    if valore == obbiettivo:
        return messaggio_indovinato(numero_prove)
    if valore > obbiettivo:
        return messaggio_base_indizi() + "basso"
    return messaggio_base_indizi() + "alto"


def stampa_info(numero_prove, obbiettivo, valore):
    print(messaggio_info(numero_prove, obbiettivo, valore))


while True:
    tentativi = tentativi + 1
    stampa_intro(tentativi)
    numero_provato = chiedi_numero_in_intervallo(minimo, massimo)
    stampa_info(tentativi, numero_da_indovinare, numero_provato)
    esci_se_uguale(numero_da_indovinare, numero_provato)
