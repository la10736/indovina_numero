# Confrontare e decidere

Per prima cosa invece di chiedere il nome cambiamo il programma dove per prima cosa si presenta e poi chiede un numero
e scrive indietro il numero che è stato scritto : *basta con i nomi*!

Il risultato del vostro programma deve diventare circa

    #### INDOVINA IL NUMERO ####
    Inserisci un numero: 42
    Hai inserito il umero 42

## Giochiamo con i confronti

Ora interroghiamo la console per cercare di capire cosa è vero e cosa è falso. In *Python* si usa `==` per verificare
se due cose sono uguali (**attenzione** uguali, non vuol dire necessariamente *la stessa cosa*). Fate pure qualche 
esperimento sapendo che `True` significa vero e `False` significa falso.


... Vi siete convinti che funziona? `42 == 42` scrive `True`? `42 == 11` scrive `False`? Allora possiamo sperimentare 
 nel nostro programma se il giocatore inserisce il numero `42`: **provateci... se ci riuscite a fare questo**
 
    #### INDOVINA IL NUMERO ####
    Inserisci un numero: 42
    Hai inserito il umero 42
    True

Due piccoli indizi:

1. Potete fare `print(qualcosa vero o falseo)` per vedere `True` o `False`
2. Una stringa è sempre diversa da un numero: provate a usare `int(stringa)` e riuscirete a trasformare le stringhe in
numeri

## Cambiare comportamento

Ora vogliamo che il programma si comporti così:

    #### INDOVINA IL NUMERO ####
    Inserisci un numero: 33
    Peccato, non è il numero giusto: riprova.
    
    #### INDOVINA IL NUMERO ####
    Inserisci un numero: 42
    Bravo hai indovinato!

Quindi se il numero è uguale a quello definito scrive `Bravo hai indovinato`, altrimenti scrive `Peccato, non è il 
numero giusto: riprova.` La costruzione per fare queste cose in *Python* è molto semplice:

```python
if <condizione> :
    quello che bisogna fare
    se la condizione è vera
else:
    quello che bisogna fare
    se la condizione è false
```

Il blocco contenuto tra `if` e `else` deve essere **rientrato di 4 spazi** come quello dopo `else`. Quando si smette 
di scrivere lasciando gli spazi finisce il blocco della condizione.

Bene ora provate pure a sperientare sulla console, ma poi cambiate il programma e fatelo funzionare come si deve.

## Dove siamo adesso

Bene ora inizia a somigliare a quello che dovrebbe venire, ricordatevi solo che se il numero da indovinare si chiamasse
`numero_da_indovinare` basterebbe cambiare questa definizione per cambiare il numero. Le cose dovrebbero errere
pressapoco [così](confrontare.py)

Prossimo: [Provare e riprovare](ciclo.md)
Precedente: [Leggere e Scrivere](leggere_scrivere.md)