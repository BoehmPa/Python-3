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
Ein kurzer Überblick über die grundlegenden Datentypen. Im weiteren Verlauf werden diese genauer erklärt.
Zum Testen kann das Python-Terminal (in Powershell-Terminal den Befehl `python` eingeben) oder [diese Datei](Basics/Grunddatentypen/grunddatentypen.py) (enthält die vollständigen Befehle inklusive `print()`) genutzt werden.
<br>
<br>

- ### Ganze Zahlen (integer)

<br>

```py
> 9
> -9
> 1133
> 12
```
<br>

#### Rechenoperationen:

```py
> 9 + 9
>>> 18

> 17 - 4
>>> 13

> 16 / 8
>>> 2

> 5 * 12
>>> 60

> (21 - 3) * 9 + 6
>>> 168
```
<br>
<br>

- ### Gleitkommazahlen (float)

<br>

```py
> 0.5
> -123.456
> +0.4578930723894579275
```
<br>

#### Rechenoperationen

```py
> 1.3 + 1.8
>>> 3.1

> 12.9 - 7.4
>>> 5.5

> 1.5 / 2.1
>>> 0.712857142857143

> 123.748593 * 1.24
>>> 153.44825532
```
<br>
<br>

- ### Zeichenketten (strings)

<br>

```py
> "Hallo Welt"
>>> Hallo Welt

> 'Hallo Welt'
>>> Hallo Welt

> "Ich sage 'Hallo Welt!'"
>>> Ich sage 'Hallo Welt!'

> 'Ich sage "Hallo Welt!"'
>>> Ich sage "Hallo Welt!"
```
<br>

#### Operationen

```py
> "Hallo" + " " + "Welt"
>>> Hallo Welt
```
<br>
<br>

- ### Listen (list)
<br>

```py
> [1,2,3]
>>> [1, 2, 3]

> ["Python", 3, "ist super", "im Jahr", 2023]
>>> ['Python', 3, 'ist super', 'im Jahr', 2023]

> ["Hallo", 2, 3, -7 / 4, [1,2,3]]
>>> ['Hallo', 2, 3, -1.75, [1, 2, 3]]
```
<br>

#### Operationen

```py
> [1,2,3] + ["Python", "ist", "super!"]
>>> [1, 2, 3, 'Python', 'ist', 'super!']
```

<br>
<br>

- ### Wörterbuch (dictionary)
<br>

```py
> d = {"schlüssel1" : "wert1", "schlüssel2" : "wert2"}
```
<br>

#### Zugriff auf Werte

```py
> d["schlüssel1"]
>>> 'wert1'

> d["schlüssel2"]
>>> 'wert2'
```

<br>

#### Modifikation

```py
> d["schlüssel2"] = "wert2.1"
> d["schlüssel2"]
>>> 'wert2'

> d["schlüssel3"] = "wert3"
> d["schlüssel3"]
>>> 'wert3'
```

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