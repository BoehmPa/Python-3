# Python-3

Ein Repo rund um die Grundlagen zum Thema Python.

<br>
<br>

# Inhaltsverzeichnis
[Teil I: Die Basics](#teil-i-die-basics)
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
    - [Ein Dateiobjekt erzeugen](#ein-dateiobjekt-erzeugen)
  - [Das Laufzeitmodell](#das-laufzeitmodell)
    - [Die Struktur von Instanzen](#die-struktur-von-instanzen)
    - [Referenzen und Instanzen freigeben](#referenzen-und-instanzen-freigeben)
    - [Mutable vs. immutable Datentypen](#mutable-vs-immutable-datentypen)
  - [Funktionen, Methoden und Attribute](#funktionen-methoden-und-attribute)
    - [Parameter von Funktioen und Methoden](#parameter-von-funktionen-und-methoden)
    - [Attribute](#attribute)
  - [Informationsquellen zu Python](#informationsquellen-zu-python)

[Teil II: Datentypen](#teil-ii-datentypen)
  - [Basisdatentypen: Eine Übersicht](#basisdatentypen-eine-übersicht)
  - [Numerische Datentypen](#numerische-datentypen)
  - [Ganzzahl - int](#ganzzahlen---int)

  








<a name="teil-i:-die-basics"></a>

# Teil I: Die Basics

<a name="einführung"></a>

## Einführung
Python ist eine Programmiersprache, welche Entwicklern sowohl das objekorientiere als auch das funktionale Programmieren ermöglicht. 


<a name="grundlegende-konzepte"></a>

### Grundlegende Konzepte
Python beeinhaltet einen Compiler und einen Interpreter mit einer großen Standardbibliothek.
Der Vorgang erfolgt folgendermaßen:

- Das Python-Programm wird ausgeführt
- Es passiert den Compiler, welcher den Code von der Sprache Python in den Byte-Code übersetzt.
- der Interpreter liest den Byte-Code und führt ihn aus.


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
 

<a name="einsatzgebiete"></a>

### Einsatzgebiete
- Datenwissenschaften
    - Datenanalyse
    - Datenvisualisierung
- KI-Anwendungen
- maschinelles Lernen (durch Python-Bibliotheken)
- Deep Learning (durch Python-Bibliotheken)


<a name="basics"></a>

## Basics

<a name="grundlegende-datentypen"></a>

### Grundlegende Datentypen

Ein kurzer Überblick über die grundlegenden Datentypen. Im weiteren Verlauf werden diese genauer erklärt.
Zum Testen kann das Python-Terminal (in Powershell-Terminal den Befehl `python` eingeben) oder [diese Datei](Basics/Grunddatentypen/grunddatentypen.py) (enthält die vollständigen Befehle inklusive `print()`) genutzt werden.


- ### Ganze Zahlen (integer)


```py
> 9
> -9
> 1133
> 12
```


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

- ### Gleitkommazahlen (float)



```py
> 0.5
> -123.456
> +0.4578930723894579275
```


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


- ### Zeichenketten (strings)


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


#### Operationen

```py
> "Hallo" + " " + "Welt"
>>> Hallo Welt
```


- ### Listen (list)


```py
> [1,2,3]
>>> [1, 2, 3]

> ["Python", 3, "ist super", "im Jahr", 2023]
>>> ['Python', 3, 'ist super', 'im Jahr', 2023]

> ["Hallo", 2, 3, -7 / 4, [1,2,3]]
>>> ['Hallo', 2, 3, -1.75, [1, 2, 3]]
```


#### Operationen

```py
> [1,2,3] + ["Python", "ist", "super!"]
>>> [1, 2, 3, 'Python', 'ist', 'super!']
```


- ### Wörterbuch (dictionary)

```py
> d = {"schlüssel1" : "wert1", "schlüssel2" : "wert2"}
```


#### Zugriff auf Werte

```py
> d["schlüssel1"]
>>> 'wert1'

> d["schlüssel2"]
>>> 'wert2'
```


#### Modifikation

```py
> d["schlüssel2"] = "wert2.1"
  d["schlüssel2"]
>>> 'wert2'

> d["schlüssel3"] = "wert3"
  d["schlüssel3"]
>>> 'wert3'
```


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


<a name="ausführen-eines-python--scripts-in-der-shell"></a>

### Ausführen eines Python-Scripts in der Shell

Manchmal kann es vorkommen, dass man ein Python-Script nicht über eine IDE ausführen kann. Dann hat man noch die Möglichkeit, dieses Script über die Shell auszuführen.

```py
> python datei.py
```
Eine Beispiel-Datei befindet sich [hier](Basics/Ausführen/py_in_shell.py).


<a name="module"></a>

### Module

Python bietet eine enorme Menge von zur Verfügung stehenden **Modulen**, welche in ihrer Gesamtheit die _Standardbibliothek_ bilden.
Diese Module dienen oft als zweckdienliche Sammlung zusätzlicher Funktionalitäten. So existiert beispielsweise das Module _math_, welches dem Programmierer Funktionen und Konstanten für mathematische Berechnungen zur Verfügung stellt. 
Bevor ein Modul verwendet werden kann, muss es über das Schlüsselwort `import` eingebunden werden.

```py
> import math
```

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

<a name="kontrollstrukturen"></a>

## Kontrollstrukturen

Unter einer _Kontrollstruktur_ versteht man ein Konstrukt zur Steuerung des Programmablaufs. In Python unterscheidet man zwei Arten von Kontrollstrukturen: **Schleifen** und **Fallunterscheidungen**. Kontrollstrukturen können beliebig ineinander verschachtelt werden. Die Einrückungstiefe wächst dabei kontinuierlich. 


<a name="fallunterscheidungen"></a>

### Fallunterscheidungen

Fallunterscheidungen verknüpfen einen Code-Block an eine Bedingung. Man unterscheidet zwei Arten von Fallunterscheidungen: `if`-Anweisungen und _bedingte Ausdrücke_


- #### Die if-Anweisung
Die einfachste Möglichkeit der Fallunterscheidung ist die `if`-Anweisung. Diese besteht aus einem Anweisungskopf, welcher eine Bedingung enthält, und aus einem Codeblock als Anweisungskörper. Dieser Codeblock wird nur ausgelöst, falls die Bedingung `TRUE` ist. Hierfür werden die logischen Ausdrücke (siehe Operatoren/Vergleiche) benutzt.
Eine Beispiel-Datei, mit einer kompletten `if`-Anweisung findest du [hier](Kontrollstrukturen/Fallunterscheidungen/if-Anweisungen.py). 

```py
> if Bedingung:
    Anweisung
```


#### Beispiel:

```py
> if x == 1:
    print("x hat den Wert von 1")
>>> x hat den Wert von 1

> if x < 1 or x > 5:
    print("x ist kleiner 1")
    print("oder größer 5)
```


Benötigt man mehrere Fallunterscheidungen, kann man nach einem `if` noch beliebig viele `elif` erfolgen.

```py
> if Bedingung:
        Anweisung
  
  elif Bedingung:
        Anweisung

  elif Bedingung
        Anweisung
```


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

- ### Bedingte Audrücke
_Bedingte Audrücke_ ähneln stark den `if`-Anweisungen, werden jedoch in eine einzige Zeile geschrieben. _Bedingte Audrücke_ enthalten `if` und `else`.
Eine Beispiel-Datei befindet sich [hier](Kontrollstrukturen/Fallunterscheidungen/bedingte-Ausdr%C3%BCcke.py).

```py
> zahl = (20 if x == 1 else 30)

```
Dies verkürzt zwar den Code, allerdings auf Kosten der Lesbarkeit und Überschaubarkeit.


<a name="Schleifen"></a>

### Schleifen
Schleifen ermöglichen es einen Codeblock, den Schleifenkörper, mehrfach hintereinander auszuführen, solange, bis eine bestimmte Bedingung erfüllt ist. In Python gibt es zwei Arten von Schleifen: die `while`-Schleife und die `for`-Schleife.


- ### While-Schleifen

Eine `while`-Schleife besteht aus einem Schleifenkopf, in welchem die Bedingung steht und einem Schleifenkörper, welcher den Codeblock enthält, welcher ausgeführt werden soll. Die `while`-Schleife läuft _solange_ eine Bedingung erfüllt ist und nicht _bis_ diese erfüllt ist. Eine Datei mit Beispielen findest du [hier](Kontrollstrukturen/Schleifen/while-Schleife.py)

```py
> while Bedingung:
    Anweisung
```  


#### Abbruch einer Schleife
Eine Schleife kann an einer bestimmten Stelle mit `break` abgebrochen werden. 

```py
> while Bedingung:
    Anweisung
    break
```


#### Abbruch eines Schleifendurchlaufs
Möchte man nur den akutellen Schleifendurchlauf abbrechen, kann dies mit `continue`erreicht werden.

```py
> while Bedingung
    Anweisung
    continue
```
Dabei wird nicht die gesamte Schleife abgebrochen, sondern lediglich der aktuelle Durchlauf.

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


<a name="die-pass-anweisung"></a>

### Die pass-Anweisung
Während der Entwicklung kann es vorkommen, das eine Kontrollstruktur nur teilweise implementiert ist. So kann zum Beispiel nur ein Anweisungskopf erstellt worden sein, ohne Anweisungskörper, da sich um dringendere Teile des Programms gekümmert werden musste. Ein alleinstehender Anweisungskopf ist jedoch ein Syntaxfehler. Aus diesem Grund gibt es die `pass`-Anweisung. Diese hat den Zweck, Syntaxfehler in vorläufigen Programmversionen zu vermeiden. Ein fertiges Programm sollte keine `pass`-Anweisung enthalten. [Beispiel](Kontrollstrukturen/pass-Anweisung.py)

```py
> Bedingung:
    pass
  Bedingung:
    print(x)
```


<a name="Dateien"></a>

## Dateien
Hier geht es primär um das Lesen und Schreiben von Dateien, da dies zum Standardrepertoire eines Programmierers gehört. 


<a name="Datenströme"></a>

### Datenströme
Unter einem _Datenstrom_ (*data stream*) versteht man eine kontinuierliche Folge von Daten. Dabei werden zwei Typen unterschieden: _eingehende Datenströme_(*downstreams*) von denen Daten gelesen werden können und in _ausgehende Datenströme_ (*upstreams*) geschrieben werden können.
Tastatureingaben, Bildschirmausgaben, Dateien und auch Netzwerkverbindungen werden als Datenstrom betrachtet.
Sowohl die Eingabe eines Benutzers als auch die Ausgabe bspw. eines Strings auf dem Bildschirm sind nichts anderes als Operatrionen auf den Standardeingabe - bzw. -ausgabeströmen *stdin* und *stdout*. Auf den Ausgabestrom *stdout* kann mit der `print`-Funktion geschrieben werden und von dem Eingabestrom mitels der `input`-Funktion gelesen werden. 


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


Sollen nun die Daten zeilenweise ausgelesen werden, ist dies relativ einfach, da das Datenobjekt zeilenweise iterierbar ist. 

```py
> file_object = open("Dateien/dateien-lesen.txt","r")
  for line in file_object:
    print(line)
  file_object.close
```

Für Test- & Verständniszwecke erweitern wir nun dieses Programm, sodass wir die Orte in einem _dictionary_ speichern, in welchem die englischen Namen die Schlüssel und die deutschen Namen deren Werte sind.


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

Mit der Methode `split` wird die aktuelle Zeile in zwei Teile aufgeteilt. Der Teil links des Leerzeichens (das englische Wort) und den Teil rechts vom Leerzeichen (das deutsche Wort). Als nächstes wird ein Eintrag ins dictionary angelegt, mit dem Schlüssel zuordnung[0] und dem Wert zuordnung[1].
In der Beispiel-Datei [dateien-lesen.py](Dateien/dateien-lesen.py) ist eine Erweiterung dieses Programmes zu finden.


<a name="daten-in-dateien-schreiben"></a>

### Daten in Dateien schreiben

Will man Daten in eine Datei schreiben, funktioniert das ähnlich wie das Lesen einer Datei. Hierzu muss statt dem Parameter `r`der Parameter `w`angegeben werden. Sollte die gewünschte Datei bereits vorhanden sein, wird diese geleert, falls nicht wird sie erstellt. 

```py
> fobj = open("dateien-schreiben.py", "w")
```
Sind alle Daten geschrieben, wird das Dateiobjekt wieder geschlossen.
```py
> fobj = close
```
Dazu befindet sich eine Beispiel-Datei, mit einem kleinen Beispiel [hier](Dateien/dateien-schreiben.py).

<a name="ein-dateiobjekt-erzeugen"></a>

### Ein Dateiobjekt erzeugen
Einem Dateiobjekt kann über die Built-in Function `open` neben dem Namen und dem Modus noch weitere Parameter übergeben werden. Außerdem gibt es neben den beiden Modi `r` und `w` einige weitere, welche durchaus nützlich sein können.

 - ### Die Built-in Function "`open`"
 Diese Funktion öffnet eine Datei und gibt das erzeugte Dateiobjekt zurück. Mithilfe dieses Datenobjektes können nachher die geünschten Operationen durchgeführt werden. 
 Der Standard-Befehl sieht so aus:
 ```py
 > open(filename, [mode,buffering,encoding,errors,newline])
 ```
 Die ersten beiden Parameter wurden bereits Besprochen. Dabei handelt es sich um den Dateinamen/den Dateipfad und um den Modus, in dem die Datei zu öffnen ist. Für den Parameter `mode` muss ein String angegeben werden. Dazu sind alle gültigen Werte in folgender Tabelle aufgelistet:

| Modus    | Beschreibung | 
| -------- | -------- | 
| `r`      | Die Datei wird ausschließlich zum Lesen geöffnet   | 
| `w`   | Die Datei wird ausschließlich zum Schreiben geöffnet, eine eventuell bestehende Datei gleichen Namens wird überschrieben    | 
| `a`   | Die Datei wird ausschließlich zum Schreiben geöffnet, eine eventuell bestehende Datei gleichen Namens wird nicht überschrieben sondern erweitert   | 
| `x`   | Die Datei wird ausschließlich zum Schreiben geöffnet, sofern diese nicht bereits existiert. Wenn eine Datei gleichen Namens vorhanden ist, wird eine _FileExistsError_-Exception geworfen  | 
| `r+`, `w+`, `a+`, `x+`   | Die Datei wird zum Lesen und Schreiben geöffnet   | 
| `rb`, `wb`, `ab`, `xb`, `r+b`, `w+b` ,`a+b`, `x+b`   | Die Datei wird im Binärmodus geöffnet. In diesem Fall müssen bytes-Instanzen anstelle von Strings verwendet werden   | 

Der Parameter _mode_ ist optional und wird als `r`angenommen, sollte er weggelassen werden.
Auf die zusätzlichen optinalen Parameter _buffering_, _encoding_, _errors_ und _newline_ wird später genauer eingegangen. 
Für das Verständnis ist hier eine kleine Zusammenfassung:
- _buffering_: steuert die interne Puffergröße
- _encoding_: legt ds Encoding fest, in dem die Datei gelesen/geschrieben werden soll. Es legt fest, wie Sonderzeichen, die über den **ASCII-Zeichensatz** hinausgehen, abgespeichert werden sollen.
- _errors_: bestimmt, wie mit Fehlern bei der Codierungvon Zeichen im angegebenen Encoding umgegangen werden soll. Wird für _errors_ der Wert _ignore_ übergeben, werden sie ignoriert, bei _strict_ wird eine _ValueError_-Exception geworfen, was auch passiert, sollte der Parameter nicht gesetzt sein.
- _newline_: legt die Zeichen fest, welche beim Schreiben oder Lesen der Datei als Newline-Zeichen erkannz/verwendet werden sollen.

- ### Attribute und Methoden eines Datenobjektes
Die folgende Tabelle gibt eine grobe Übersicht über die wichtigsten Methoden eines Dateiobjekts.

| Methode  | Beschreibung |
|----------|----------|
| `close()`| Schließt ein Dateiobjekt   |
| `fileno()`    | Gibt den Deskriptor der geöffneten Datei als ganze Zahl zurück|
| `flush()`    | Verfügt, dass anstehende Schreiboperationen sofort ausgeführt werden   |
| `isatty()` | _True_, wenn das Dateiobjekt auf einem Datenstrom geöffnet wurde, der nicht an beliebiger Stellegeschrieben oder gelesen werden kann  |
| `next()`| Liest die nächste Zeile der Datei ein und gibt sie als String zurück   |
| `read([size])` | Liest _size_ Bytes der Datei ein oder weniger, wenn vorher das Ende der Datei erreicht wurde. Sollte _size_ nicht angegeben sein, wird die Datei vollständig gelesen. Die Daten werden abhängig vom Lesemodus als String oder _bytes_-String zurückgegeben   |
| `readline([size])`    | Liest eine Zeile der Datei ein, Durch Angabe von _size_ lässt sich die Anzahl der zu lesenden Bytes begrenzen  |
| `readline([sizehint])`    | Liest alle Zeilen und gibt sie in Form einer Liste von Strings zurück. Sillte _sizehint_ angegeben sein, wird nur gelesen, bis ungefähr _sizehint_ Bystes gelesen wurden  |
| `seek(offset, [whence])`   | Setzt die aktuelle Schreib-/Leseposition in der Datei auf _offset_   |
| `tell()`    | Liefert die aktuelle Schreib-/Leseposition in der Datei   |
|`truncate([size])`    | Löscht in der Datei alle Daten, die hinter der aktuellen Schreib-/Lesepostion stehen, bzw. - sofern angegeben- alles außer den ersten _size_ Bytes   |
| `write(str)`    | Schreibt den String in _str_ in die Datei  |
| `writelines(iterable)`   | Schreibt mehrere Zeilen in die Datei. Das iterierbare Objekt _iterable_ muss Strings durchlaufen, möglich ist zum Beispiel eine Liste von Strings   |

<a name="das-Laufzeitmodell"></a>

## Das Laufzeitmodell
In diesem Abschnitt wird sich damit beschäftigt, wie Python Variablen zur Laufzeit verwaltet und welche Besonderheiten sich dabei für die Programmierung ergeben.
<br>
Variablen sind Platzhalter für Werte wie Zahlen, Listen oder sonstige Strukturen. Für die Programmierung ist der Begriff _Speicherstelle_ eher zutreffend, da hier Variablen vor allem den Zweck erfüllen, Daten für ihre Weiterverwendung zwischenzuspeicher. Um zu verstehen, was intern passiert, wenn eine neue Variable erzeugt wird, müssen zwei Begriffe voneinander Unterschieden werden: _Instanz_ und _Referenz_. Eine Instanz ist ein konkretes Dateiobjekt im Speicher, das nach der Vorlage eines bestimmten Datentyps erzeugt wurde - zum Beispiel die Zahl 132 nach der Vorlage des Datentyp Integer.
Am einfachsten lässt sich eine Instanz einer Ganzzahl beispielsweise so erzeugen:
```py
> 1234
>> 1234
```
Für die Programmierung ist diese Instanz aber wenig praktisch, da sie zwar nach der Erzeugung ausgegeben wird, danach aber nicht mehr zugänglich ist und somit ihr Wert nicht weiterverwendet werden kann. Weshalb nun Referenzen eine Rolle spielen. "Referenz" bedeutet so viel wie "Verweis". Erst durch Referenzen wird es möglich, mit Instanzen zu arbeiten, weil Referenzen den Zugriff auf diese ermöglichen. Die einfachste Form einer Referenz in `Python` ist ein _symbolischer Name_- wie beispielsweise _a_. Mit dem Zuweisungsoperator _=_fwird eine Referenz auf eine Instanz erzeugt. Dabei steht die Referenz links und die Instanz rechts vom Operator.

```py
> a = 1234
``` 
Es ist auch möglich, bereits referenzierte Instanzen mit weriteren Referenzen zu versehen:

```py
> referenz1 = 3456
> referenz2 = referenz1
```
Besonders wichtig hierbei ist, dass es nach wie vor nur eine Instanz mit dem Wert _3456_ im Speicher gibt. Die Instanz wird also nicht kopiert, sondern nur ein weiteres mal _referenziert_. Ebenso wichtig zu beachten ist, dass Referenzen auf dieselbe Instanz voneinander unabhängig sind und sich der Wert, auf den die anderen Referenzen verweisen, nicht ändert, wenn wir einer von ihnen eine neue Instanz zuweisen.

```py
> referenz1 = 3456
> referenz2 = referenz1
> print(referenz1)
>> 3456
> print(referenz2)
>> 3456
> referenz1 = 1234
> print(referenz1)
>> 1234
> print(referenz2)
>> 3456
```

<a name="die-struktur-von-instanzen"></a>

### Die Struktur von Instanzen
Jede Instanz in Python umfasst drei Merkmale: ihren _Datentyp_, ihren _Wert_ und ihre _Identität_. 
Als Beispiel könnte man sagen die Referenz _referenz1_ referenziert auf ein Instanz mit der Identiät 1234567, vom Dateityp int und dem Wert 1234.

- #### Datentyp
Der Datentyp dient bei der Erzeugung der Instanz als Bauplan und legt fest, welche Werte die Instanz annehmen darf. So erlaubt der Datentyp _int_ das Speichern einer ganzen Zahl. Strings lassen sich mit dem Datentyp _str_ verwalten. Die Datentypen können herausgefunden werden:
```py
> type(1337)
>> <class 'int' >
> type("Hallo Welt")
>> <class 'str'>
> v1 = 2674
> type(v1)
>> <class 'int'>
> type(v1) == type(2674)
>> True
> type(v1) == int
>> True
> type(v1) == str
>> False
```
Dabei sollte aber beachtet werden, dass sich ein Typ nur auf Instanzen bezieht, und nichts mit den verknüpften Referenzen zu tun hat. Eine Referenz hat keinen Typ und kann Instanzen beliebiger Typen referenzieren. Eine Referenz referenziert also auf eine Instanz mit einem bestimmten Datentyp.

- ### Wert
Was den Wert einer Instanz konkret ausmacht, hängt von ihrem Typ ab. Dies können Zahlen, Zeichenketten oder Daten anderer Typen sein. Diese können mit dem Operator _==_ bezüglich ihres Wertes verglichen werden. Dies ist jedoch nur sinnvoll, wenn es sich auf strukturell ähnliche Datentypen bezieht - etwas Gleitkommazahlen und Ganzzahlen.

- ### Identität
Die Identität einer Instanz dient dazu, diese von allen anderen Instanzen zu unterscheiden. Sie ist mit dem individuellen Fingerabdruck eines Menschen zu vergleichen, da sie für jede Instanz programmweit eindeutig ist und sich nicht ändern kann. Eine Identität ist eine Ganzzahl und lässt sich mithilfe der Funktion _id_ ermitteln:

```py
> id(variable)
> id(instanz)
```
Identitäten werden immer dann wichtig, wenn man prüfen möchte, ob es sich um eine ganz bestimmte Instanz handelt und nicht nur um eine mit dem selben Wert und dem gleichen Typ.
Diese können auch mit dem Operator _==_ verglichen werden.

```py
> id(referenz1) == id(referenz2)
>> True/False
```

<a name="referenzen-und-instanzen-freigeben"></a>

### Referenzen und Instanzen freigeben
Während eines Programmablaufs werden in der Regel sehr viele Instanzen angelegt, die aber nicht alle die ganze Zeit benötigt werden. Deshalb wäre es wünschenswert, wenn es eine Möglichkeit gäbe, nicht mehr benötigte Instanzen auf Anfrage zu entfernen. Python lässt den Programmierer den Speicher nicht direkt verwalten, sondern übernimmt dies für ihn. Instanzen, auf die keine Referenzen mehr verweisen, werden von Python als nicht mehr benötigt eingestuft und dementsprechend wieder freigegeben. Will man also eine Instanz entfernen, muss die dazugehörige Referenz gelöscht werden. Dafür gibt es die _del_-Anweisung. Nach ihrer Freigabe existiert die Referenz nicht mehr, ein Versuch auf diese zuzugreifen führt zu einem _NameError_.

```py
> v1 = 1337
> del v1
> v1
>> Traceback (most recent call last): File "<stdin>", line 1, in <module> NameError: name 'v1' is not definded
> del v1, v2, v3
```
Um zu erkennen, wann für eine Instanz keine Referenzen mehr existieren, speichert Python intern für jede Instanz einen Zähler, den sogenannten _Referenzzähler_ auch _reference count_. Für frisch erzeugte Instanzen hat er den Wert Null. Immer wenn eine neue Referenz auf eine Instanz erzeugt wird, erhöht sich der Referenzzähler der Instanz um eins, und immer wenn eine Referenz freigegeben wird, wurd er um eins verringert. Damit gibt der Referenzzähler einer Instanz stets die aktuelle Anzahl von Referenzen an, die auf die Instanz verweisen. Erreicht der Zähler den Wert Null, gibt es für die Instanz keine Referenzen mehr. Da Instanzen für Programmierer nur über Referenzen zugänglich sind, ist der Zugriff auf eine solche Instanz nicht mehr möglich - sie kann gelöscht werden.

<a name="mutable-vs.-immutable-datentypen"></a>

### Mutable vs. immutable Datentypen
Python unterscheidet grundlegend zwei Arten von Datentypen: _mutablen_ Datentypen und _immutablen_ Datentypen. Der Unterschied besteht darin, ob sich der Wert der Instanz zur Laufzeit ändern kann, ob sie also veränderbar ist. Instanzen eines mutablen Typs sind dazu in der Lage, nach ihrer Erzeugung andere Werte anzunehmen, während das bei immutablen Datentypen nicht der Fall ist. Wenn sich der Wert einer Instanz aber nicht ändern kann, ergibt es auch keinen Sinn, mehrere immutable Instanzen des gleichen Wertes im Speicher zu verwalten, weil im Optimalfall genau eine Instanz ausreicht, auf die dann die entsprechenden Referenzen verweisen. 

- ### Mutable Datentypen und Seiteneffekte
Bei den mutablen, also den veränderlichen Datentypen sieht es anders aus: weil Python damit rechnen muss, dass sich der Wert einer solchen Instanz nachträglich ändern wird, ist das oben erläuterte System, nach Möglichkeit bereits vorhandene Instanzen erneut zu referenzieren, nicht sinnvoll. Hier kann man sich also darauf verlassen, dass immer eine neue Instanz erzeugt wird. Dieses unterschiedliche Verhalten beim Umgang mit mutablen und immutablen Datentypen führt dazu, dass der gleiche Code für verschiedene Datentypen fundamental anderes bewirken kann. 

```py
> a = "Wasser"
> a += "flasche"
> print(a)
>> Wasserflasche
```

Aber:
```py
> a = "Wasser"
> b = a
> a += "flasche"
> print(a)
>> Wasserflasche
> print(b)
>> Wasser
```
Dies liegt daran, dass ein String ein immutabler Datentyp ist.
Eine Liste ist ein mutabler Datentyp, weshalb bei ihr folgendes Funktioniert:
```py
> a = [1,2]
> b = a
> a += [3, 4]
> print(a)
>> [1,2,3,4]
> print(b)
>> [1,2,3,4]
```

<a name="funktionen,-methoden-und-attribute"></a>

## Funktionen, Methoden und Attribute
Dies ist erneut nur ein grober Einblick in die Thematik. Im späteren Verlauf wird genauer auf die einzelnen Themen eingegangen.

<a name="parameter-von-funktionen-und-methoden"></a>

### Parameter von Funktionen und Methoden
Bei einer _Funktion_ handelt es sich um ein benanntes Unterprogramm, das eine häufig benötigte Funktionalität beinhaltet und über einen _Funktionsaufruf_ ausgeführt werden kann. Ein Beispiel einer solchen Funktion ist die eingebaute Funktion (auch Built-in Function) `max` zur Bestimmung des größten Elements einer Liste:
```py
> max([3,6,2,1,9])
>> 9
```
Dabei ist die Liste, deren größtes Element bestimmt werden soll, ein Parameter fer Funktion `max` und wird beim Funktionsaufruf deshalb in die Klammern geschrieben.
Wenn ein Funktionsaufruf ein Ergebnis zurückliefert, kann dieser Rückgabewert als Instanz weiterverwendet werden:
```py
> wert = max([3,6,2,4,9])
> wert/2
>>> 4,5
```
Eine Methode ist eine Funktion, die im Kontext einer bestimmten Instanz ausgeführt wird. Listen verfüge beispielsweise über eine Methode `sort`, die die Liste, für diesie aufgerufen wird, sortiert.
```py
> liste = [4,6,2,1,8,5,9]
> liste.sort
> liste
>>> [1,2,4,5,6,8,9]
```
Welche Methoden für eine Instanz verfügbar sind, hängt von ihrem Datentyp ab. 

- ### Positionsbezogene Parameter
Viele Methoden, und Funktionen, benötigen beim Aufruf neben der Instanz, auf die sich der Aufruf bezieht, weitere Informationen, um zu funktionieren. Dafür gibt es sogenannte _Parameter_, die, durch Kommata getrennt, un die Klammern am Ende des Methodenaufrufs geschrieben werden. Als Parameter können sowohl Refernezen als auch Literale aufgegeben werden:
```py
> var = 12
> referenz.methode(var, "Hallo Welt")
```
Wie viele und welche Parameter einer Methode übergeben werden dürfen, hängt von ihrer Definition ab und ist daher von Methode zu Methode verschieden. Eine Methode zusammen mit den Parametern, die sie erwartet, wird _Schnittstelle_ gennant.
```py
> methode(parameter1, parameter2, parameter3)
```
In diesem Fall erwartet die Methode drei positionsbezogene Parameter. Positionsbezogen bedeutet, dass die beim Methodenaufruf übergebenen Instanzen entsprechend ihrer Position in der Parameterliste den Parametern zugeordnet werden. 
```py
referenz.methode(1, 45, -7)
```

- ### Schlüsselwortparameter
Es ist auch möglich, einer Methode _Schlüsselwortparameter (engl. keyword arguments)_ zu übergeben. Schlüsselwortparameter werden direkt mit dem formalen Parameternamen verknüpftm und ihre Reihenfolge in der Parameterliste spielt keine Rolle mehr,
Um einen Wert als Schlüsselwortparameter zu übergeben, weist man den Parameternamen innerhalb des Methodenaufrufs den zu übergebenden Wert mithilfe des Gkeichheitszeichens zu. Die beiden folgenden Methodenaufrufe sind demnach gleichwertig:
```py
> referenz.methode(1, 2, 3)
> referenz.methode(parameter2=2, parameter1=1, parameter3=3)
```
Allerdings können auch positions- und schlüsselwortbezogene Parameter gemischt werden, wobei allerdings alle Schlüsselwortparameter am Ende der Parameterliste stehen müssen. Damit ist der fildende Aufruf äquivalent zu den beiden vorangegangenen:
```py
> referenz.methode(1, parameter3=3, parameter2=2)
```
In der Regel werden Parameter postionsbezogen übergeben, weil der Schreibaufwand geringer ist.

### Optionale Parameter
Es gibt optionale Parameter, die nur bei Bedarf übergeben werden müssen. Methoden mit solchen Parametern werden durch eckige Klammern gekennzeichnet:
```py
> methode(parameter1, [parameter2, parameter3])
```
In diesem Beispiel ist also nur Parameter 1 erforderlich und Parameter 2 und Parameter 3 sind optional.

### Reine Schlüsselwortparameter
Eine Funktion oder Methode kann über reine Schlüsselwortparameter verfügen. Das sind Parameter, die ausschließlich in Schlüsselwortschreibweise übergeben werden können. Diese Parameter werden in einer Funktions- oder Methodenschnittstelle durch geschweifte Klammern gekennzeichnet:
```py
> methode(parameter1, parameter2, {parameter3})
```
Diese können optional oder nicht optional sein.

<a name="attribute"></a>

### Attribute
Neben Methoden können Instanzen auch Attribute besitzen. Bei einem Attribut handelt es sich um eine Referenz, die mit einer Instanz verknüpft ist. Beispielsweise besitzt jede komplexe Zahl für den Zugriff auf ihren Real- bzw. Imaginärteil die Attribute `real` und `imag`.
```py
> zahl = 5 + 6j
> zahl.real
>> 5.0
> zahl.imag
>> 6.0
```
Da ein Ausdruck der Form referenz.attribut selbst wieder eine Referenz ist, lässt er sich wie jede andere Referenz verwenden. Er kann als Operand in einer Berechnung auftreten oder in eine Liste gespecihert werden:
```py
> zahl.real*zahl.real+5*zahl.imag
>> 55.0
> [1, zahl.imag, zahl.real]
>> [1, 6.0, 5.0]
```
Insbesondere kann die Instanz, auf die referenz.attribut verweist, selbst ein Attribut `aaa` besitzen, auf das dann mixt referenz.attribut.aaa zugegriffen werden kann. Genauso funktioniert der Zugriff auf eine Methode der Instanz referenz.attribut.methode(parameter1, parameter2).
Im nachfolgenden Beispiel zeigt das Attribut `real` einer komplexen Zahl auf eine Gleitkommazhal die ihrerseits eine Methode `is_integer` besitzt, um zu prüfen, ob es sich um eine ganze Zahl handel:
```py
> zahl.real.is_integer
>> TRUE
```
Hier wurde also über zahl.real auf den Realteil 5.0 der komplexen Zahl 5+6j ,zugegriffen und anschließend die Methode is_integer von 5.0 aufgerufen.
In Python-Programmen treten solche verschachtelten Attribut- und Methodenzugriffe häufig auf.

<a name="informationsquellen-zu-python"></a>

## Informationsquellen zu Python

### Die Built-in Funkction help
Um die interaktive Hilfefunktion zu starten, kann die eingebaute Funktion `help` aufgerufen werden. Mit `help()` wird ein Einleitungstext ausgegeben, gefolgt von einem Eingabeprompt. Hier können Begriffe nachgeschlagen werden. Mögliche Begriffe sind Schlüsselwörter wie `for`, Synbole wie `+`, Module `pprint` oder Themen `DEBUGGING`. Eine Lister der möglichen Suchbegriffe in den jeweiligen Kategorien lässt sich über die Befehle _keywords_, _symbols_, _modules_ und _topics_ anzeigen.

### Die Onlinedokumentation
Die Texte, die Pythons interaktive Hilfefunktion anzeigt, sind Auszüge aus der Doku. Die jeweils aktuellste Version findet man unter https://docs.python.org. Über eine Auswahlliste in der oberen linken Ecke lässt sich zur Dokumentation einer älteren Python-Version wechseln.

### PEPs
Python Enhancement Proposals, kurz PEPs, sind kurze Ausarbeitungen, die ein Problem in der Sprache oder im Interpreter identifizieren, mögliche Lösungsansätze und die Diskussion darüber zusammenfassen und schließlich eine Lösung vorzuschlagen. Unter https://www.python.org/dev/peps findet man eine Liste aller vorgeschlagenen PEPs. Jedoch kann ein PEP mitunter sehr technisch ausfallen, was dazuführt, dass selbst erfahrene Python-Entwickler dieses nur schwer verstehen.


<a name="teil-ii:-datentypen"></a>

# Teil II: Datentypen

<a name="basisdatentypen:-eine-übersicht"></a>

## Basisdatentypen: eine Übersicht
| Datentyp  | speichert | Veränderlichkeit |
|----------|----------|----------|
|  NoneType | das Nichts | unerveränderlich |
|  *_Numerische Datentypen_*  |
|  int | ganze Zahlen | unerveränderlich |
| float  | Gleitkommazahlen  | unveränderlich  |
|bool  |boolesche Werte  |  unveränderlich|
|complex  | komplexe Zahlen |  unveränderlich|
|  Sequenzielle Datentypen |
| list | Listen  | veränderlich  |
| tuple  | Listen  | unveränderlich  |
| str | Text | unveränderlich  |
| bytes | Binärdaten als Sequenz von Bytes  | unveränderlich  |
| bytearray | Binärdaten als Sequenz von Bytes  | veränderlich  |
| *_Zuordnungen und Mengen_*  |
| dict | Schlüssel-Wert-Zuordnungen  | veränderlich  |
| set | Mengen beliebiger Instanzen | veränderlich  |
| frozenset  | Mengen beliebiger Instanzen  | unveränderlich  |

### Das Nichts - NoneType

Es gibt nur eine einzige Instanz des _"Nichts"_, das _None_. Das ist eine Konstante, die jederzeit im Quelltext verwendet werden kann.
```py
> ref = NONE
> ref
> print(ref)
>> NONE
```
Man kann None verwenden, um zu überprüfen, ob eine Referenz auf nichts verweist:
```py
> if ref is None:
>  print("ref is None")
>> ref is None
```
Wichtig: mit dem Schlüsselwort _is_ wird überprüft, ob die von `ref` referenzierte Instanz mit `None` identisch ist. Dies kann auch mit dem Operator `==` erfolgen, wobei diese Operationen, nur in diesem Beispiel und auch nur in diesem Fall, vordergründig äquivalent sind, denn mit `==` werden zwei Werte und mit `is` zwei Identitäten auf Gleichheit überprüft.

### Operatoren
In Python hängt die Bedeutung eines Operators davon ab, auf welchen Datentypen er angewendet wird. In Python haben Operatoren, wie auch in der Mathematik, eine Bindigkeit. Diese ist so definiert, dass `*` stärker bindet als `+`. Es gilt also: _Punkt vor Strich_. Zudem gibt es eine Operatorenrangfolge, die definiert, welcher Operator wie stark bindet und auf diese Weise einem klammerlosen Ausdruck eine eindeutige Auswertungsreihenfolge und damit einen eindeutigen Wert zuweist.

|Operator  | Übliche Bedeutung |
|------|------|
| x**y |  y-te Potenz von x  |
|+x  | positives Vorzeichen  |
|-x  |negatives Vorzeichen  |  
| ~x | bitweises Komplement von x  |   
| x*y | Produkt von x und y  |  
| x/y | Quotient von x und y  |  
| x%y | Rest bei ganzzahliger Division von x durch y  |  
| x//y | ganzzahlige Division von x durch y  |  
| x@y | Matrizenmultiplikation von x und y  |     
| x+y | Addition von x und y  |  
| x-y | Subtraktion von x und y  |  
| x>>n | bitweise Verschiebung um n Stellen nach rechts  |  
| x<<n | bitweise Verschiebung um n Stellen nach links  |  
| x&y | bitweises UND zwischen x und y  |  
| x^y | bitweises ausschließendes ODER zwischen x und y |  
| x|y | bitweises nicht ausschließendes ODER zwischen x und y |  
|x<y  | ist x kleiner y? |  
|x>y  | ist x größer y? |  
| x<=y | ist x kleiner oder gleich y? |  
| x>=y | ist x größer oder gleich y? |  
| x!=y  |ist x ungleich y?  |  
| x==y | ist x gleich y? |  
| x is y | sind x und y identisch? |  
| x is not y | sind x und y nicht identisch? |  
| x in y | befindet sich x in y? |  
| x not in y | befindet sich x nicht in y? |  
| not x | logische Negierungs |  
| x and y | logisches UND  |  
| x or y | logisches ODER |  

Eine weiter Regel von Python: Ausdrücke oder Teilausdrücke, die nur aus Operatoren gleicher Bindigkeit bestehen, werden von _links nach rechts_ ausgewertet.
```py
> 6-2-3
>> 1
```
<a name="numerische-datentypen"></a>

## Numerische Datentypen
| Datentyp  | speichert | Veränderlichkeit |
|----------|----------|----------|
|  int | ganze Zahlen | unerveränderlich |
| float  | Gleitkommazahlen  | unveränderlich  |
|bool  |boolesche Werte  |  unveränderlich|
|complex  | komplexe Zahlen |  unveränderlich|

Alle numerischen Datentypen sind unveränderlich!

### Arithmetische Operatoren
Zu den bereits aufgezeigten arithemtischen Operatoren gibt es in Python die Möglichkeit, diese verkürzt Darzustellen.
| Operator  | Entsprechung|
|----------|----------|
| x+=y | x=x+y  |
| x-=y | x=x-y |
| x*=y | x= x*y  |
| x/=y | x=x/y |
| x%=y | x=x%y  |
| x**=y | x=x**y |
| x//=y | x=x//y |

### Vergleichende Operatoren
| Vergleich               |            Bedeutung   |
| ------------------------| ---------------------- |
| ==                      | ist gleich/das Selbe   |
| !=                      | ist ungleich           |
| <                       | ist kleiner            |
| >                       | ist größer             |
| <=                      | ist kleiner oder gleich|
| >=                      | ist größer oder gleich |

Da komplexe Zahlen prinzipiell nicht sinnvoll anzuordnen sind, lässt der Datentyp `complex`nur die Verwendung der ersten beiden Operatoren zu.

### Konvertierung zwischen numerischen Datentypen

Numerische Datentypen können über die eingebauten Funktionen `float`, `int`, `bool` und `complex` ineinander umgeformt werden. Dabei können je nach Umformung Informationen verloren gehen. 
```py
> float(33)
>> 33
> int(33.5)
>> 33
> bool(12)
>> True
> complex(True)
>>(1+0j)
```
Anstelle eines konkreten Literals kann auch eine Referenz eingesetzt bzw. eine Referenz mit dem entstehenden Wert verknüpft werden:
```py
> var1 = 12.5
> int(var1)
>> 12
> var2 = int(40.25)
> var2
>> 40
```

<a name = "ganzzahlen-int"></a>

## Ganzzahlen - int
Für den Raum der ganzen Zahlen gibt es in Python den Datentyp `int`. Im Gegensatz zu vielen anderen Programmiersprachen unterliegt dieser Datentyp in seinem Wertebereich keine prinzipiellen Grenzen, was den Umgang mit großen Zahlen in Python erleichtert. Seit Python 3.6 kann ein Unterstrich verwendet werden, um die Ziffern eines Literals zu gruppieren:

```py
> 1_000_000
>> 1000000
> 1_0_0
>> 100
```
Die Gruppierung ändert nichts am Zahlenwert des Literals, sondern dient dazu, die Lesbarkeit von Zahlenliteralen zu erhöhen.
