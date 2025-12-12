# Aufgabe 3: Größenvergleich
# Vergleicht zwei Nutzereingaben

# Nutzereingaben anfordern
eingabe1 = int(input("Bitte geben Sie die erste Zahl ein: "))
eingabe2 = int(input("Bitte geben Sie die zweite Zahl ein: "))

# Vergleich durchführen
if eingabe1 > eingabe2:
    print("Eingabe 1 war größer")
elif eingabe2 > eingabe1:
    print("Eingabe 2 war größer")
else:
    print("Die Eingaben waren identisch")