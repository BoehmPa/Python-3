geheimnis = 1337
versuch = -1
zaehler = 0

while versuch != geheimnis:
    versuch = int(input("Raten Sie: "))

    if versuch > geheimnis:
        print("kleiner")

    if versuch < geheimnis:
        print("größer")
    zaehler += 1

print(f"Super, du hast es in {zaehler} Versuchen geschafft!")