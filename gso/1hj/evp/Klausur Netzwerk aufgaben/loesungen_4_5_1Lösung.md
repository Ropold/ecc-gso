# Klausur EvP - Netzwerk Lösungen

## Aufgabe 4 (12P) - Phi

**a) Privater Adressbereich:**
- `10.0.0.0/8` (Klasse A privat)
- Netzmaske: `255.255.0.0/16`

**b) Netzmaske der Subnetze:**
- `/16` bzw. `255.255.0.0`

**c) Oktett-Schema:**

| Oktett | Information | Nummernbereich |
|--------|-------------|-------|
| 1. Oktett | Adressbereich | 10    |
| 2. Oktett | Abteilung | 1-30  |
| 3. Oktett | Etage | 0-10  |
| 4. Oktett | Host | 1-150 |

**d) IP-Adresse und Broadcastadresse:**
- **IP-Adresse:** `10.12.3.43`
- **Broadcastadresse:** `10.12.255.255`

---

## Aufgabe 5 (9P)

**a) Privater Adressbereich:**
- `172.16.0.0/16` (Klasse B privat)
- Netzmaske: `255.255.0.0`

**b) Netzmaske der Subnetze:**
`/24`

**c) Adressen für die Subnetze:**

| Subnetz | Netzwerkadr. | Broadcastadr. | max. Adressber. für Rechner | Gateway Adr. |
|---------|-------------|---------------|----------------------------|--------------|
| 1       | 172.16.1.0  | 172.16.1.255  | 172.16.1.1 - 172.16.1.50   | 172.16.1.254 |
| 2       | 172.16.2.0  | 172.16.2.255  | 172.16.2.1 - 172.16.2.50   | 172.16.2.254 |
| 3       | 172.16.3.0  | 172.16.3.255  | 172.16.3.1 - 172.16.3.50   | 172.16.3.254 |
| 4       | 172.16.4.0  | 172.16.4.255  | 172.16.4.1 - 172.16.4.50   | 172.16.4.254 |
