# Aufgabe 4: Summieren mit for-Schleife

# Nutzer gibt Unter- und Obergrenze an
untergrenze = int(input("Bitte geben Sie die Untergrenze ein: "))
obergrenze = int(input("Bitte geben Sie die Obergrenze ein: "))

# Summe berechnen
summe = 0

for i in range(untergrenze, obergrenze + 1):
    summe += i

print(f"Die Summe von {untergrenze} bis {obergrenze} ist: {summe}")