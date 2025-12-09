# Aufgabe 6: Würfelspiel mit Computergegner
# Ziel: Erreiche genau 21 Punkte vor dem Computer

from random import randint

print("Willkommen zum Würfelspiel mit Computergegner!")
print("Ziel: Erreiche genau 21 Punkte vor dem Computer\n")

spieler_punkte = 0
computer_punkte = 0
runde = 0

while spieler_punkte != 21 and computer_punkte != 21:
    runde += 1
    print(f"--- Runde {runde} ---")

    # Spieler würfelt
    input("Drücken Sie Enter zum Würfeln...")
    spieler_wurf = randint(1, 6)
    print(f"Spieler würfelt: {spieler_wurf}")
    spieler_punkte += spieler_wurf

    if spieler_punkte > 21:
        print(f"Spieler überschreitet mit {spieler_punkte} Punkten! Zurück auf 0.")
        spieler_punkte = 0
    elif spieler_punkte == 21:
        print(f"Spieler gewinnt mit 21 Punkten!")
        break
    else:
        print(f"Spieler Punktzahl: {spieler_punkte}")

    # Computer würfelt
    computer_wurf = randint(1, 6)
    print(f"Computer würfelt: {computer_wurf}")
    computer_punkte += computer_wurf

    if computer_punkte > 21:
        print(f"Computer überschreitet mit {computer_punkte} Punkten! Zurück auf 0.")
        computer_punkte = 0
    elif computer_punkte == 21:
        print(f"Computer gewinnt mit 21 Punkten!")
        break
    else:
        print(f"Computer Punktzahl: {computer_punkte}")

    print(f"\nSpielstand: Spieler {spieler_punkte} - Computer {computer_punkte}\n")

print(f"\nSpiel beendet nach {runde} Runden!")