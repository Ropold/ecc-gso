# Bits und Bytes

## Was ist ein Bit?

Ein **Bit** ist die kleinste Informationseinheit in der Informatik. Der Begriff kommt von "**bi**nary digi**t**" (binäre Ziffer).

Ein Bit kann nur zwei Zustände haben:
- `0` (aus/falsch)
- `1` (an/wahr)

### Beispiele für Bits:
- Lichtschalter: aus (0) oder an (1)
- Antwort: nein (0) oder ja (1)
- Strom: kein Strom (0) oder Strom fließt (1)

## Was ist ein Byte?

Ein **Byte** besteht aus **8 Bits** und kann damit 256 verschiedene Werte darstellen (2^8 = 256).

### Beispiel eines Bytes:
```
01001000
```

Jede Position ist ein Bit, insgesamt 8 Stück = 1 Byte

## Wertebereich eines Bytes

Mit 8 Bits kann man Zahlen von 0 bis 255 darstellen:
- Kleinster Wert: `00000000` = 0
- Größter Wert: `11111111` = 255

## Umrechnung von Binär zu Dezimal

Jedes Bit hat einen Stellenwert (von rechts nach links):

```
Position:    7    6    5    4    3    2    1    0
Stellenwert: 128  64   32   16   8    4    2    1
Bit:         0    1    0    0    1    0    0    0
             └────┴────┴────┴────┴────┴────┴────┴──→
                    64 + 8 = 72
```

Das Byte `01001000` entspricht also der Dezimalzahl **72** (was dem ASCII-Zeichen 'H' entspricht).

### Schritt-für-Schritt Anleitung

**Methode 1: Addition der Stellenwerte**

1. Schreibe die Stellenwerte über die Binärzahl (128, 64, 32, 16, 8, 4, 2, 1)
2. Markiere alle Positionen mit einer 1
3. Addiere die Stellenwerte an den markierten Positionen

**Beispiel:** `10110101`
```
128  64   32   16   8    4    2    1
 1    0    1    1    0    1    0    1
 ↓         ↓    ↓         ↓         ↓
128 +    32 + 16  +   4   +    1 = 181
```

**Methode 2: Verdopplungsmethode (von links nach rechts)**

1. Starte mit 0
2. Gehe von links nach rechts durch die Binärzahl
3. Für jede Stelle: Verdopple den aktuellen Wert und addiere das Bit (0 oder 1)

**Beispiel:** `10110101`
```
Schritt 1: 0 × 2 + 1 = 1
Schritt 2: 1 × 2 + 0 = 2
Schritt 3: 2 × 2 + 1 = 5
Schritt 4: 5 × 2 + 1 = 11
Schritt 5: 11 × 2 + 0 = 22
Schritt 6: 22 × 2 + 1 = 45
Schritt 7: 45 × 2 + 0 = 90
Schritt 8: 90 × 2 + 1 = 181
```

### Weitere Umrechnungsbeispiele

#### Beispiel 1: `11111111`
```
128 + 64 + 32 + 16 + 8 + 4 + 2 + 1 = 255
```
Dies ist der größtmögliche Wert eines Bytes.

#### Beispiel 2: `10000000`
```
128 = 128
```
Nur das höchstwertige Bit ist gesetzt.

#### Beispiel 3: `00001111`
```
8 + 4 + 2 + 1 = 15
```
Die unteren 4 Bits (Nibble) sind gesetzt.

## Umrechnung von Dezimal zu Binär

Um eine Dezimalzahl in eine Binärzahl umzuwandeln, gibt es mehrere Methoden:

### Methode 1: Division durch 2 (Restmethode)

1. Teile die Dezimalzahl durch 2
2. Notiere den Rest (0 oder 1)
3. Wiederhole mit dem Ergebnis, bis 0 erreicht ist
4. Die Binärzahl ergibt sich aus den Resten von unten nach oben

**Beispiel:** 181 → Binär
```
181 ÷ 2 = 90  Rest 1  ←─ Letztes Bit (Position 0)
 90 ÷ 2 = 45  Rest 0
 45 ÷ 2 = 22  Rest 1
 22 ÷ 2 = 11  Rest 0
 11 ÷ 2 =  5  Rest 1
  5 ÷ 2 =  2  Rest 1
  2 ÷ 2 =  1  Rest 0
  1 ÷ 2 =  0  Rest 1  ←─ Erstes Bit (Position 7)

Ergebnis: 10110101
```

