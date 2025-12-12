# Aufgabe 4: Summieren mit while-Schleife

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