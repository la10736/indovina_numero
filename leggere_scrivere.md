# Leggere e Scrivere

Per prima cosa cancelliamo tutto quello che abbiamo scritto in `indovina_numero.py` e lo eseguiamo di nuovo per vedere
se è tutto a posto.

## Scrivere qualcosa

Per far sì che *Python* scriva quacosa si usa la funzione `print()` che vuol dire *`stampa`*: con *Python* si *parla
soprattutto inglese*. Tra le parentesi bisogna mettere una stringa (sequenza di caratteri) che può essere indicata sia 
con le virgolette `"` che con `'`. Noi per semplicità useremo sempre `"`. Quindi ora andiamo sulla console e facciamo 
stampare la prima stringa "la mia prima stringa".
 
Dopo averlo provato sulla console scriviamo nel programma ed eseguiamolo:
 
    /usr/bin/python3.4 /home/michele/PycharmProjects/indovina_numero/indovina_numero.py
    la mia prima stringa
    
    Process finished with exit code 0


Ancora una cosettina. Nella console provate a scrivere:

```python
frase="la mia prima stringa"
```

Cosa succede se dopo scrivete `frase` e premete a capo? 

Ora modificate il programma per funzionare come prima ma usando la riga

    print(frase)

## Chiedere qualcosa all'utente

In *Python* esiste la funzione `input()` che vuol dire *`inserisci`*. in pratica usando input chiedi al giocatore di
scrivere qualcosa. Puoi scegliere la frase che il giocatore vedrà sullo schermo prima di scrivere.
Per esempio se scrivi `input("inserisci il numero")` il giocatore vedrà:

    inserisci il numero

Provate ora sulla console a usare il comando `input` per chiedere `"come ti chiami?"` all'utente. Dopo cambiate
il programma affinché faccia due cose:
 
1. chieda all'utente come si chiama e
2. scriva sullo schermo:

    Ciao <il nome inserito dall'utente>, sto imparando a usare Python
    
**Un piccolo indizio**: provate sulla console a scrivere la seguente riga e osservate cosa succede

```python
>>> print("Ciao " + "pippo")
```

## Dove siamo adesso

Forse può sembrare che non abbiamo fatto granché, ma il nostro programma inizia a 
[prendere forma](leggere_scrivere.py)

* Prossimo: [Confrontare e decidere](confrontare.md)
* Precedente: [Primi Passi](iniziamo.md) 
