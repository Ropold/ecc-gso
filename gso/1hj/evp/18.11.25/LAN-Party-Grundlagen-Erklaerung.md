# LAN-Party Grundlagen - IPv4-Adressierung erklärt

## Was ist eine IP-Adresse?

Eine IP-Adresse ist wie eine Hausnummer im Internet oder in einem lokalen Netzwerk. Jedes Gerät (Computer, Smartphone, Drucker) braucht eine eindeutige Adresse, damit Datenpakete zum richtigen Empfänger gelangen.

### Aufbau einer IPv4-Adresse
- Eine IPv4-Adresse besteht aus 32 Bits (Einsen und Nullen)
- Wir schreiben sie als 4 Zahlen, getrennt durch Punkte
- Jede Zahl steht für 8 Bits (ein Oktett) und kann von 0 bis 255 gehen
- **Beispiel:** `192.168.1.100`

#### Was sind 32 Bits? - Detaillierte Erklärung

Ein Bit ist die kleinste Informationseinheit in der Informatik - es kann nur `0` oder `1` sein.
32 Bits bedeutet: 32 solcher Einsen und Nullen hintereinander.

**Beispiel einer kompletten IPv4-Adresse in Binär:**
```
11000000.10101000.00000001.01100100
```

#### Warum schreiben wir sie als 4 Zahlen?

Weil 32 Einsen und Nullen schwer zu lesen sind! Deshalb teilen wir sie in **4 Blöcke à 8 Bits** auf.

**Wie kommen wir von Binär zu Dezimal?**

Jeder 8-Bit-Block wird in eine Dezimalzahl umgewandelt:

**Beispiel - erster Block: `11000000`**

```
Position:  1   1   0   0   0   0   0   0
Wert:    128  64  32  16   8   4   2   1
         ─────────────────────────────────
         128+ 64+ 0 + 0 + 0 + 0 + 0 + 0 = 192
```

**Die komplette Umwandlung:**
```
11000000 . 10101000 . 00000001 . 01100100
   ↓          ↓          ↓          ↓
  192    .   168    .    1     .   100
```

#### Warum 0 bis 255?

Mit 8 Bits kannst du genau 2^8 = 256 verschiedene Werte darstellen.
Da wir bei 0 anfangen zu zählen: **0 bis 255**

**Beispiele:**
- `00000000` = 0 (kleinste Zahl)
- `11111111` = 255 (größte Zahl)
- `10000000` = 128 (mittlerer Bereich)

#### Zusammenfassung IPv4-Aufbau

IPv4-Adresse `192.168.1.100` bedeutet eigentlich:
```
Dezimal:  192        . 168        . 1          . 100
Binär:    11000000   . 10101000   . 00000001   . 01100100
          └─ 8 Bit ─┘  └─ 8 Bit ─┘  └─ 8 Bit ─┘  └─ 8 Bit ─┘
                            32 Bits insgesamt
```

Deshalb gibt es insgesamt **2^32 = 4.294.967.296** mögliche IPv4-Adressen!

## Die Netzmaske - Wer gehört zu wem?

Die Netzmaske teilt die IP-Adresse in zwei Teile auf:

1. **Netzwerkteil** - Welches Netzwerk ist das?
2. **Hostteil** - Welcher Rechner im Netzwerk?

### Wie funktioniert das?
- In der Netzmaske stehen links nur Einsen (1), rechts nur Nullen (0)
- Die Einsen markieren den Netzwerkteil
- Die Nullen markieren den Hostteil

**Beispiel:**
- IP-Adresse: `192.168.1.100`
- Netzmaske: `255.255.255.0` (oder `/24`)
- Netzwerkteil: `192.168.1` (bleibt für alle gleich)
- Hostteil: `100` (unterscheidet die einzelnen Geräte)

### CIDR-Schreibweise
Statt `255.255.255.0` kann man auch `/24` schreiben. Die Zahl gibt an, wie viele Bits auf 1 gesetzt sind.

- `/24` = 24 Einsen = `255.255.255.0`
- `/16` = 16 Einsen = `255.255.0.0`
- `/8` = 8 Einsen = `255.0.0.0`

## Besondere Adressen in jedem Netzwerk

### Netzwerkadresse
- Die **niedrigste** Adresse im Netzwerk
- Alle Host-Bits sind auf 0 gesetzt
- Adressiert das gesamte Netzwerk
- **Beispiel:** `192.168.1.0/24` - das ist die Netzwerkadresse
- Diese Adresse kann NICHT für einen Computer verwendet werden

### Broadcast-Adresse
- Die **höchste** Adresse im Netzwerk
- Alle Host-Bits sind auf 1 gesetzt
- Sendet an ALLE Geräte im Netzwerk gleichzeitig
- **Beispiel:** `192.168.1.255` (bei Netzwerk `192.168.1.0/24`)
- Diese Adresse kann NICHT für einen Computer verwendet werden

### Nutzbare Adressen berechnen
Wenn du wissen willst, wie viele Computer du in einem Netzwerk anschließen kannst:

**Formel:** 2ⁿ - 2

- **n** = Anzahl der Bits im Hostteil
- **-2** weil Netzwerk- und Broadcast-Adresse nicht nutzbar sind

