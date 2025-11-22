# LAN-Party Plannung - Aufgabenloesung

## Aufgabenstellung

Nachdem der grundlegende Aufbau von IPv4-Adressen nun bekannt ist, kann die eigentliche Planung der LAN-Party beginnen. Zum reibungslosen Ablauf wuenscht die Geschaeftsfuehrung, das Hand-Zettel erstellt werden, nach denen jeder Teilnehmer seine IP-Konfiguration selbstaendig (manuell) durchfuehren kann.

**Anforderungen:**
- Bis zu 10 unterschiedliche Spiele
- Maximal 100 Teilnehmer pro Spiel
- Client-Betriebssysteme: Windows und Linux
- Zielgruppe: Technisch nicht versierte User

---

## Frage 1: Welche Informationen muessen auf den Handzetteln vorhanden sein?

### Notwendige technische Informationen

Jeder Handzettel muss folgende IP-Konfigurationsdaten enthalten:

#### 1. IP-Adresse
- **Beispiel:** `192.168.10.15`
- **Erklaerung fuer User:** "Deine eindeutige Netzwerkadresse fuer dieses Spiel"
- Jeder Teilnehmer braucht eine EIGENE, eindeutige IP-Adresse

#### 2. Subnetzmaske (Subnet Mask)
- **Beispiel:** `255.255.255.0` oder `/24`
- **Erklaerung fuer User:** "Definiert dein lokales Netzwerk"
- Fuer alle Teilnehmer eines Spiels IDENTISCH

#### 3. Standard-Gateway (Default Gateway)
- **Beispiel:** `192.168.10.1`
- **Erklaerung fuer User:** "Adresse des Routers/Ausgang ins Internet"
- Fuer alle Teilnehmer eines Spiels IDENTISCH

#### 4. DNS-Server (optional, aber empfohlen)
- **Beispiel:** `192.168.10.1` oder `8.8.8.8` (Google DNS)
- **Erklaerung fuer User:** "Uebersetzt Webseiten-Namen in IP-Adressen"
- Wichtig fuer Internetverbindung und Updates

---

## Beispiel-Handzettel fuer Spiel 1

### Deine IP-Konfiguration fuer "Counter-Strike 2"

**WICHTIG:** Jeder Spieler hat unterschiedliche Werte! Verwende NUR die Werte auf DEINEM Zettel!

#### Deine Netzwerk-Einstellungen:
```
IP-Adresse:      192.168.10.15
Subnetzmaske:    255.255.255.0
Standard-Gateway: 192.168.10.1
DNS-Server:      192.168.10.1
```

---

## Anleitung fuer Windows

### Schritt-fuer-Schritt fuer Windows 10/11:

1. **Oeffne die Netzwerkeinstellungen**
   - Druecke `Windows-Taste + R`
   - Tippe ein: `ncpa.cpl`
   - Druecke `Enter`

2. **Netzwerkadapter auswaehlen**
   - Rechtsklick auf deine Ethernet/LAN-Verbindung
   - Klicke auf "Eigenschaften"

3. **IPv4-Einstellungen oeffnen**
   - Scrolle runter und waehle: "Internetprotokoll Version 4 (TCP/IPv4)"
   - Klicke auf "Eigenschaften"

4. **IP-Adresse eintragen**
   - Waehle: "Folgende IP-Adresse verwenden"
   - Trage ein:
     - **IP-Adresse:** `192.168.10.15` <- DEINE Adresse vom Zettel!
     - **Subnetzmaske:** `255.255.255.0`
     - **Standardgateway:** `192.168.10.1`

5. **DNS eintragen**
   - Waehle: "Folgende DNS-Serveradressen verwenden"
   - Trage ein:
     - **Bevorzugter DNS-Server:** `192.168.10.1`

6. **Speichern**
   - Klicke auf "OK"
   - Nochmal "OK" im naechsten Fenster

7. **Testen**
   - Oeffne die Eingabeaufforderung (CMD)
   - Tippe: `ping 192.168.10.1`
   - Du solltest Antworten sehen!

---

## Anleitung fuer Linux

### Schritt-fuer-Schritt fuer Ubuntu/Linux Mint (GUI):

1. **Netzwerkeinstellungen oeffnen**
   - Klicke auf das Netzwerk-Symbol oben rechts
   - Waehle "Einstellungen" oder "Netzwerkverbindungen"

2. **Kabelverbindung bearbeiten**
   - Waehle deine Ethernet/Kabelverbindung
   - Klicke auf das Zahnrad-Symbol oder "Bearbeiten"

