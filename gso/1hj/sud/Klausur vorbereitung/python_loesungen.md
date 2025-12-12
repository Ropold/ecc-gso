# Klausurvorbereitung - Python Lösungen

## Aufgabe 1: Umrechnung

**Frage:** Ein Computer kodiert Buchstaben und Sonderzeichen als achtstellige Dualzahlen. Wie viele verschiedene Zeichen können auf diese Weise codiert werden?

**Lösung:**
- Bei 8 Bit gibt es 2^8 = **256 verschiedene Zeichen**

---

## Aufgabe 3: Größenvergleich

```python
# Größenvergleich von zwei Nutzereingaben

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
```

---

## Aufgabe 4: Summieren

**Variante 1: Mit while-Schleife**

```python
# Summieren mit while-Schleife

# Nutzer gibt Unter- und Obergrenze an
untergrenze = int(input("Bitte geben Sie die Untergrenze ein: "))
obergrenze = int(input("Bitte geben Sie die Obergrenze ein: "))

# Summe berechnen
summe = 0
i = untergrenze

while i <= obergrenze:
    summe += i
    i += 1

print(f"Die Summe von {untergrenze} bis {obergrenze} ist: {summe}")
```

**Variante 2: Mit for-Schleife**

```python
# Summieren mit for-Schleife

# Nutzer gibt Unter- und Obergrenze an
untergrenze = int(input("Bitte geben Sie die Untergrenze ein: "))
obergrenze = int(input("Bitte geben Sie die Obergrenze ein: "))

# Summe berechnen
summe = 0

for i in range(untergrenze, obergrenze + 1):
    summe += i

print(f"Die Summe von {untergrenze} bis {obergrenze} ist: {summe}")
```

---

## Aufgabe 5: Winkelmass Umwandler

```python
from math import pi

# Winkelmass Umwandler

print("Winkelmass Umwandler")
print("1 - Von Gradmass zu Bogenmass")
print("2 - Von Bogenmass zu Gradmass")

wahl = int(input("Bitte wählen Sie eine Option (1 oder 2): "))

if wahl == 1:
    # Gradmass zu Bogenmass
    grad = float(input("Bitte geben Sie den Winkel in Grad ein: "))
    bogenmass = (grad * pi) / 180
    print(f"{grad}° = {bogenmass} rad")
elif wahl == 2:
    # Bogenmass zu Gradmass
    rad = float(input("Bitte geben Sie den Winkel in Bogenmass (rad) ein: "))
    gradmass = (rad * 180) / pi
    print(f"{rad} rad = {gradmass}°")
else:
    print("Ungültige Eingabe!")
```

**Formeln:**
- Grad zu Bogenmass: `rad = (grad × π) / 180`
- Bogenmass zu Grad: `grad = (rad × 180) / π`

---

## Aufgabe 6: Würfelspiel

```python
from random import randint

# Würfelspiel bis 21 Punkte

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
        print(f"\n🎉 Glückwunsch! Du hast 21 Punkte erreicht!")
        print(f"Du hast {wurf_anzahl} Würfe gebraucht.")
    else:
        print(f"Aktuelle Punktzahl: {punkte}\n")
```

**Zusatz: Mit Computergegner**

```python
from random import randint

# Würfelspiel mit Computergegner

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
        print(f"🎉 Spieler gewinnt mit 21 Punkten!")
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
        print(f"💻 Computer gewinnt mit 21 Punkten!")
        break
    else:
        print(f"Computer Punktzahl: {computer_punkte}")

    print(f"\nSpielstand: Spieler {spieler_punkte} - Computer {computer_punkte}\n")

print(f"\nSpiel beendet nach {runde} Runden!")
```