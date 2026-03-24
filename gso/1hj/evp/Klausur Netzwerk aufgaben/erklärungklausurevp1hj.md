# Erklärung Netzwerk-Begriffe - Klausur EvP 1. Halbjahr

## Netzmaske

Die Netzmaske gibt an, welcher Teil einer IP-Adresse das **Netzwerk** identifiziert und welcher Teil **frei verfügbar** ist.

**Wichtig:** Der "freie" Teil kann für verschiedene Zwecke genutzt werden:
- Nur für Rechner/Systeme
- ODER aufgeteilt in: Abteilung, Etage, Rechner (wie in Aufgabe 4)

**Schreibweisen:**
- CIDR-Notation: `/24`
- Dezimal: `255.255.255.0`

**Gängige Netzmasken:**

| CIDR | Dezimal | Netz-Oktette | Freie Oktette | Max. Adressen |
|------|---------|--------------|---------------|---------------|
| /8   | 255.0.0.0 | 1 | 3 | 16.777.214 |
| /16  | 255.255.0.0 | 2 | 2 | 65.534 |
| /24  | 255.255.255.0 | 3 | 1 | 254 |

**Beispiel aus Aufgabe 4:**

Anforderung: Abteilung, Etage UND Rechner sollen in der IP sichtbar sein = **3 freie Oktette nötig** = `/8`!

```
10      .  12     .   3     .  43
│          │          │        │
Netzwerk   Abteilung  Etage    Rechner/System
(1 Okt.)   ◄────── 3 freie Oktette ──────►
```

- Privater Adressbereich: `10.0.0.0/8` (1 Oktett Netzwerk, 3 frei)
- Subnetze bekommen `/16` (jede Abteilung = eigenes Subnetz, z.B. `10.12.0.0/16`)

---

## Subnetze

Ein **Subnetz** ist ein abgetrennter Bereich innerhalb eines größeren Netzwerks. Geräte im selben Subnetz können direkt miteinander kommunizieren. Für Kommunikation zwischen verschiedenen Subnetzen braucht man ein Gateway/Router.

### Beispiel: Firma mit 4 Abteilungen

**Ohne Subnetze:** Alle 200 Rechner im selben Netzwerk - chaotisch, unsicher, langsam.

**Mit Subnetzen:** Jede Abteilung bekommt ihr eigenes "Mini-Netzwerk":

```
Firmennetzwerk: 172.16.0.0/16
        │
        ├── Subnetz 1 (Buchhaltung):  172.16.1.0/24  → Rechner: 172.16.1.1 - 172.16.1.50
        ├── Subnetz 2 (Vertrieb):     172.16.2.0/24  → Rechner: 172.16.2.1 - 172.16.2.50
        ├── Subnetz 3 (IT):           172.16.3.0/24  → Rechner: 172.16.3.1 - 172.16.3.50
        └── Subnetz 4 (Marketing):    172.16.4.0/24  → Rechner: 172.16.4.1 - 172.16.4.50
```

**Was ändert sich im Subnetz?**
- Das 3. Oktett! (1, 2, 3, 4...)
- Jedes Subnetz hat eigene Netzwerk-, Broadcast- und Gateway-Adresse

### Beispiel Aufgabe 4: Subnetze nach Abteilungen

```
Firmennetzwerk: 10.0.0.0/8
        │
        ├── Abteilung 1:   10.1.0.0/16
        ├── Abteilung 2:   10.2.0.0/16
        ├── ...
        └── Abteilung 12:  10.12.0.0/16  → Rechner in Etage 3: 10.12.3.1 - 10.12.3.150
```

Hier ändert sich das **2. Oktett** pro Subnetz (Abteilung).

---

## Subnetz vs. Subnetzmaske - Der Unterschied

| Begriff | Was ist das? | Beispiel |
|---------|--------------|----------|
| **Subnetz** | Ein konkretes Netzwerk mit Adressen | `172.16.1.0/24` |
| **Subnetzmaske** | Die "Schablone", die angibt wie groß das Subnetz ist | `255.255.255.0` oder `/24` |

### Einfach erklärt:

- **Subnetz** = "In welchem Netzwerk bin ich?" → `172.16.1.0`
- **Subnetzmaske** = "Wie groß ist dieses Netzwerk?" → `255.255.255.0`

