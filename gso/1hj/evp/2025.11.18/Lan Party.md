# Handzettel LAN-Party Planung

## 1. IP einstellen

1. Windows + R → `ncpa.cpl` → Enter
2. Netzwerkadapter rechtsklicken → Eigenschaften
3. Internetprotokoll IPv4 → Eigenschaften
4. Folgende IP-Adresse verwenden:
   - IP: `192.168.10.15`
   - Subnetzmaske: `255.255.255.0`
   - Gateway: `192.168.10.1`
5. OK → Fertig

## 2. IPv4-Adressräume

Für max. 100 Teilnehmer pro Spiel → /25 Subnetz (126 nutzbare Hosts)

| Spiel | Netzwerk | Gateway | Subnetzmaske |
|-------|----------|---------|--------------|
| Spiel 1 | 192.168.1.0/25 | 192.168.1.1 | 255.255.255.128 |
| Spiel 2 | 192.168.1.128/25 | 192.168.1.129 | 255.255.255.128 |
| Spiel 3 | 192.168.2.0/25 | 192.168.2.1 | 255.255.255.128 |
| Spiel 4 | 192.168.2.128/25 | 192.168.2.129 | 255.255.255.128 |
| Spiel 5 | 192.168.3.0/25 | 192.168.3.1 | 255.255.255.128 |
| Spiel 6 | 192.168.3.128/25 | 192.168.3.129 | 255.255.255.128 |
| Spiel 7 | 192.168.4.0/25 | 192.168.4.1 | 255.255.255.128 |
| Spiel 8 | 192.168.4.128/25 | 192.168.4.129 | 255.255.255.128 |
| Spiel 9 | 192.168.5.0/25 | 192.168.5.1 | 255.255.255.128 |
| Spiel 10 | 192.168.5.128/25 | 192.168.5.129 | 255.255.255.128 |

## 3. Beispiel-Handzettel

### Spiel 1 - Counter-Strike (Netzwerk: 192.168.1.0/25)

**Teilnehmer 1:**
- IP: `192.168.1.10`
- Subnetzmaske: `255.255.255.128`
- Gateway: `192.168.1.1`

**Teilnehmer 2:**
- IP: `192.168.1.11`
- Subnetzmaske: `255.255.255.128`
- Gateway: `192.168.1.1`

### Spiel 2 - League of Legends (Netzwerk: 192.168.1.128/25)

**Teilnehmer 1:**
- IP: `192.168.1.140`
- Subnetzmaske: `255.255.255.128`
- Gateway: `192.168.1.129`

**Teilnehmer 2:**
- IP: `192.168.1.141`
- Subnetzmaske: `255.255.255.128`
- Gateway: `192.168.1.129`
