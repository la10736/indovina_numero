# Indizi

Il nostro gioco è troppo difficile. Provate a giocare con il programma di un compagno che magari ha usato un altro 
numero: indovinare è *troppo difficile*.

Se il vostro programma deve rispondesse come mostrato sotto diventerebbe più semplice.

    --- Tentativo numero 1.
    Inserisci un numero: 1000
    Peccato non hai indovinato... prova ancora con un numero più alto.
    --- Tentativo numero 2.
    Inserisci un numero: 1500
    Peccato non hai indovinato... prova ancora con un numero più basso.
    --- Tentativo numero 3.
    Inserisci un numero: 1234
    BRAVO!!!! Hai indovinato in 3 tentativi.

## Cambiamo la frase a secnda del numero provato

Quando il giocatore non indovina vogliamo dirgli se mettere un numero più grande o più piccolo. Pensiamoci bene abbiamo 
bisogno di qualcosa che dica `True` se `numero_provato` è maggiore di `numero_da_indovinare` e `False` quando non è 
maggiore per usare `if` come abbiamo fatto per capire se il numero è quello giusto. 

* Idee? 
* Cosa potremmo usare?
* Sperimentiamo?


```python
>>> 5 > 6
False
>>> 6 > 5
True
>>> 5 < 6
True
```

Credo propio che ora ci possiamo riuscire.... 

## Dove siamo adesso

Il gioco si può giocare ma il numero è sempre lo stesso.... un po noioso. Scusate forse il vostro programma
non è proprio uguale a [questo](indizi.py) ma il bello è che le cose si possono fare in tanti modi diversi.

* Prossimo: [Numero a caso](casuale.md)
* Precedente: [Conteggi](conteggi.md)


