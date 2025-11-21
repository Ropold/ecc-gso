# EVP Aufgaben - Datenraten und Datenmengen

## Aufgaben vom Tafelbild (Bild.png)

### Aufgabe: Datenrate berechnen

**Gegeben:**
- Datenmenge = 2³² Byte
- Datenrate = ?
- Zeit = 16 KB/s

**Formel:**
```
Datenrate = Datenmenge / Zeit
```

**Umrechnung:**
```
1 Byte = 8 Bit
Datenmenge in Bit = 2³² Byte × 8 Bit/Byte
```

**Berechnung:**
```
Zeit = Datenmenge / Datenrate
Zeit = (2³² Byte × 8 Bit/Byte) / 16 KB/s
Zeit = 34,36 s
```

---

### Aufgabe: Download-Zeit berechnen

**Gegeben:**
- Datenmenge = 5 GB
- Datenrate = 500 MB/s
- Zeit = ?

**Lösung:**
```
Zeit = Datenmenge / Datenrate
Zeit = 5 GB / 500 MB/s
Zeit = 5000 MB / 500 MB/s
Zeit = 10 s
```

---

## Aufgabe 1 (aus evp.pdf)

### a) Datenübertragungsrate berechnen

**Gegeben:**
- Downstream = 10 GBit/s
- Upstream = 200 MBit/s
- Datenmenge = 2 TB

**Umrechnung der Datenmenge:**
```
2 TB = 2000 GB
     = 2 000 000 MB × 8
     = 16 000 000 Mbit
```

**Berechnung der Zeit:**
```
Zeit = Datenmenge / Datenrate
Zeit = 16 000 000 mBit / 200 mBit/s
Zeit = 80 000 Sekunden
```

**Antwort:** Die Zeit beträgt 80 000 Sekunden (ca. 22,2 Stunden)

---

### b) Datenmenge bei gegebener Zeit und Datenrate berechnen

**Gegeben:**
- Zeit = 40 Stunden
- Datenrate = 700 mBit/s

**Umrechnung:**
```
40 Stunden = 144 000 Sekunden
```

**Berechnung:**
```
Datenmenge = Zeit × Datenrate
Datenmenge = 144 000 sek × 700 mBit/s
          = 100 800 000 Mbit
          = 28 800 000 Mbit
          = 3 600 000 MB
          = 3 600 GB
          = 3,6 TB
```

**Antwort:** Die Datenmenge beträgt 3,6 TB

---

## Aufgabe 2 (aus evp.pdf)

### Downstream und Upstream berechnen

**Gegeben:**
- Datenmenge = 8 TiB (roh) → Downstream
- Datenmenge = 2 TiB (fertig) → Upstream
- Zeit = 2 h (beide)
- Zeit = 7200 Sekunden

**Formel:**
```
Datenrate = Datenmenge / Zeit
```

---

### Downstream berechnen:

**Umrechnung:**
```
8 TiB = 8 × 2⁴⁰ Byte
      = 8 796 093 022 208 Byte × 8
      = 70 368 744 177 664 Bit
```

**Berechnung:**
```
Datenrate = 70 368 744 177 664 Bit / 7200 sek
          = 9 773 436 691 bit/s
          = 9 773 436 kbit/s
          = 9 773 Mbit/s
          ≈ 9 Gbit/s
```

**Antwort:** Downstream = 9 773 Mbit/s (≈ 9 Gbit/s)

**Hinweis:** S. Anbieter hat ausreichende Werte

---

### Upstream berechnen:

**Umrechnung:**
```
2 TiB = 2 × 2⁴⁰ Byte
      = 2 199 023 255 552 Byte × 8
      = 17 592 186 044 416 Bit
```

**Berechnung:**
```
Datenrate = 17 592 186 044 446 Bit / 7200 sek
          = 2 443 359 172 bit/s
          = 2 443 359 kbit/s
          = 2 443 Mbit/s
          ≈ 2,5 Gbit/s
```

**Antwort:** Upstream = 2 443 Mbit/s (≈ 2,5 Gbit/s)

**Hinweis:** S. Anbieter hat ausreichende Werte

---

**Fazit:** Die beiden schnellsten Leitungen würden funktionieren!

---

## Beispielrechnung: Upload bei 500 Mbit/s

**Gegeben:**
- Datenmenge = 5 GB = 5000 MB
- Datenrate = 500 Mbit/s

**Umrechnung:**
```
5 GB = 5000 MB × 8
     = 40 000 mBits
```

**Berechnung:**
```
Zeit = 5 GB / 500 mBit/s
     = 40 000 mBits / 500 mBits
     = 80 Sekunden
```

**Antwort:** Upload dauert 80 Sekunden

---

## Wichtige Formeln:

### 1. Datenrate berechnen:
```
Datenrate = Datenmenge / Zeit
```

### 2. Zeit berechnen:
```
Zeit = Datenmenge / Datenrate
```

### 3. Datenmenge berechnen:
```
Datenmenge = Zeit × Datenrate
```

### 4. Umrechnung Byte zu Bit:
```
Bit = Byte × 8
```

### 5. Einheiten umrechnen:
```
SI-System (Basis 1000):
1 KB = 1 000 Byte
1 MB = 1 000 KB = 1 000 000 Byte
1 GB = 1 000 MB = 1 000 000 000 Byte
1 TB = 1 000 GB = 1 000 000 000 000 Byte

Binär-System (Basis 1024):
1 KiB = 1 024 Byte
1 MiB = 1 024 KiB = 1 048 576 Byte
1 GiB = 1 024 MiB = 1 073 741 824 Byte
1 TiB = 1 024 GiB = 1 099 511 627 776 Byte
```