**Beispiel für /24:**
- 8 Bits für Hosts (32 - 24 = 8)
- 2⁸ = 256
- 256 - 2 = **254 nutzbare Adressen**
- Von `192.168.1.1` bis `192.168.1.254`

## Adressierungsarten - Wie kommunizieren Geräte?

### Unicast
- Ein Gerät sendet an EIN bestimmtes Gerät
- Wie ein Brief mit genauer Adresse
- **Beispiel:** Dein PC sendet eine Anfrage an einen Webserver

### Broadcast
- Ein Gerät sendet an ALLE Geräte im Netzwerk
- Wie eine Durchsage über Lautsprecher
- **Beispiel:** `192.168.1.255` - alle Geräte im Netz 192.168.1.0/24 empfangen die Nachricht

### Multicast
- Ein Gerät sendet an eine GRUPPE von Geräten
- Wie ein Newsletter an Abonnenten
- **Beispiel:** Video-Streaming an mehrere Zuschauer gleichzeitig

### Anycast
- Ein Gerät sendet an EINEN aus einer Gruppe
- Meistens wird der nächstgelegene oder beste ausgewählt
- **Beispiel:** DNS-Server - es antwortet der schnellste verfügbare

## Netzklassen (historisch)

Früher wurden IP-Adressen in Klassen eingeteilt. Heute nicht mehr wirklich relevant, aber die Begriffe werden noch verwendet:

| Klasse | Netzmaske | Adressbereich | Verwendung |
|--------|-----------|---------------|------------|
| A | /8 (255.0.0.0) | 1.x.x.x - 127.x.x.x | Sehr große Netze |
| B | /16 (255.255.0.0) | 128.x.x.x - 191.x.x.x | Mittelgroße Netze |
| C | /24 (255.255.255.0) | 192.x.x.x - 223.x.x.x | Kleine Netze |
| D | - | 224.x.x.x - 239.x.x.x | Multicast |
| E | - | ab 240.x.x.x | Reserviert/nicht benutzt |

## Private IP-Adressen - Für dein Heimnetzwerk

Diese Adressen sind für private Netzwerke reserviert und werden im öffentlichen Internet NICHT weitergeleitet:

### Die drei privaten Bereiche:
1. **10.0.0.0/8**
   - Von 10.0.0.0 bis 10.255.255.255
   - Sehr großer Bereich
   - Oft in großen Firmen

2. **172.16.0.0/12**
   - Von 172.16.0.0 bis 172.31.255.255
   - Mittlerer Bereich
   - Oft in mittleren Firmen

3. **192.168.0.0/16**
   - Von 192.168.0.0 bis 192.168.255.255
   - Kleinerer Bereich
   - Typisch für Heimnetzwerke (z.B. FritzBox: 192.168.178.x)

**Vorteil:** Jeder kann diese Adressen in seinem privaten Netz verwenden. Sie kollidieren nicht, weil sie nicht im Internet geroutet werden.

## Spezielle Adressbereiche

### 127.0.0.0/8 - Loopback
- Der Computer spricht mit sich selbst
- **127.0.0.1** = "localhost"
- Nützlich zum Testen von Netzwerkprogrammen
- **Beispiel:** Wenn du einen Webserver auf deinem PC testest: `http://127.0.0.1`

### 169.254.0.0/16 - APIPA
- **A**utomatic **P**rivate **IP** **A**ddressing
- Wird automatisch vergeben, wenn kein DHCP-Server gefunden wird
- Zeigt oft ein Problem an: "Keine Netzwerkverbindung zum Router"

### 192.0.2.0/24 - Dokumentation
- Nur für Beispiele in Handbüchern und Dokumentationen
- Diese Adressen funktionieren nicht wirklich

## Praktisches Beispiel: LAN-Party einrichten

Stell dir vor, du richtest eine LAN-Party mit 20 Freunden ein:

1. **Netzwerk wählen:** `192.168.100.0/24`
   - Netzwerkadresse: `192.168.100.0`
   - Broadcast: `192.168.100.255`
   - Nutzbare Adressen: `192.168.100.1` bis `192.168.100.254` (254 Stück)

2. **Router/Gateway:** `192.168.100.1`

3. **PCs vergeben:**
   - PC 1: `192.168.100.10`
   - PC 2: `192.168.100.11`
   - PC 3: `192.168.100.12`
   - usw.

4. **Alle mit Netzmaske:** `255.255.255.0` oder `/24`

Jetzt können alle miteinander spielen! Die Computer sind im selben Netzwerk und können direkt kommunizieren.

## Zusammenfassung

- **IP-Adresse** = Eindeutige Adresse für jedes Gerät (z.B. 192.168.1.100)
- **Netzmaske** = Teilt Netzwerk- und Hostteil (z.B. 255.255.255.0 oder /24)
- **Netzwerkadresse** = Niedrigste Adresse, adressiert das ganze Netz
- **Broadcast** = Höchste Adresse, sendet an alle Geräte
- **Private Adressen** = 10.x.x.x, 172.16-31.x.x, 192.168.x.x für lokale Netze
- **Loopback** = 127.0.0.1 für lokale Tests
- **Nutzbare Hosts** = 2ⁿ - 2 (n = Anzahl Host-Bits)