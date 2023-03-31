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
    - [Ein Dateiobjekt erzeugen](#ein-dateiobjekt-erzeugen)
- [Das Laufzeitmodell](#das-laufzeitmodell)
    - [Die Struktur von Instanzen](#die-struktur-von-instanzen)


  










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

Eine `while`-Schleife besteht asi einem Schleifenkopf, in welchem die Bedingung steht und einem Schleifenkörper, welcher den Codeblock enthält, welcher ausgeführt werden soll. Die `while`-Schleife läuft _solange_ eine Bedingung erfüllt ist und nicht _bis_ diese erfüllt ist. Eine Datei mit Beispielen findest du [hier](Kontrollstrukturen/Schleifen/while-Schleife.py)

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

Mit der Methode `split` um die aktuelle Zeile in zwei Teile aufzuteilen. Der Teil links des Leerzeichens (das englische Wort) und den Teil rechts vom Leerzeichen (das deutsche Wort). Als nächstes wird ein Eintrag ins dictionary angelegt, mit dem Schlüssel zuordnung[0] und dem Wert zuordnung[1].
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




