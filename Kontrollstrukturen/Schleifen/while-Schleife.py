zahl = 1224

while zahl != 1234:
    print("Die aktuelle Zahl ist: " + str(zahl) + ".")
    zahl += 1


geheime_zahl = 70
versuch = 64

while versuch != geheime_zahl:
    print("das ist dein " +  str(versuch) + ". Versuch.")
    versuch += 1
    if versuch == 69:
        print("Das Spiel wird beendet, da du bei Versuch " + str(versuch)+ " angelangt bist.")
        break


while True:
    zahl = int(input("Geben Sie eine Zahl ein: "))
    if zahl < 0:
        print("Bitt keine negativen Zahlen.")
        continue
    ergebnis = 1
    while zahl > 0:
        ergebnis = ergebnis * zahl
        zahl -= 1
    print("Ergebnis: " + str(ergebnis))