### Methode 2: Subtraktion der Stellenwerte

1. Beginne mit dem größten Stellenwert (128 bei einem Byte)
2. Wenn die Zahl größer/gleich dem Stellenwert ist: setze 1 und subtrahiere
3. Wenn die Zahl kleiner ist: setze 0
4. Wiederhole mit dem nächsten Stellenwert

**Beispiel:** 181 → Binär
```
181 ≥ 128? Ja → 1, Rest: 181 - 128 = 53
 53 ≥  64? Nein → 0
 53 ≥  32? Ja → 1, Rest: 53 - 32 = 21
 21 ≥  16? Ja → 1, Rest: 21 - 16 = 5
  5 ≥   8? Nein → 0
  5 ≥   4? Ja → 1, Rest: 5 - 4 = 1
  1 ≥   2? Nein → 0
  1 ≥   1? Ja → 1, Rest: 1 - 1 = 0

Ergebnis: 10110101
```

### Weitere Umrechnungsbeispiele (Dezimal → Binär)

#### Beispiel 1: 200 → Binär
```
200 ≥ 128? Ja → 1, Rest: 72
 72 ≥  64? Ja → 1, Rest: 8
  8 ≥  32? Nein → 0
  8 ≥  16? Nein → 0
  8 ≥   8? Ja → 1, Rest: 0
  0 ≥   4? Nein → 0
  0 ≥   2? Nein → 0
  0 ≥   1? Nein → 0

Ergebnis: 11001000
```

#### Beispiel 2: 100 → Binär
```
100 ≥ 128? Nein → 0
100 ≥  64? Ja → 1, Rest: 36
 36 ≥  32? Ja → 1, Rest: 4
  4 ≥  16? Nein → 0
  4 ≥   8? Nein → 0
  4 ≥   4? Ja → 1, Rest: 0
  0 ≥   2? Nein → 0
  0 ≥   1? Nein → 0

Ergebnis: 01100100
```

## Übungsaufgaben

### Aufgaben: Binär → Dezimal

Rechne folgende Binärzahlen in Dezimalzahlen um:

1. `00110011` = ?
2. `11110000` = ?
3. `01010101` = ?
4. `10101010` = ?
5. `00001000` = ?

<details>
<summary>Lösungen anzeigen</summary>

1. `00110011` = 32 + 16 + 2 + 1 = **51**
2. `11110000` = 128 + 64 + 32 + 16 = **240**
3. `01010101` = 64 + 16 + 4 + 1 = **85**
4. `10101010` = 128 + 32 + 8 + 2 = **170**
5. `00001000` = 8 = **8**

</details>

### Aufgaben: Dezimal → Binär

Rechne folgende Dezimalzahlen in Binärzahlen um (8 Bits):

1. 64 = ?
2. 127 = ?
3. 33 = ?
4. 250 = ?
5. 16 = ?

<details>
<summary>Lösungen anzeigen</summary>

1. 64 = **01000000**
2. 127 = **01111111**
3. 33 = **00100001**
4. 250 = **11111010**
5. 16 = **00010000**

</details>

### Aufgaben: Gemischt

1. Wie viele verschiedene Werte kann man mit 4 Bits darstellen?
2. Was ist der größte Wert, den man mit 6 Bits darstellen kann?
3. Wie viele Bytes sind 1 MB (nach binärer Definition)?
4. Wandle um: `11011011` → Dezimal → Hex

<details>
<summary>Lösungen anzeigen</summary>

1. 2^4 = **16 verschiedene Werte** (0 bis 15)
2. Mit 6 Bits: 2^6 - 1 = 63, also **63** (Binär: `111111`)
3. 1 MB = 1024 KB = 1024 × 1024 Bytes = **1.048.576 Bytes**
4. `11011011` = 128 + 64 + 16 + 8 + 2 + 1 = 219 = **0xDB** (Hex)

</details>

## Größere Einheiten

### Binäre Präfixe (IEC-Standard)

