# Aufgabe 5: Winkelmass Umwandler
# Konvertiert zwischen Gradmass und Bogenmass

from math import pi

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