3. **IPv4-Einstellungen**
   - Gehe zum Tab "IPv4"
   - Methode: Aendere auf "Manuell"

4. **Adresse hinzufuegen**
   - Klicke auf "Hinzufuegen" unter Adressen
   - Trage ein:
     - **Adresse:** `192.168.10.15` <- DEINE Adresse vom Zettel!
     - **Netzmaske:** `255.255.255.0` oder `24`
     - **Gateway:** `192.168.10.1`

5. **DNS eintragen**
   - Im Feld "DNS-Server": `192.168.10.1`

6. **Speichern und Anwenden**
   - Klicke auf "Speichern" oder "Anwenden"
   - Schalte die Verbindung aus und wieder ein

7. **Testen**
   - Oeffne ein Terminal
   - Tippe: `ping 192.168.10.1`
   - Du solltest Antworten sehen!

### Fuer erfahrene Linux-User (Terminal):

```bash
# Netzwerk-Interface anzeigen (z.B. eth0, enp0s3)
ip addr

# IP-Konfiguration setzen
sudo ip addr add 192.168.10.15/24 dev eth0
sudo ip route add default via 192.168.10.1

# DNS setzen (in /etc/resolv.conf)
echo "nameserver 192.168.10.1" | sudo tee /etc/resolv.conf

# Testen
ping -c 4 192.168.10.1
```

---

## Netzwerkplanung fuer 10 Spiele

Da bis zu 10 verschiedene Spiele mit jeweils maximal 100 Teilnehmern geplant sind:

### Empfohlene Netzwerk-Aufteilung:

| Spiel | Netzwerk | IP-Bereich | Gateway | Verfuegbare IPs |
|-------|----------|------------|---------|----------------|
| Spiel 1 | 192.168.10.0/24 | 192.168.10.2 - 192.168.10.254 | 192.168.10.1 | 253 |
| Spiel 2 | 192.168.20.0/24 | 192.168.20.2 - 192.168.20.254 | 192.168.20.1 | 253 |
| Spiel 3 | 192.168.30.0/24 | 192.168.30.2 - 192.168.30.254 | 192.168.30.1 | 253 |
| Spiel 4 | 192.168.40.0/24 | 192.168.40.2 - 192.168.40.254 | 192.168.40.1 | 253 |
| Spiel 5 | 192.168.50.0/24 | 192.168.50.2 - 192.168.50.254 | 192.168.50.1 | 253 |
| Spiel 6 | 192.168.60.0/24 | 192.168.60.2 - 192.168.60.254 | 192.168.60.1 | 253 |
| Spiel 7 | 192.168.70.0/24 | 192.168.70.2 - 192.168.70.254 | 192.168.70.1 | 253 |
| Spiel 8 | 192.168.80.0/24 | 192.168.80.2 - 192.168.80.254 | 192.168.80.1 | 253 |
| Spiel 9 | 192.168.90.0/24 | 192.168.90.2 - 192.168.90.254 | 192.168.90.1 | 253 |
| Spiel 10 | 192.168.100.0/24 | 192.168.100.2 - 192.168.100.254 | 192.168.100.1 | 253 |

**Warum /24 (255.255.255.0)?**
- Bietet 253 nutzbare IP-Adressen pro Spiel
- Reicht fuer maximal 100 Teilnehmer pro Spiel
- Einfach zu merken und zu konfigurieren
- Klare Trennung zwischen den Spielen

---

## Zusammenfassung: Was MUSS auf dem Handzettel stehen?

### Minimale Informationen (technisch):
1. **IP-Adresse** (eindeutig fuer jeden Teilnehmer)
2. **Subnetzmaske** (fuer alle gleich: 255.255.255.0)
3. **Standard-Gateway** (fuer alle gleich: z.B. 192.168.10.1)
4. **DNS-Server** (optional, aber empfohlen)

### Zusaetzliche Informationen (fuer nicht-technische User):
1. **Spielname** (damit klar ist, wofuer die Konfiguration ist)
2. **Schritt-fuer-Schritt Anleitung** fuer Windows UND Linux
3. **Test-Anleitung** (Ping-Befehl)
4. **Ansprechpartner** bei Problemen (Support-Desk)
5. **WLAN deaktivieren!** (wichtiger Hinweis, damit nicht das falsche Interface konfiguriert wird)

### Wichtige Hinweise fuer die Handzettel:
- Grosse, gut lesbare Schrift
- Farbliche Markierung der individuellen IP-Adresse
- Warnung: "Verwende NUR DEINE IP-Adresse!"
- Screenshots der Konfigurationsschritte
- QR-Code zu Video-Anleitungen (optional)