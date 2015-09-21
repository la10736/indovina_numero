# Provare e riprovare

Quello che vogliamo ottenere è far riprovare il giocatore a inserire numeri fino a quando indovina.

Per chi ha usato *Scratch* questo era un classico lavoro per il blocchetto **Per Sempre**. In *Python* esiste una cosa 
molto simile : `while True:`

## Per Sempre

Il ciclo `while` (letteralmente: fintanto che) si scrive così:

```python
while <condizione>:
    casa fare fintanto che
    condizione è vera
```

Quindi dato che `True` è sempre vero `while True` è proprio per sempre... almeno fino quando qualcuno non prova a 
interrompere il programma.

Provate quindi a sulla console a farvi stampare all'infinito una frase e poi trasformate il vostro programma in un 
ciclo continuo. Quando vorrete interrompere la console potete usare la combinazione di tasti `Ctrl-C`, mentre per
interrompere il programma usate il quadretto rosso (se lo usate con la console poi dovete farla ripartire).

## Interrompere Il programma quando il nummero viene indovinato

Potremmo usare la condizione del `while` e farla diventare `False` quando qualcuno indovina, ma forse il programma
è più semplice se impariamo a interromperlo quando indoviniamo.

Ora vi fornisco la formula magica per uscire dal programma in ogni punto:

```python
import sys
sys.exit()
```

## Dove siamo adesso

Ora assomiglia a un gioco! Se indovini ti dice che hai indovinato e quando indovini il gioco finisce. Dovrebbe
assomigliare a [questo](ciclo.py)

* Prossimo: [Conteggi](conteggi.md)
* Precedente: [Confrontare e decidere](confrontare.md)