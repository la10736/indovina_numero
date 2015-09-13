# Tutto funziona correttamente: abbiamo finito?

Ci sono tante maniere di scrivere i programmi. Ma anche se danno lo stesso risultato non tutte sono uguali: infatti se 
avessimo usato nomi diversi per chiamare i nostri valori cosa poteva venire fuori? 

Di seguito riporto il programma dove ho solo cambiato i nomi dei valori: risulta migliore o peggiore?

```python
import random

a = 0
b = 2000
c = random.randint(a, b)
d = 0

while True:
    d = d + 1
    print("--- Tentativo numero " + str(d) + ".")
    e = a - 1
    while not a <= e <= b:
        f = input("Inserisci un numero tra " + str(a) + " e " + str(b) + ":")
        try:
            e = int(f)
        except:
            print("Ma chi vuoi prendere in giro? '" + f + "' non è un numero!")
    if e == c:
        print("BRAVO!!!! Hai indovinato in " + str(d) + " tentativi.")
        import sys
        sys.exit()
    g = "Peccato non hai indovinato... prova ancora con un numero più "
    if e > c:
        g = g + "basso"
    if e < c:
        g = g + "alto"
    print(g + ".")
```

Io lo trovo molto più difficile da capire, ma se provate a usarlo funziona uguale a quello di prima. Quindi la prima 
cosa che impariamo è che bisogna usare nomi per i valori che spiegano subito cosa è il valore, inoltre riutilizzare
vecchi nomi è inutile e non si risparmi niente: usate nomi nuovi ogni volta che avete concetti nuovi.

Comunque anche con i nomi corretti a me sembra un programma difficile da capire: 

* tutte quelle cose insime
* tante rientranze
* un programma lungo

Possiamo scriverlo meglio? Di cosa abbiamo bisogno per renderlo più semplice?

Per esempio se avessimo una funzione `dentro_intervallo(valore, minimo, massimo)` che rende `True` se `valore` è tra
minimo e massimo allora potremmo riscrivere `while not minimo <= numero_provato <= massimo` come

```python
while not dentro_intervallo(numero_provato, minimo, massimo)
```

ma ancora meglio sarebbe

```python
while fuori_intervallo(numero_provato, minimo, massimo)
```

che spiega esattamente cosa stiamo facendo.

Quindi potremmo definire funzioni che spiegano con il loro nome esattamente cosa viene fatto e il nostro programma 
potrebbe diventare qualcosa come.

```python
while True:
    tentativo = tentativo + 1
    stampa_intro(tentativo)
    numero_provato = chiedi_numero_in_intervallo(minimo, massimo)
    stampa_info(tentativo, numero_da_indovinare, numero_provato)
    esci_se_uguale(numero_da_indovinare, numero_provato)
```

Sarebbe un programma semplice capire... vediamo se riusciamo a farlo.

## Come si definisce una funzione

```python
def funzione(a, b, ... ):
    contenuto
    return valore
```

Sperimentiamo: facciamo una funzione che moltiblica gli argomenti passati. 

```python
>>> def moltiplica(a, b):
...     return a*b
... 
>>> moltiplica(2,3)
6
>>> moltiplica("a",3)
'aaa'
```

Sembra semplice, che ne dite di provare a scrivere la funzione `fuori_intervallo(numero, minimo, massimo)` e sostituirla
nel ciclo `while`. [Ecco come viene](refact_0.py).

Ora proviamo a fare 

* `stampa_intro(numero_tentativo)`
* `chiedi_numero_in_intervallo(min_val, max_val)`
* `stampa_info(numero_tentativo, obbiettivo, numero)`
* `esci_se_uguale(obbiettivo, numero)`

Un piccolo aiutino: sostituite `numero_da_indovinare = random.randint(minimo, massimo)` con il vecchio  
`numero_da_indovinare = 1234` e usate il carattere `#` per commentare la vecchia riga fino a quando il vostro programma 
non funzionerà bene come prima. Verificate provando che il gioco funziona a ogni modifica del vostro programma. Qunado
avete finito e tutto funziona bene potete rimettere il numero casuale.

Forse per fare questo ci vuole un po di tempo e tanti tentativi e la soluzione che trovate [quì](finale.py)
è un tantino esagerata (ma non troppo... si può fare molto meglio) ma credo che ora leggendo il vostro gioco capite 
subito quello che fa in ogni punto. Personalmente credo che sia sempre meglio lasciare le cose non solo funzionanti ma 
comprensibili... e trovo questo anche molto **divertente**!

