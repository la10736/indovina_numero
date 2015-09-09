# Conteggi

Quello che vogliamo fare ora è contare i tentativi, scrivere a ogni tentativo quanti ne sono stati fatti e infine
quando si indoviva scrivere quanti sono stati in tutto, L'aspetto di una partita sarà circa questo:

    --- Tentativo numero 1.
    Inserisci un numero: 1000
    Peccato non hai indovinato... prova ancora!
    --- Tentativo numero 2.
    Inserisci un numero: 1500
    Peccato non hai indovinato... prova ancora!
    --- Tentativo numero 3.
    Inserisci un numero: 1234
    BRAVO!!!! Hai indovinato in 3 tentativi.

## Contiamo e stampiamo i tentativi

Lasciamo stare il programma e passiamo alla console. Deviniamo un nome `tentativi` uguale a `10`. Come possiamo fare?

```python
>>> tentativi = 10
>>> tentativi
10
```

Se vogliamo aumentare `tantativi` di `1` ci basta trasformare in simboli la frase *`tentativi` uguale a `tentativi` più
`1`*.

### Contest

Provate a scrivere sulla console un ciclo in cui aumentate di `1` `tentativi` *fintanto che* `tentativi` risulta minore
do `20`. Dopo scrivete queste righe:

```python
>>> if tentativi == 20: print("HO VINTO!")
```

Se leggete `HO VINTO!` allora ci siete **riusciti!!!**

### Soluzione parziale

Per ora vogliamo fare una versione semplificata del tipo:

    1
    Inserisci un numero: 1000
    Peccato non hai indovinato... prova ancora!
    2
    Inserisci un numero: 1500
    Peccato non hai indovinato... prova ancora!
    3
    Inserisci un numero: 1234
    BRAVO!!!! Hai indovinato.

Per fare questo provate prima sulla console a scrivere
```python
>>> print(tentativi)
20
```

## Componiamo le frasi con i numeri

Ora vogliamo che prima di ogni tentativo venga stampata una frase del tipo `--- Tentativo numero 3.` dove il numro `3`
deve essere il numero del tentivo che cambia di volta in volta.

Prima siamo riusciti a scrivere frasi del tipo `Hai inserito il umero 42`, proviamo quindi ignorare il `.` finale e 
vediamo se riuasciamo a scrivere `--- Tentativo numero 3` usando lo stesso *trucco*...

Cosa succede se scrivete un comando come questo?

```python
>>> frase = "--- Tentativo numero " + tentativi
```

Risponde `TypeError: Can't convert 'int' object to str implicitly` dove in pratica *Python* ci dice che non riesce
a trasformare un numero intero (`tentativi` è un numero intero) in un stringa.

Riassumiamo:

* `"Hai inserito il umero " + "42"` funziona
* `"--- Tentativo numero " + 42` **non** funziona

Bene ora provate a usare la funzione `str()` sulla console per scrivere
```python
>>> str(42)
'42'
>>> str(tentativi)
'20'
```

Quindi ora siamo in grado di scrivere sia la frase da scrivere prima di ogni tentativo che la frase finale
`BRAVO!!!! Hai indovinato in 3 tentativi.`. Solo un piccolo aiuto:

```python
>>> "Uniamo " + "3 " + "stringhe."
'Uniamo 3 stringhe.'
```

## Dove siamo adesso

Stiamo contando i tentativi e facciamo capire al giocatore che il tempo passa. Ecco il [programma](conteggi.py)

* Prossimo: [Indizi](indizi.md)
* Precedente: [Provare e riprovare](ciclo.md)
 