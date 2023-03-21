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
- [Kontrollstrukturen](#kontrollstrukturen)
    - [Fallunterscheidungen](#fallunterscheidungen)
    - [Schleifen](#schleifen)
    - [Die pass-Anweisung](#die-pass-anweisung)
- [Dateien](#dateien)
    - [Datenströme](#datenströme)
    - [Daten aus Dateien lesen](#daten-aus-einer-datei-lesen)
    - [Daten in Dateien schreiben](#daten-in-dateien-schreiben)


  







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
  d["schlüssel2"]
>>> 'wert2'

> d["schlüssel3"] = "wert3"
  d["schlüssel3"]
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
  print(name)
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
  print(zahl)
>>> 0.5

> string = "Hallo Welt"
  print(string)
>>> Hallo Welt

> print(1.5 + zahl)
>>> 2

> addition = 4 + 7
  print(addition)
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

Python macht Programmierern genaue Vorgaben, wie der Quellcode strukturiert sein muss. Dies führt zu einem strukturiertem und übersichtlichen Code, was besonders für Programmierneulinge gut ist.
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

<a name="kontrollstrukturen"></a>

## Kontrollstrukturen

Unter einer _Kontrollstruktur_ versteht man ein Konstrukt zur Steuerung des Programmablaufs. In Python unterscheidet man zwei Arten von Kontrollstrukturen: **Schleifen** und **Fallunterscheidungen**. Kontrollstrukturen können beliebig ineinander verschachtelt werden. Die Einrückungstiefe wächst dabei kontinuierlich. 

<br>

<a name="fallunterscheidungen"></a>

### Fallunterscheidungen

Fallunterscheidungen verknüpfen einen Code-Block an eine Bedingung. Man unterscheidet zwei Arten von Fallunterscheidungen: `if`-Anweisungen und _bedingte Ausdrücke_

<br>

- #### Die if-Anweisung
Die einfachste Möglichkeit der Fallunterscheidung ist die `if`-Anweisung. Diese besteht aus einem Anweisungskopf, welcher eine Bedingung enthält, und aus einem Codeblock als Anweisungskörper. Dieser Codeblock wird nur ausgelöst, falls die Bedingung `TRUE` ist. Hierfür werden die logischen Ausdrücke (siehe Operatoren/Vergleiche) benutzt.
Eine Beispiel-Datei, mit einer kompletten `if`-Anweisung findest du [hier](Kontrollstrukturen/Fallunterscheidungen/if-Anweisungen.py). 

```py
> if Bedingung:
    Anweisung
```

<br>

#### Beispiel:

```py
> if x == 1:
    print("x hat den Wert von 1")
>>> x hat den Wert von 1

> if x < 1 or x > 5:
    print("x ist kleiner 1")
    print("oder größer 5)
```

<br>

Benötigt man mehrere Fallunterscheidungen, kann man nach einem `if` noch beliebig viele `elif` erfolgen.

```py
> if Bedingung:
        Anweisung
  
  elif Bedingung:
        Anweisung

  elif Bedingung
        Anweisung
```

<br>

Als letzte Möglichkeit kann man auch alle unbehandelten Fälle auf einma abfangen. Dazu kann eine `if`-Anweisung um einen `else`-Zweig erweitert werden. Dieser muss am Ende der `if`-Anweisung geschrieben werden.

```py
> if Bedingung:
        Anweisung
  
  elif Bedingung:
        Anweisung

  else Bedingung:
        Anweisung
```
Der `else`-Zweig wird nur ausgeführt, wenn keine der vorangegangen Bedingungen erfüllt wurde. Zu jeder `if`-Anweisung darf nur ein `else`-Zweig gehören.

<br>
<br>

- ### Bedingte Audrücke
_Bedingte Audrücke_ ähneln stark den `if`-Anweisungen, werden jedoch in eine einzige Zeile geschrieben. _Bedingte Audrücke_ enthalten `if` und `else`.
Eine Beispiel-Datei befindet sich [hier](Kontrollstrukturen/Fallunterscheidungen/bedingte-Ausdr%C3%BCcke.py).

```py
> zahl = (20 if x == 1 else 30)

```
Dies verkürzt zwar den Code, allerdings auf Kosten der Lesbarkeit und Überschaubarkeit.

<br>
<br>

<a name="Schleifen"></a>

### Schleifen
Schleifen ermöglichen es einen Codeblock, den Schleifenkörper, mehrfach hintereinander auszuführen, solange, bis eine bestimmte Bedingung erfüllt ist. In Python gibt es zwei Arten von Schleifen: die `while`-Schleife und die `for`-Schleife.

<br>

- ### While-Schleifen

Eine `while`-Schleife besteht asi einem Schleifenkopf, in welchem die Bedingung steht und einem Schleifenkörper, welcher den Codeblock enthält, welcher ausgeführt werden soll. Die `while`-Schleife läuft _solange_ eine Bedingung erfüllt ist und nicht _bis_ diese erfüllt ist. Eine Datei mit Beispielen findest du [hier](Kontrollstrukturen/Schleifen/while-Schleife.py)

```py
> while Bedingung:
    Anweisung
```  

<br>

#### Abbruch einer Schleife
Eine Schleife kann an einer bestimmten Stelle mit `break` abgebrochen werden. 

```py
> while Bedingung:
    Anweisung
    break
```

<br>

#### Abbruch eines Schleifendurchlaufs
Möchte man nur den akutellen Schleifendurchlauf abbrechen, kann dies mit `continue`erreicht werden.

```py
> while Bedingung
    Anweisung
    continue
```
Dabei wird nicht die gesamte Schleife abgebrochen, sondern lediglich der aktuelle Durchlauf.

<br>
<br>

- ### For-Schleifen
Die `for`-Schleife wird verwendet, um ein _iterierbares Objekt_ (z.B. Listen oder Strings) zu durchlaufen. Dafür folgt auf `for` ein Bezeichner, das Schlüsselwort `in` und der Name des iterierbaren Objektes. [Beispiel](Kontrollstrukturen/Schleifen/for-Schleife.py)

```py
> for element in Objekt:
    Anweisung
```

Auch bei der `for`-Schleife funktionieren die Schlüsselwörter `continue`und `break`zum Abbrechen der Schleife bzw. des Schleifendurchlaufs. Zusätzlich kann eine `for`-Schleife über einen `else`-Zweig verfügen, der dann ausgeführt wird, wenn die Schleife vollständig durchgelaufen ist und nicht über `break`vorzeitig abgebrochen wurde.

```py
> for element in Objekt:
    Anweisung
> else:
    Anweisung
```

Die `for`-Schleife kann auch als Zählerschleife benutzt werden. Dazu besitzt sie eine eingebaute `range`-Funktion, welche ein Objekt iterierbares Objekt erzeugt, welche alle ganze Zahlen eines bestimmten Bereiches durchläuft. Der erste Wert ist dabei der Startwert und inkludiert, der zweite Wert ist der Stopwert und ist exkludiert, der dritte Wert gibt die Schrittgröße an.

```py
> for element in range(start, stop, step)
    Anweisung
```

<br>
<br>

<a name="die-pass-anweisung"></a>

### Die pass-Anweisung
Während der Entwicklung kann es vorkommen, das eine Kontrollstruktur nur teilweise implementiert ist. So kann zum Beispiel nur ein Anweisungskopf erstellt worden sein, ohne Anweisungskörper, da sich um dringendere Teile des Programms gekümmert werden musste. Ein alleinstehender Anweisungskopf ist jedoch ein Syntaxfehler. Aus diesem Grund gibt es die `pass`-Anweisung. Diese hat den Zweck, Syntaxfehler in vorläufigen Programmversionen zu vermeiden. Ein fertiges Programm sollte keine `pass`-Anweisung enthalten. [Beispiel](Kontrollstrukturen/pass-Anweisung.py)

```py
> Bedingung:
    pass
  Bedingung:
    print(x)
```

<br>
<br>

<a name="Dateien"></a>

## Dateien
Hier geht es primär um das Lesen und Schreiben von Dateien, da dies zum Standardrepertoire eines Programmierers gehört. 

<br>

<a name="Datenströme"></a>

### Datenströme
Unter einem _Datenstrom_ (*data stream*) versteht man eine kontinuierliche Folge von Daten. Dabei werden zwei Typen unterschieden: _eingehende Datenströme_(*downstreams*) von denen Daten gelesen werden können und in _ausgehende Datenströme_ (*upstreams*) geschrieben werden können.
Tastatureingaben, Bildschirmausgaben, Dateien und auch Netzwerkverbindungen werden als Datenstrom betrachtet.
Sowohl die Eingabe eines Benutzers als auch die Ausgabe bspw. eines Strings auf dem Bildschirm sind nichts anderes als Operatrionen auf den Standardeingabe - bzw. -ausgabeströmen *stdin* und *stdout*. Auf den Ausgabestrom *stdout* kann mit der `print`-Funktion geschrieben werden und von dem Eingabestrom mitels der `input`-Funktion gelesen werden. 

<br>
<br>

<a name="daten-aus-einer-datei-lesen"></a>

### Daten aus einer Datei lesen
Sollen Daten aus einer Datei gelesen werden, muss zuerst lesend auf diese zugegriffen werden. Dafür existiert die [dateien-lesen.txt](Dateien/dateien-lesen.txt)-Datei.
Um die Datei zum Lesen zu öffnen, verwendet man die Funktion `open`. Diese gibt ein sogenanntes _Dateiobjekt_ (*file object*) zurück.

```py
> open("Dateipfad", "Modus")
```

In diesem Beispiel würde der Code folgendermaßen aussehen:

```py
> file_object = open("Dateien/dateien-lesen.txt","r")
```
Der Modus _"r"_ steht hierbei für read, sodass die Datei zum Lesen geöffnet wird. Nun können mit dem Datenobjekt Daten aus der Datei gelesen werden. Ist das Lesen der Datei beendet, muss sie explizit durch das Aufrufen der Methode `close` geschlossen werden.

```py
> file_object.close
```
Danach können keine weiteren Daten mehr aus dem Datenobjekt gelesen werden.

<br>

Sollen nun die Daten zeilenweise ausgelesen werden, ist dies relativ einfach, da das Datenobjekt zeilenweise iterierbar ist. 

```py
> file_object = open("Dateien/dateien-lesen.txt","r")
  for line in file_object:
    print(line)
  file_object.close
```

Für Test- & Verständniszwecke erweitern wir nun dieses Programm, sodass wir die Orte in einem _dictionary_ speichern, in welchem die englischen Namen die Schlüssel und die deutschen Namen deren Werte sind.

<br>

Dafür wird zuerst ein leeres dictionary angelegt.

```py
> laender{}
```

Als nächstes wird die dateien-lesen.txt-Datei geöffnet und in einer Schleife über alle Zeilen iteriert.

```py
> file_object = open("Dateien/dateien-lesen.py", "r")
  for line in file_object:
    zuordnung = line.split(" ")
    laender[zuordnung[0]] = zuordnung[1]
  file_object.close
```

Mit der Methode `split` um die aktuelle Zeile in zwei Teile aufzuteilen. Der Teil links des Leerzeichens (das englische Wort) und den Teil rechts vom Leerzeichen (das deutsche Wort). Als nächstes wird ein Eintrag ins dictionary angelegt, mit dem Schlüssel zuordnung[0] und dem Wert zuordnung[1].
In der Beispiel-Datei [dateien-lesen.py](Dateien/dateien-lesen.py) ist eine Erweiterung dieses Programmes zu finden.

<br>
<br>

<a name="daten-in-dateien-schreiben"></a>

### Daten in Dateien schreiben
