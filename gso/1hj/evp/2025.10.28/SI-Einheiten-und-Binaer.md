# SI-Einheiten und Binärsystem - Erklärung

## SI-Einheiten (Internationale Standardeinheiten)

Die SI-Einheiten basieren auf dem **Dezimalsystem (Basis 10)** und verwenden Potenzen von 1000.

### Übersicht der Einheiten:

| Einheit | Wert | Potenz | Bedeutung |
|---------|------|--------|-----------|
| **kilo** | 1.000 | 10³ | Tausend |
| **Mega** | 1.000.000 | 10⁶ | Million |
| **Giga** | 1.000.000.000 | 10⁹ | Milliarde |
| **Tera** | 1.000.000.000.000 | 10¹² | Billion |

### Beispiel:
- 1 Kilobyte (KB) = 1.000 Byte
- 1 Megabyte (MB) = 1.000 KB = 1.000.000 Byte
- 1 Gigabyte (GB) = 1.000 MB = 1.000.000.000 Byte
- 1 Terabyte (TB) = 1.000 GB = 1.000.000.000.000 Byte

---

## Binärsystem (für Computer/Informatik)

Computer arbeiten mit dem **Binärsystem (Basis 2)** - also Potenzen von 2.

### Grundeinheiten:

| Symbol | Bedeutung | Wert |
|--------|-----------|------|
| **Bit** | Kleinste Einheit | 0 oder 1 |
| **Byte** | 8 Bit | 8 Bit |

### Binäre Präfixe (IEC-Standard):

Die **echten** binären Einheiten verwenden Potenzen von 2 (Basis 1024):

| Einheit | Wert | Potenz | Bedeutung |
|---------|------|--------|-----------|
| **Kibi** (KiB) | 1.024 | 2¹⁰ | Kibibyte |
| **Mebi** (MiB) | 1.048.576 | 2²⁰ | Mebibyte |
| **Gibi** (GiB) | 1.073.741.824 | 2³⁰ | Gibibyte |
| **Tebi** (TiB) | 1.099.511.627.776 | 2⁴⁰ | Tebibyte |

### Speichergrößen im Binärsystem:

```
1 Byte    = 8 Bit
1 KiB     = 1.024 Byte  (2¹⁰)
1 MiB     = 1.024 KiB   (2²⁰ Byte)
1 GiB     = 1.024 MiB   (2³⁰ Byte)
1 TiB     = 1.024 GiB   (2⁴⁰ Byte)
```

---

## Der wichtige Unterschied!

### SI vs. Binär:

- **SI-Einheiten** (KB, MB, GB, TB): Basis 1.000 (Dezimal)
- **Binär-Einheiten** (KiB, MiB, GiB, TiB): Basis 1.024 (Binär)

**Beispiel:**
- 1 GB (SI) = 1.000.000.000 Byte
- 1 GiB (Binär) = 1.073.741.824 Byte
- **Unterschied:** ~7,4% mehr bei GiB!

---

## Vergleichs-Pyramide (Gemeinsamer Nenner: Byte)

```
                                    BYTE (Gemeinsamer Nenner)
                                           |
                    ┌──────────────────────┴──────────────────────┐
                    |                                              |
              SI-EINHEITEN                                  BINÄR-EINHEITEN
            (Basis 1.000)                                    (Basis 1.024)
                    |                                              |
         ┌──────────┼──────────┬──────────┐            ┌──────────┼──────────┬──────────┐
         |          |          |          |            |          |          |          |
        KB         MB         GB         TB           KiB        MiB        GiB        TiB
         |          |          |          |            |          |          |          |
    1.000 B    1.000 KB   1.000 MB   1.000 GB      1.024 B    1.024 KiB  1.024 MiB  1.024 GiB
         |          |          |          |            |          |          |          |
    10³ Byte   10⁶ Byte   10⁹ Byte  10¹² Byte     2¹⁰ Byte   2²⁰ Byte   2³⁰ Byte   2⁴⁰ Byte
```

### Direkter Vergleich in Byte:

| Einheit | SI (Dezimal) | Binär (IEC) | Unterschied |
|---------|--------------|-------------|-------------|
| **Kilo** | 1 KB = 1.000 Byte | 1 KiB = 1.024 Byte | +2,4% |
| **Mega** | 1 MB = 1.000.000 Byte | 1 MiB = 1.048.576 Byte | +4,9% |
| **Giga** | 1 GB = 1.000.000.000 Byte | 1 GiB = 1.073.741.824 Byte | +7,4% |
| **Tera** | 1 TB = 1.000.000.000.000 Byte | 1 TiB = 1.099.511.627.776 Byte | +10,0% |

**Wichtig:** Je größer die Einheit, desto größer wird der Unterschied zwischen SI und Binär!

---

## Zusammenfassung:

- **SI-Einheiten** (dezimal): Basis 10, Schritte von 1.000
  - kilo (10³), Mega (10⁶), Giga (10⁹), Tera (10¹²)

- **Binärsystem** (Computer): Basis 2, Schritte von 1.024
  - 1 Byte = 8 Bit
  - Potenzen von 2 (2¹⁰, 2²⁰, 2³⁰, 2⁴⁰)

- **Umrechnung**: Immer beachten, ob SI-Einheiten (1.000) oder binäre Einheiten (1.024) gemeint sind!