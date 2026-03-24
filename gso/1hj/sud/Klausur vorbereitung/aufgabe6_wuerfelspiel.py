# Aufgabe 6: Würfelspiel
# Ziel: Erreiche genau 21 Punkte
# Regel: Bei Überschreitung fällst du auf 0 zurück

from random import randint

print("Willkommen zum Würfelspiel!")
print("Ziel: Erreiche genau 21 Punkte")
print("Regel: Bei Überschreitung fällst du auf 0 zurück\n")

punkte = 0
wurf_anzahl = 0

while punkte != 21:
    input("Drücken Sie Enter zum Würfeln...")

    # Würfeln (1-6)
    wurf = randint(1, 6)
    wurf_anzahl += 1

    print(f"Wurf {wurf_anzahl}: Du hast eine {wurf} gewürfelt")

    # Punkte addieren
    punkte += wurf

    # Überprüfung
    if punkte > 21:
        print(f"Oh nein! Mit {punkte} Punkten hast du 21 überschritten!")
        print("Du fällst auf 0 zurück.\n")
        punkte = 0
    elif punkte == 21:
        print(f"\nGlückwunsch! Du hast 21 Punkte erreicht!")
        print(f"Du hast {wurf_anzahl} Würfe gebraucht.")
    else:
        print(f"Aktuelle Punktzahl: {punkte}\n")