### Die Subnetzmaske bestimmt die Größe:

```
255.255.255.0  = /24 = 254 Hosts möglich   (1 Oktett frei)
255.255.0.0    = /16 = 65.534 Hosts möglich (2 Oktette frei)
255.0.0.0      = /8  = 16 Mio. Hosts möglich (3 Oktette frei)
```

**Wo 255 steht = Netzwerk-Teil (fest)**
**Wo 0 steht = Host-Teil (frei für Geräte)**

### Wann welche Subnetzmaske?

| Anforderung | Subnetzmaske | Warum? |
|-------------|--------------|--------|
| Max. 254 Rechner, keine weitere Unterteilung | `255.255.255.0` (/24) | 1 Oktett reicht für 254 Adressen |
| Brauche Etage + Rechner sichtbar | `255.255.0.0` (/16) | 2 Oktette frei (Etage + Host) |
| Brauche Abteilung + Etage + Rechner | `255.0.0.0` (/8) | 3 Oktette frei |

### Beispiel Aufgabe 5:

```
Anforderung: 4 Subnetze, max. 50 Rechner pro Subnetz
                                    │
                                    ▼
Subnetzmaske: 255.255.255.0 (/24) reicht! (254 > 50)
                                    │
                                    ▼
Subnetze:     172.16.1.0/24, 172.16.2.0/24, 172.16.3.0/24, 172.16.4.0/24
```

### Beispiel Aufgabe 4:

```
Anforderung: Abteilung, Etage, Rechner sollen sichtbar sein
                                    │
                                    ▼
Brauche 3 freie Oktette → Adressbereich mit /8 (255.0.0.0)
                                    │
                                    ▼
Subnetze pro Abteilung: /16 (255.255.0.0)
    → 10.12.0.0/16 = Abteilung 12, Oktett 3+4 frei für Etage+Host
```

---

## "Welche Netzmaske erhalten die Subnetze?"

Diese Frage bedeutet: **Wie groß sollen die einzelnen Subnetze sein?**

Die Wahl hängt davon ab, wie viele Hosts (Geräte) im Subnetz benötigt werden:

| Benötigte Hosts | Passende Netzmaske | Verfügbare Hosts |
|-----------------|-------------------|------------------|
| bis 254 | /24 | 254 |
| bis 65.534 | /16 | 65.534 |
| bis 16 Mio. | /8 | 16.777.214 |

**Beispiel Aufgabe 5:**
- Anforderung: max. 50 Systeme pro Abteilung
- Lösung: `/24` (bietet 254 Hosts - mehr als genug für 50)

**Beispiel Aufgabe 4:**
- Anforderung: max. 150 Systeme, plus Etagen- und Abteilungsinfo im Schema
- Lösung: `/16` für die Subnetze (3. Oktett = Etage, 4. Oktett = Host)

---

## Netzwerkadresse

Die **Netzwerkadresse** ist die **erste Adresse** eines Subnetzes. Sie identifiziert das Netzwerk selbst und kann **nicht** an Geräte vergeben werden.

**Berechnung:** Alle Host-Bits auf 0 setzen.

**Beispiele:**

| Subnetz | Netzwerkadresse |
|---------|-----------------|
| 172.16.1.0/24 | `172.16.1.0` |
| 172.16.2.0/24 | `172.16.2.0` |
| 192.168.0.0/24 | `192.168.0.0` |
| 10.12.0.0/16 | `10.12.0.0` |

---

## Broadcastadresse

Die **Broadcastadresse** ist die **letzte Adresse** eines Subnetzes. Sie wird verwendet, um Nachrichten an **alle Geräte** im Netzwerk gleichzeitig zu senden. Sie kann **nicht** an einzelne Geräte vergeben werden.

**Berechnung:** Alle Host-Bits auf 1 setzen.

**Beispiele:**

| Subnetz | Broadcastadresse |
|---------|------------------|
| 172.16.1.0/24 | `172.16.1.255` |
| 172.16.2.0/24 | `172.16.2.255` |
| 192.168.0.0/24 | `192.168.0.255` |
| 10.12.0.0/16 | `10.12.255.255` |

