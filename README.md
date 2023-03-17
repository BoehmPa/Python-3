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
    - [Operatoren](#operatoren)
    - [Ausgabe](#ausgabe)
    - [Kommentare](#ausgabe)
    - [Variablen](#variablen)
    - [Ausführen eines Python-Scripts in der Shell](#ausführen-eines-python-scripts-in-der-shell)
    - [Module](#module)
    - [Grundstruktur](#grundstruktur)
- [Kontrollstruktur](#kontrollstruktur)
  







<br>
<br>
<br>
<br>

<a name="einführung"></a>

## Einführung
Python ist eine Programmiersprache, welche Entwicklern sowohl das objekorientiere als auch das funktionale Programmieren ermöglicht. 

<br>

<a name="grundlegende-konzepte"></a>

### Grundlegende Konzepte
Python beeinhaltet einen Compiler und einen Interpreter mit einer großen Standardbibliothek.
Der Vorgang erfolgt folgendermaßen:

- Das Python-Programm wird ausgeführt
- Es passiert den Compiler, welcher den Code von der Sprache Python in den Byte-Code übersetzt.
- der Interpreter liest den Byte-Code und führt ihn aus.

<br>

<a name="Stärken"></a>

### Stärken

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

### Einsatzgebiete
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

<br>
<br>

<a name="operatoren"></a>

### Operatoren
Python bietet verschiedene Arten von Operatoren wie arithmetische und logische Operatoren

| arithmetische Operatoren| Zeichen                |
| --------------------    | ---------------------- |
| Addition                |           +            |
| Subtraktion             |           -            |
| Multiplikation          |           *            |
| Division                |           /            |


| Vergleich               |            Bedeutung   |
| ------------------------| ---------------------- |
| ==                      | ist gleich/das Selbe   |
| !=                      | ist ungleich           |
| <                       | ist kleiner            |
| >                       | ist größer             |
| <=                      | ist kleiner oder gleich|
| >=                      | ist größer oder gleich |

Diese Vergleiche können mit einander verknüpft werden, da diese nur **`TRUE`** oder **`FALSE`** ausgeben können. Dies erfolgt mit den Verknüpfungen _`and`_ oder _`or`_. 

<br>
<br>

<a name="ausgabe"></a>

### Ausgabe

in Python wird eine Ausgabe mit der `print()`-Funktion ausgeführt.

```py
> print(3)
```

Will man beispielsweise einen string Ausgeben, muss dieser in `""` gesetzt werden. Es können auch Variablen statt Werte verwendet werden.

```py
> print("String.")

> name = "Peter"
> print(name)
>>> Peter
```

Dafür kann ebenfalls die Datei ["grunddatentypen.py"](Basics/Grunddatentypen/grunddatentypen.py) eingesehen werden. 

<br>
<br>

<a name="kommentare"></a>

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

Genau genommen wird mit dieser Notation kein Kommentar, sondern ein mehrzeiliger String, erzeugt.

<br>
<br>

<a name="variablen"></a>

### Variablen
In Python können Werten einen Namen zugewiesen werden. Diese Art der Operation nennt man Zuweisung.
Diese Variablen können dann später abgerufen werden oder in Berechnung verwendet werden, indem anstelle des Werts, der Name der Variablen eingesetzt wird.
Zudem ist es auch möglich, Berechnungen Variablen zuzuweisen.

```py
> zahl = 0.5
> print(zahl)
>>> 0.5

> string = "Hallo Welt"
> print(string)
>>> Hallo Welt

> print(1.5 + zahl)
>>> 2

> addition = 4 + 7
> print(addition)
>>> 11
```
Bei der Bennennung der Variablen sollte man darauf achten, **nur Buchstaben des englischen Alphabets** zu wählen. Außerdem ist Python **_case sensitive_**.Heißt: man unterscheidet zwischen Groß- & Kleinschreibung. In der Praxis bedeutet das, dass die Variablen **`name`** und **`Name`** nicht identisch sind, sondern mit zwei unterschiedlichen Werten verknüpft sein können. 

<br>
<br>

<a name="ausführen-eines-python--scripts-in-der-shell"></a>

### Ausführen eines Python-Scripts in der Shell

Manchmal kann es vorkommen, dass man ein Python-Script nicht über eine IDE ausführen kann. Dann hat man noch die Möglichkeit, dieses Script über die Shell auszuführen.

```py
> python datei.py
```
Eine Beispiel-Datei befindet sich [hier](Basics/Ausführen/py_in_shell.py).

<br>
<br>

<a name="module"></a>

### Module

Python bietet eine enorme Menge von zur Verfügung stehenden **Modulen**, welche in ihrer Gesamtheit die _Standardbibliothek_ bilden.
Diese Module dienen oft als zweckdienliche Sammlung zusätzlicher Funktionalitäten. So existiert beispielsweise das Module _math_, welches dem Programmierer Funktionen und Konstanten für mathematische Berechnungen zur Verfügung stellt. 
Bevor ein Modul verwendet werden kann, muss es über das Schlüsselwort `import` eingebunden werden.

```py
> import math
```

<br>
<br>

<a name="grundstruktur"></a>

### Grundstruktur

Python macht Programmieren genaue Vorgaben, wie der Quellcode strukturiert sein muss. Dies führt zu einem strukturiertem und übersichtlichen Code, was besonders für Programmierneulinge gut ist.
Grundsätzlich besteht ein Python-Programm aus einzelnen _Anweisungen_, die entweder eine Zeile im Quelltext einnehmen. 

```py
> print("Hallo")
```

Einige Anweisungen lassen sich in einen Anweisungskopf und in einen Anweisungskörper unterteilen, wobei der Körper weitere Anweisungen enthalten kann.

```py
> Anweisungskopf:
    Anweisung
    .
    .
    .
    .
    Anweisung
>>>
```

<br>
<br>

<a name="kontrollstruktur"></a>

## Kontrollstruktur


<br>
