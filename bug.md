# BUG: Se l'utente non mette un numero il programma deve funzionare e non terminare con errore

Alla mia prima partita dopo quasi una decina di tentativi ho premuto per sbaglio a capo e questo è quello che è 
successo:

```
--- Tentativo numero 7.
Inserisci un numero tra 0 e 2000:1796
Peccato non hai indovinato... prova ancora con un numero più alto.
--- Tentativo numero 8.
Inserisci un numero tra 0 e 2000:
Traceback (most recent call last):
  File "/home/michele/PycharmProjects/base_python/indovina_casuale.py", line 12, in <module>
    numero_provato = int(tentativo)
ValueError: invalid literal for int() with base 10: ''
```

**Mi sono arrabbiato un sacco dato che ero vicino alla fine!!!!**

Anche il vostro programma ha lo stesso problema: se il giocatore preme a capo senza inserire un numero e scrive qualcosa
che non è un numero come `ciao`, il programma termina con errore.

Ma prima di affrontare questo problema facciamo un passo indietro risolviamo un'altro problema....

## Verificare se il giocatore ha scritto il numero nell'intervallo proposto

*Se il giocatore* **non** *mette il numero nell'intervallo che abbiamo deciso rifaciamo la domanda senza aumentare il 
numero dei tentativi.*

Avete qulche idea?

Vi suggerisco di provare sulla console

```python
>>> 0 <= 5 <= 2000
True
>>> 0 <= 3000 <= 2000
False
>>> 0 <= -1 <= 2000
False
```

Quindi siamo in grado di provare nel nostro programma se il numero è nell'intervallo: giusto per verificare facciamo
scrivere ogni volta che il numero è giusto la scritta `"Numero nell'intervallo"`, giusto per vedere se abbiamo capito.

Adesso noi vogliamo sapere quando il numero **non** è *buono* per dire al giocatore `"Numero non nell'intervallo"`. 
Sperimentiamo la parola `not` che significa *fai il contrario*:

```python
>>> not True
False
>>> not False
True
>>> not 0 <= 5 <= 2000
False
>>> not 0 <= -1 <= 2000
True
>>> not 0 <= 3000 <= 2000
True
```

Quindi cambiate il programma per far scrivere `"Numero non nell'intervallo"`tutte le volte 
che il numero è sbagliato. Il programma deve funzionare così:

    --- Tentativo numero 1.
    Inserisci un numero tra 0 e 2000:3000
    Numero non nell'intervallo
    Peccato non hai indovinato... prova ancora con un numero più basso.
    --- Tentativo numero 2.
    Inserisci un numero tra 0 e 2000:

Ma questo non basta perché i tentativi vanno avanti e noi non lo vogliamo e bisogna richiedere di nuovo un numero senza 
aumentare il numero dei tentativi. Quindi ora sapete tutto quello che serve per riuscire a farlo funzionare come
vogliamo, ma vi consiglio di provare anche questo sulla console:

```python
>>> n = 0
>>> while True:
...     n = n + 1
...     if n == 5 :
...         break
... 
>>> print(n)
5
```

Quindi riassumendo sappiamo:

* Capire se il numero è nell'intervallo
* Capire se il numero **non** è nell'intervallo
* Fare un ciclo che continua fino a che la condizione è `True`
* Interromepre un ciclo quando vogliamo

Bene, credo proprio che ora sapete come fare... ma ci sono tantissimi modi per fare le stesse cose. Il programma deve
funzionare così:

```
--- Tentativo numero 1.
Inserisci un numero tra 0 e 2000:3000
Inserisci un numero tra 0 e 2000:-10
Inserisci un numero tra 0 e 2000:1000
Peccato non hai indovinato... prova ancora con un numero più alto.
--- Tentativo numero 2.
Inserisci un numero tra 0 e 2000:
```

## Capire se il giocatore ha scritto un numero o no

Adesso possiamo concentrarci con il **BUG**: *Come facciamo a capire che non è stato inserito un numero?*.

Avete qualche idea? Sperimentatela sulla console.

Il vero problema è che non sappiamo con cosa confrontare per capire se non è un numero, Forse è meglio riguardare cosa
ci dice l'errore.
```
    numero_provato = int(tentativo)
ValueError: invalid literal for int() with base 10: ''
```

Qundo *Python* prova a usare la funzione `int()` con `tentativo` allora trova un errore. Ora vi chiedo di sperimentare
queste poche righe sulla console


```python
>>> int("ciao")
Traceback (most recent call last):
  File "/usr/lib/python3.4/code.py", line 90, in runcode
    exec(code, self.locals)
  File "<input>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'ciao'
>>> try:
...     int("ciao")
... except:
...     print("NON è un numero")
... 
NON è un numero
```

Quindi possiamo usare `try` `except` per catturare il problema e far fare al programma queste cose:

```python
--- Tentativo numero 1.
Inserisci un numero tra 0 e 2000:
Ma chi vuoi prendere in giro? '' non è un numero!
Inserisci un numero tra 0 e 2000:1000
Peccato non hai indovinato... prova ancora con un numero più alto.
--- Tentativo numero 2.
Inserisci un numero tra 0 e 2000:ciao
Ma chi vuoi prendere in giro? 'ciao' non è un numero!
Inserisci un numero tra 0 e 2000:3000
Inserisci un numero tra 0 e 2000:1500
Peccato non hai indovinato... prova ancora con un numero più basso.
--- Tentativo numero 3.
Inserisci un numero tra 0 e 2000:
```


## Dove siamo adesso

Ora il gioco funziona proprio come vogliamo e non ci sono [**BUG**](bug.py) (almeno crediamo)..... Ma abbiamo proprio 
finito?

* Prossimo: [Scriviamolo meglio](refact.md)
* Precedente: [Numero a caso](casuale.md)

