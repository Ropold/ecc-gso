# Klausur EvP - Netzwerk Lösungen

## Aufgabe 5 (9P) - Christoph

**a) Privater Adressbereich:**
- `172.16.0.0/16` (Klasse B privat)
- Netzmaske: `255.255.0.0`

**b) Netzmaske der Subnetze:**
`/ 24`

**c) Adressen für die Subnetze:**

| Subnetz | Netzwerkadr. | Broadcastadr. | max. Adressber. für Rechner | Gateway Adr. |
|---------|--------------|---------------|-----------------------------|--------------|
| 1       | 192.168.0.0  | 192.168.0.255 | 192.168.0.0 - 192.168.0.254 | 192.168.0.1  |
| 2       | 192.168.1.0  | 192.168.1.255 | 192.168.1.1 - 192.168.1.254 | 192.168.1.1  |
| 3       | 192.168.2.0  | 192.168.2.255 | 192.168.2.2 - 192.168.2.254 | 192.168.2.1  |
| 4       | 192.168.3.0  | 192.168.3.255 | 192.168.3.3 - 192.168.3.254 | 192.168.3.1  |