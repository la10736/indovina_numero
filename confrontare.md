# Confrontare e decidere

*Basta con i nomi!* Per prima cosa cambiamo il programma in modo tale che esegua le seguenti azioni:

1. si presenta brevemente;
2. chiede all'utente di inserire un numero;
3. visualizza un messaggio con il numero che è stato inserito.

Il risultato del vostro programma dovrebbe assomigliare a questo:

    #### INDOVINA IL NUMERO ####
    Inserisci un numero: 42
    Hai inserito il numero 42

## Giochiamo con i confronti

Ora interroghiamo la console per cercare di capire cosa è vero e cosa è falso. In *Python* si usa `==` per verificare
se due cose sono uguali ( **attenzione**: uguali non vuol dire necessariamente che siano *la stessa cosa*). Fate pure
qualche esperimento sapendo che `True` significa vero e `False` significa falso.

... Vi siete convinti che funziona? `42 == 42` scrive `True`? `42 == 11` scrive `False`? Allora possiamo sperimentare 
 nel nostro programma se il giocatore inserisce il numero `42`: **provate a vedere se riuscite a fare questo**
 
    #### INDOVINA IL NUMERO ####
    Inserisci un numero: 42
    Hai inserito il numero 42
    True

Due piccoli indizi:

1. Potete usare l'istruzione `print(qualcosa vero o falso)` per far scrivere a *Python* `True` o `False`.
2. Una stringa è sempre diversa da un numero: provate a usare `int(stringa)` e riuscirete a trasformare le stringhe in
numeri

## Cambiare comportamento

Ora vogliamo che il programma si comporti così:

    #### INDOVINA IL NUMERO ####
    Inserisci un numero: 33
    Peccato non hai indovinato... prova ancora!
    
    #### INDOVINA IL NUMERO ####
    Inserisci un numero: 42
    BRAVO!!!! Hai indovinato

Quindi se il numero è uguale a quello definito scrive `Bravo hai indovinato`, altrimenti scrive `Peccato non hai
indovinato... prova ancora!` La costruzione per fare queste cose in *Python* è molto semplice:

```python
if <condizione> :
    quello che bisogna fare
    se la condizione è vera
else:
    quello che bisogna fare
    se la condizione è false
```

Il blocco contenuto tra `if` e `else` deve essere **rientrato di 4 spazi** come quello dopo `else`. Quando si smette 
di scrivere eliminando il rientro finisce il blocco della condizione.

Bene, ora provate a sperimentare sulla console, ma poi cambiate il programma e fatelo funzionare come si deve.

## Dove siamo adesso

Ora inizia a somigliare a quello che dovrebbe essere, ricordatevi solo che se il numero da indovinare si chiamasse
`numero_da_indovinare` basterebbe cambiare questa definizione per cambiare il numero. Le cose dovrebbero essere
pressapoco [così](confrontare.py)

* Prossimo: [Provare e riprovare](ciclo.md)
* Precedente: [Leggere e Scrivere](leggere_scrivere.md)