**Beispiel aus Aufgabe 4d:**
- Abteilung 12, also Subnetz `10.12.0.0/16`
- Broadcastadresse: `10.12.255.255`

---

## Max. Adressbereich für Rechner

Der **Adressbereich für Rechner** sind die IP-Adressen, die tatsächlich an Geräte (PCs, Server, Drucker etc.) vergeben werden können.

### Theoretischer vs. praktischer Bereich

**Theoretisch nutzbar (bei /24):**
- Von `.1` bis `.254` (254 Adressen)
- `.0` = Netzwerkadresse (nicht nutzbar)
- `.255` = Broadcast (nicht nutzbar)

**Praktisch vergeben:**
- Hängt von der **Aufgabenstellung** ab!
- Wenn nur 50 Rechner benötigt werden, reicht `.1` bis `.50`
- Das Gateway braucht auch eine Adresse (meist `.1` oder `.254`)

### Beispiele

**Aufgabe 5 - 50 Rechner benötigt:**

| Gateway-Position | Rechner-Bereich |
|------------------|-----------------|
| Gateway auf `.254` | `.1` bis `.50` |
| Gateway auf `.1` | `.2` bis `.51` |

**Aufgabe 4 - 150 Rechner benötigt:**
- 4. Oktett für Hosts: `1-150`

### Wichtig zu verstehen:

| Begriff | Bedeutung |
|---------|-----------|
| **Theoretisch nutzbar** | Alle Adressen zwischen Netzwerk- und Broadcastadresse (bei /24: 1-254) |
| **Praktisch vergeben** | Nur so viele wie laut Aufgabe benötigt werden |
| **Nicht vergessen** | Gateway-Adresse abziehen! |

---

## Gateway-Adresse

Das **Gateway** (auch: Default Gateway, Router) ist das Gerät, das den Datenverkehr zwischen verschiedenen Netzwerken weiterleitet. Es ist der "Ausgang" aus dem lokalen Netzwerk ins Internet oder zu anderen Subnetzen.

### Typische Positionen

| Position | Gateway-Adresse | Rechner ab |
|----------|-----------------|------------|
| Am Ende | `.254` | `.1` |
| Am Anfang | `.1` | `.2` |

Beide Varianten sind korrekt - Hauptsache **konsistent** und das Gateway liegt **nicht** im Rechner-Adressbereich!

**Beispiele aus Aufgabe 5:**

| Subnetz | Gateway (am Ende) |
|---------|-------------------|
| 172.16.1.0/24 | `172.16.1.254` |
| 172.16.2.0/24 | `172.16.2.254` |
| 172.16.3.0/24 | `172.16.3.254` |
| 172.16.4.0/24 | `172.16.4.254` |

---

## Private Adressbereiche (Bonus)

Für interne Netzwerke werden **private IP-Adressen** verwendet, die nicht im Internet geroutet werden:

| Klasse | Bereich | CIDR | Typische Verwendung |
|--------|---------|------|---------------------|
| A | 10.0.0.0 - 10.255.255.255 | /8 | Große Unternehmen |
| B | 172.16.0.0 - 172.31.255.255 | /12 | Mittlere Netzwerke |
| C | 192.168.0.0 - 192.168.255.255 | /16 | Heimnetzwerke, kleine Firmen |

**Aufgabe 4:** `10.0.0.0/8` (Klasse A) - weil viele Abteilungen und Etagen
**Aufgabe 5:** `172.16.0.0/16` (Klasse B) - für 4 Subnetze ausreichend

---

## Zusammenfassung: Schema für Subnetz-Tabelle

Bei einer /24 Netzmaske:

```
Netzwerkadresse:     x.x.x.0      (erste Adresse, nicht nutzbar)
Gateway:             x.x.x.1      ODER x.x.x.254
Rechner:             x.x.x.1-254  (minus Gateway, minus was nicht gebraucht wird)
Broadcastadresse:    x.x.x.255    (letzte Adresse, nicht nutzbar)
```

**Checkliste für Klausur:**
1. Netzwerkadresse = erstes Oktett auf `.0`
2. Broadcastadresse = letztes Oktett auf `.255` (bei /24)
3. Gateway = `.1` oder `.254` (konsistent bleiben!)
4. Rechner = restlicher Bereich, nur so viele wie benötigt