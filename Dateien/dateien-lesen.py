
file_object = open("Dateien/dateien-lesen.txt","r")
for line in file_object:
    print(line)
file_object.close

laender = {}

file_object = open("Dateien/dateien-lesen.py", "r")
for line in file_object:
    zuordnung = line.split(" ")
    laender[zuordnung[0]] = zuordnung[1]
file_object.close
while True:
    land = input("Geben Sie ein Land ein: ")
    if land in laender:
        print("Der deutsche Name für dieses Land lautet: ", laender[land])
    else:
        print("Das Land befindet sich nicht im dictionary.")


