# Leggere e Scrivere

Per prima cosa cancelliamo tutto quello che abbiamo scritto in `indovina_numero.py` e lo eseguiamo di nuovo per vedere
se è tutto a posto.

## Scrivere qualcosa

Per far si che *Python* scriva quacosa si usa la funzione `print()` che vuol dire *`stampa`*: con *Python* si *parla
soprattutto inglese*. Tra le parentesi bisogna mettere una stringa (sequenza di caratteri) che può essere indicata sia 
con le virgolette `"` che con `'`. Noi per semplicità useremo sempre `"`. Quindi ora andiamo sulla console e facciamo 
stampare la prima stringa "la mia prima strigna".
 
Dopo averlo provato sulla console Scriviamo nel programma e eseguiamolo:
 
    /usr/bin/python3.4 /home/michele/PycharmProjects/indovina_numero/indovina_numero.py
    la mia prima stringa
    
    Process finished with exit code 0


Ancora una cosettina. Nella console provate a scrivere... cosa succede se dopo scrivete `frase` e premete a capo? 

```python
frase="la mia prima stringa"
```

Ora modificate il programma per funzionare come prima ma usando la riga

    print(frase)

## Chiedere qualcosa all'utente

In *Python* esiste la funzione `input()` che vuol dire *`inseriment`*. Alla funzione `input` bisogna passare la stringa 
il con mesaggio che si vuole madare prima all'utente prima che lui scrive e poi si aspetta che venga inserito qualcosa.

Provate ora sulla console a usare il comando `input` per chiedere a chi deve scrivere `"come ti chiami?"`. Dopo cambiate
il programma per chiede all'utente come si chiama e poi scrivere sullo scermo

    Ciao <il nome scritto>, sto imparando a usare Python
    
**Un piccolo indizio**: provate sulla console a scrivere la riga e osserbvate cosa succede

```python
>>> print("Ciao " + "pippo")
```

## Dove siamo adesso

Forse può sembrare che non abbiamo fatto un gran che, ma il nostro preogramma inizia a 
[prendere forma](leggere_scrivere.py)

Prossimo: [Confrontare e decidere](confrontare.md)
Precedente: [Primi Passi](iniziamo.md) 