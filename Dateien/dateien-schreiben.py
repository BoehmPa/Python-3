woerter = {
    "Germany" : "Deutschland", 
    "Spain" : "Spanien",
    "Greece" : "Griechenland"
}

fobj = open("Dateien/dateien-schreiben.txt", "w")
for engl in woerter:
    fobj.write("{}{}".format(engl, woerter[engl]))
fobj.close
