# Python-3

Diese README dient dazu, alle wichtigen Dinge über das Thema **Python 3** einfach zu notieren.

<br>
<br>

# Inhaltsverzeichnis
- [Eine Einführung in Python](#einführung)
    - [Grundlegende Konzepte](#grundlegende-konzepte) 
    - [Stärken](#stärken)
    - [Einsatzgebiete](#einsatzgebiete)
- [Die Basics](#basics) 
    - [Grundlegende Datentypen](#grundlegende-datentypen)
  









<a name="einführung"></a>

## Einführung
Python ist eine Programmiersprache, welche Entwicklern sowohl das objekorientiere als auch das funktionale Programmieren ermöglicht. 

<br>

<a name="grundlegende-konzepte"></a>

#### Grundlegende Konzepte
Python beeinhaltet einen Compiler und einen Interpreter mit einer großen Standardbibliothek.
Der Vorgang erfolgt folgendermaßen:

- Das Python-Programm wird ausgeführt
- Es passiert den Compiler, welcher den Code von der Sprache Python in den Byte-Code übersetzt.
- der Interpreter liest den Byte-Code und führt ihn aus.

<br>

<a name="Stärken"></a>

#### Stärken

- Python kann vielseitig eingesetzt werden:
    - kleine oder große Applikationen
    - serverseitige Programmiersprache
    - Skriptsprache
    - Python-Interpreter für Smartphone- & Tabletsysteme
- einfache Syntax
    - leicht zu lernen
    - leicht zu lesen
- große Standardbibliothek
- automatische Speicherverwaltung
- sehr gute Erweitbarkeit
 




<br>

<a name="einsatzgebiete"></a>

#### Einsatzgebiete
- Datenwissenschaften
    - Datenanalyse
    - Datenvisualisierung
- KI-Anwendungen
- maschinelles Lernen (durch Python-Bibliotheken)
- Deep Learning (durch Python-Bibliotheken)


<br>

<a name="basics"></a>

## Basics

<br>

<a name="grundlegende-datentypen"></a>

### Grundlegende Datentypen




### Python in der Shell
```py
> python datei.py
```
Eine Beispiel-Datei befindet sich unter Basics/Python in der Shell/"**py_in_shell.py**"

<br>

### Ausgabe
in Python wird eine Ausgabe mit dem `print`-Befehl ausgeführt.
```py
print(3)
```
Will man einen string Ausgeben, muss diese in `""`gesetzte werden.
```py
print("ich bin ein String.")
```

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
Genau genommen wird mit dieser Notation kein Kommentar, sondern ein mehrzeiliger String erzeugt.

<br>

### Python in der Shell
```py
> python datei.py
```
Eine Beispiel-Datei befindet sich [hier](Basics/Ausführen/py_in_shell.py)

<br>

## Kontrollstrukturen

<br>


### f-strings
#### Erklärung:

Beispiel:
```py
print(f"ich habe {anzahl} Äpfel gegessen!")
```