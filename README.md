# Python-3

Diese README dient dazu, mir alle unbekannten oder wichtigen Dinge über das Thema **Python 3** einfach zu notieren.

<br>
<br>

## Grundlagen
<br>

### Python in der Shell
```py
> python datei.py
```
Eine Beispiel-Datei befindet sich unter Grundlagen/ersteVersuche "**py_in_shell.py**"

<br>

### Kommentare
Ein Kommentar, welcher in der selben Zeile endet, wird folgendermaßen verfasst:
```py
# gibt einen Text aus
print("einen Text")
```
Will man einen Kommentar über mehrere Zeilen schreiben, dann verfasst man ihn so:
```py
""" dies ist ein Blockkommentar,
    welcher sich über mehrere Zeilen erstreckt."""
```
Genau genommen wird mit dieser Notation kein Kommentar, sondern ein mehrzeiliger String erzeugt

<br>

## Kontrollstrukturen

<br>


### f-strings
#### Erklärung:

Beispiel:
```py
print(f"ich habe {anzahl} Äpfel gegessen!")
```