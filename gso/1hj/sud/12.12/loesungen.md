# Lösungen Klausur der Unterbrücken-Bus-Akademie

## Aufgabe 1: Binär-Uhr

### a) [4 Punkte]
**Begründung, warum die obere Zeile unabhängig von der Uhrzeit die Stundenzahl darstellen muss:**

Die obere Zeile der Binär-Uhr muss unabhängig von der angezeigten Uhrzeit immer die Stundenzahl darstellen, weil:

1. **Stellenwertigkeit im Binärsystem**: In einer Binärdarstellung hat jede Position einen festen Stellenwert (20, 21, 22, 23, 24). Die Stunden werden im 24-Stunden-Format dargestellt und benötigen maximal 5 Bits (0-23).

2. **Eindeutige Zuordnung**: Die obere Zeile repräsentiert die Stunden-Bits, die mittlere Zeile die Minuten-Bits und die untere Zeile die Sekunden-Bits. Diese Zuordnung ist fest und ändert sich nicht mit der Zeit.

3. **Logische Struktur**: Die Binär-Uhr folgt dem Prinzip der positionsbasierten Darstellung. Jede Zeile hat eine feste Bedeutung, unabhängig vom aktuellen Zeitwert.

4. **Im Beispiel sichtbar**: Die Zeit 23:02:14 zeigt in der oberen Zeile genau die Binärdarstellung von 23 (10111 in binär), was unabhängig von Minuten und Sekunden ist.

### b) [8 Punkte]
**Sekundendarstellung für 18:17:36 Uhr:**

Die Zeit ist 18:17:36, die Sekundenzahl ist also **36**.

36 in binär: 36 = 32 + 4 = 100100 (binär)

Darstellung im Binär-Uhr-Grid (nur Symbole mit Zustand AN):
- Bit 5 (32): AN (gefülltes Quadrat)
- Bit 4 (16): AUS
- Bit 3 (8): AUS
- Bit 2 (4): AN (gefülltes Quadrat)
- Bit 1 (2): AUS
- Bit 0 (1): AUS

**Die Sekunden-Zeile zeigt: ▮ ▯ ▯ ▮ ▯ ▯** (Position 5 und 2 gefüllt)

---

## Aufgabe 2: Hex-Editor - Zeichencodes

Die fünf unbekannten Textzeichen ermittelt:

| Zeichencode (linke Markierung) | 4A | 61 | 68 | 72 | 3B |
|--------------------------------|----|----|----|----|-----|
| Dualcode                       | 0100 1010 | 0110 0001 | 0110 1000 | 0111 0010 | 0011 1011 |
| Dezimal (Hilfszeile)          | 74 | 97 | 104 | 114 | 59 |
| Textzeichen (rechte Markierung)| J  | a  | h  | r  | ; |

**Herleitung:**
- 4A (hex) = 74 (dez) = 0100 1010 (binär) → ASCII: 'J'
- 61 (hex) = 97 (dez) = 0110 0001 (binär) → ASCII: 'a'
- 68 (hex) = 104 (dez) = 0110 1000 (binär) → ASCII: 'h'
- 72 (hex) = 114 (dez) = 0111 0010 (binär) → ASCII: 'r'
- 3B (hex) = 59 (dez) = 0011 1011 (binär) → ASCII: ';'

Das ergibt das Wort "Jahr;"

---

## Aufgabe 3: Flächenberechnung Programm

### a) [8 Punkte] Fünf Fehler im Code

| Fehlernummer | Beschreibung |
|--------------|--------------|
| 1 | **Keine Anweisung im Else-Block (Zeile ~6)**: Nach dem ersten `if a == "Rechteck":` fehlt eine Anweisung im impliziten Else-Fall. Der Code springt direkt zu `else b = "Flächeninhalt":` was syntaktisch falsch ist. |
| 2 | **Falsche Variable 'O' statt 'o' (Zeile ~15)**: In der Rechteck-Umfang-Berechnung wird `O = 2 * q + 2` verwendet, aber später wird `print("Der Umfang ist", O, "cm groß")` aufgerufen. Es sollte durchgehend kleine 'o' verwendet werden, oder die Variable muss konsistent benannt sein. |
| 3 | **Fehlende Konvertierung zu int() bei Dreieck-Umfang (Zeile ~28)**: Bei `q = input(...)` für die Kantenlänge der Grundseite fehlt die Konvertierung zu int(). Es sollte `q = int(input(...))` sein. |
| 4 | **Falsche Formel für Quadrat-Umfang (Zeile ~17)**: Die Formel `Q = q + q + q + q` ist zwar korrekt, aber die Ausgabe verwendet ein großes 'Q' während die Variable möglicherweise 'O' sein sollte für Konsistenz. |
| 5 | **Schreibweise "Dreieck" inkonsistent (Zeile ~27)**: Im Code steht `elif a == "Dreieck":` aber in der ersten Abfrage wird möglicherweise eine andere Schreibweise erwartet. Groß-/Kleinschreibung muss beachtet werden! |

### b) [8 Punkte] Blackbox Tests

**Nicht genutzte Eingabefelder markiert mit ✗:**

| Testfall-Nr | Eingabe a | Eingabe b | q | z | w | r | R | Soll-Ausgabe | Ok/Nicht Ok |
|-------------|-----------|-----------|---|---|---|---|---|--------------|-------------|
| 1 | Quadrat | Umfang | 4 | ✗ | ✗ | ✗ | ✗ | 16 | Ok |
| 2 | Dreieck | Umfang | 2 | 3 | ✗ | ✗ | ✗ | 9 | Ok |
| 3 | Rechteck | Flächeninhalt | 5 | 5 | ✗ | ✗ | ✗ | 25 | Ok |
| 4 | Dreieck | Flächeninhalt | ✗ | ✗ | ✗ | 4 | 2 | 4 | Ok |
| 5 | Rechteck | Flächeninhalt | 4 | 6 | ✗ | ✗ | ✗ | 24 | Ok |
| 6 | Quadrat | Flächeninhalt | 5 | ✗ | ✗ | ✗ | ✗ | 25 | Ok |

**Erklärung:**
- Testfall 1: Quadrat Umfang benötigt nur q (Kantenlänge)
- Testfall 2: Dreieck Umfang benötigt q (Grundseite), z (erste Seite), w wird nicht genutzt da Formel falsch ist
- Testfall 3: Rechteck Flächeninhalt benötigt q und z (zwei Kantenlängen)
- Testfall 4: Dreieck Flächeninhalt benötigt r (Höhe) und R (Grundseite)
- Testfall 5: Rechteck Flächeninhalt benötigt q und z
- Testfall 6: Quadrat Flächeninhalt benötigt nur q