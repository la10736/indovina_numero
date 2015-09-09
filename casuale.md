# Numero a caso
Fino ad ora il numero da indovinare era fissa to e il gioco non era tanto divertente, ma in questa maniera potevamo 
provare facilmente se funzionava o meno quello che avevamo scritto. Ma ora è venuto il momento di farlo diventare un 
gioco e di non sapere qual'è il numero da indovinare.

## Il Computer sceglie il numero

Si ma come si fa? Si usano i potenti mezzi di *Python* importando nuove funzionalità usando `import`. In
inglese casuale si dice *random* e vediamo cosa succede a importare `random` sulla console

```python
>>> import random
```

Non succede niente! .... Questo è un buon segno!

Ora provate sempre sulla console questo comando

```python
>>> random.randint(0, 5000)
765
```

La funzione `randint(minimo, massimo)` ritorna un numero casuale tra minimo e massimo... ma non mi ricordo bene se 
`minimo` e `massimo` sono compresi, poco male **proviamo**!

```python
>>> random.randint(0, 1)
0
>>> random.randint(0, 1)
1
```

Questo significa che sono compresi.

Modificate ora il vostro programma per dare un numero casuale tra `0` e `2000` e dire al giocatore di inserire
un numero in questo intervallo e stampando una frase del tipo:

```
Inserisci un numero tra 0 e 2000:
```

## Dove siamo adesso

Ora si riesce a giocare e il gioco non è ne banale ne troppo difficile (Io ci sono riuscito in 12 tentativi). 
[Questo](casuale.py) è quello che è diventao.

* Prossimo: [BUG](bug.md)
* Precedente: [Indizi](indizi.md)