- 1 Byte = 8 Bits
- 1 Kilobyte (KB) = 1.024 Bytes = 2^10 Bytes
- 1 Megabyte (MB) = 1.024 KB = 1.048.576 Bytes = 2^20 Bytes
- 1 Gigabyte (GB) = 1.024 MB = 1.073.741.824 Bytes = 2^30 Bytes
- 1 Terabyte (TB) = 1.024 GB = 2^40 Bytes

**Warum 1.024 und nicht 1.000?**
Computer arbeiten mit dem Binärsystem (Potenzen von 2). 2^10 = 1.024 ist die nächste Zweierpotenz nahe 1.000.

### Dezimale Präfixe (SI-Standard)

In manchen Bereichen (z.B. Festplattenherstellern) werden auch dezimale Präfixe verwendet:
- 1 Kilobyte (kB) = 1.000 Bytes
- 1 Megabyte (MB) = 1.000 kB
- 1 Gigabyte (GB) = 1.000 MB

**Wichtig:** Achte auf die Schreibweise! KB vs. kB kann unterschiedliche Bedeutungen haben.

### Umrechnungen zwischen Einheiten

#### Von kleineren zu größeren Einheiten (Division)

**Beispiel 1:** 4.096 Bytes in KB umrechnen
```
4.096 Bytes ÷ 1.024 = 4 KB
```

**Beispiel 2:** 5.242.880 Bytes in MB umrechnen
```
Methode 1 (direkt):
5.242.880 Bytes ÷ 1.048.576 = 5 MB

Methode 2 (schrittweise):
5.242.880 Bytes ÷ 1.024 = 5.120 KB
5.120 KB ÷ 1.024 = 5 MB
```

**Beispiel 3:** 2.048 MB in GB umrechnen
```
2.048 MB ÷ 1.024 = 2 GB
```

#### Von größeren zu kleineren Einheiten (Multiplikation)

**Beispiel 1:** 3 KB in Bytes umrechnen
```
3 KB × 1.024 = 3.072 Bytes
```

**Beispiel 2:** 2 GB in MB umrechnen
```
2 GB × 1.024 = 2.048 MB
```

**Beispiel 3:** 1,5 GB in Bytes umrechnen
```
Methode 1 (schrittweise):
1,5 GB × 1.024 = 1.536 MB
1.536 MB × 1.024 = 1.572.864 KB
1.572.864 KB × 1.024 = 1.610.612.736 Bytes

Methode 2 (direkt):
1,5 GB × 1.073.741.824 = 1.610.612.736 Bytes
```

### Übungsaufgaben: Einheiten umrechnen

1. 8.192 Bytes = ? KB
2. 3 MB = ? KB
3. 0,5 GB = ? MB
4. 16.384 KB = ? MB
5. 2.097.152 Bytes = ? MB

<details>
<summary>Lösungen anzeigen</summary>

1. 8.192 Bytes ÷ 1.024 = **8 KB**
2. 3 MB × 1.024 = **3.072 KB**
3. 0,5 GB × 1.024 = **512 MB**
4. 16.384 KB ÷ 1.024 = **16 MB**
5. 2.097.152 Bytes ÷ 1.024 = 2.048 KB ÷ 1.024 = **2 MB**

</details>

## Praktische Beispiele

### Textzeichen
Ein einzelnes Zeichen (z.B. 'A', 'b', '5') benötigt:
- 1 Byte im ASCII-Format
- 1-4 Bytes im UTF-8-Format (je nach Zeichen)

### Farben
Eine Farbe im RGB-Format benötigt:
- 3 Bytes (1 Byte für Rot, 1 für Grün, 1 für Blau)
- Beispiel: `RGB(255, 0, 128)` = `11111111 00000000 10000000`

### Zahlen
- Eine Ganzzahl (Integer): meist 4 Bytes (32 Bits) = Werte von -2.147.483.648 bis 2.147.483.647
- Eine Fließkommazahl (Float): meist 4 oder 8 Bytes

## Zusammenfassung

- **Bit** = kleinste Einheit, kann 0 oder 1 sein
- **Byte** = 8 Bits, kann 256 verschiedene Werte darstellen
- Alles im Computer basiert auf Bits: Zahlen, Text, Bilder, Videos, Programme