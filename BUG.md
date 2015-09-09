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

Mi sono arrabbiato un sacco dato che ero vicino alla fine!!!! 

## Verificare se il giocatore ha scritto il numero nell'intervallo proposto

Prima di correggere il vero *BUG* facciamo in maniera che se il giocatore non mette il numero nell'intervallo rifaciamo
la domanda senza aumentare i tentativi.

Avete qulche idea?

Vi suggerisco di provare sulla console

```python
>>> 0 <= 5 <= 2000
True
>>> 0 <= 3000 <= 2000
False
>>> 0 <= -1 <= 2000
False

Si ma noi vogliamo trovare una regola per restare in un ciclo fino a quando il numero non è utilizzabile; quindi deve
essere`True` fino a che il numero non è nell'intervallo e diventare `False` quando il numero è nell'intervallo: 
esattamente il contrario di quello che abbiamo scritto. Il *Pitone* fornisce la parola chiave `not` che significa il
contrario di quello che segue:

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

Quindi se mettiamo tutto questo in un ciclo.... 3 minuti....[un aiutino](indovina_verifica_intervallo.py)
 

## Capire se il giocatore ha scritto un numero o no

Adesso viene la parte difficile: *Come facciamo a capire che non è stato inserito un numero?*.

Una idea potrebbe essere quella di verificare se `tentativo` è una stringa vuota 

```python
>>> tentativo = ''
>>> tentativo == ''
True
>>> tentativo = '12'
>>> tentativo == ''
False
```

Ma cosa succede se uno per sbaglio scrive delle lettere?

```python
--- Tentativo numero 2.
Inserisci un numero tra 0 e 2000:ab
Traceback (most recent call last):
  File "/home/michele/PycharmProjects/base_python/indovina_verifica_intervallo.py", line 14, in <module>
    numero_provato = int(tentativo)
ValueError: invalid literal for int() with base 10: 'ab'
```

Questo significa che controllare se la stringa è vuota non basta.

```python
>>> tentativo = 'ab'
>>> tentativo == ''
False
```

Bene, il *Pitone* permette dei definire dei blocchi dove se avviene un errore ci si accorge e si può salvare la 
situazione:

```python
try:
    blocclo che può avere problemi
except:
    cosa fare se avviene un problema
```

A dire il vero si possono fare cose **molto** più complesse, ma per ora questo è uno strumento *molto potente che ci
permetterà di risolvere tanti problemi.*

Sperimentiamolo: quello che genera il problema è la riga `numero_provato = int(tentativo)`, per la verità il problema
è `int(tentativo)` quando tentativo non può essere trasformato in numero.

```python
>>> tenativo = 'ab'
>>> int(tentativo)
Traceback (most recent call last):
  File "/usr/lib/python3.4/code.py", line 90, in runcode
    exec(code, self.locals)
  File "<input>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'ab'
```

Proviamo quindi a *catturare* questo problema

```python
>>> try:
...     int(tentativo)
... except:
...     print(tentativo + " non sembra un numero")
... 
ab non sembra un numero
>>> tentativo = "12"
>>> try:
...     int(tentativo)
... except:
...     print(tentativo + " non sembra un numero")
... 
12
```

Bene allora abbiamo tutti gli strumenti.... 3 minuti, non uno di più! Ecco una possibile 
[soluzione](indovina_protetto.py)
