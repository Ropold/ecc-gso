# LF3 – LS 3.2 „Let's have a LAN-Party" I01
## 2. „LAN-Party - Grundlagen-IPv4-Adressierung"

**Abteilung IT-Berufe**
**Georg-Simon-Ohm**
GSO 04.10..2020 v1.0
EvP

---

## IP-Nummer (IP):
Die IP-Nummer ist eine eindeutige Adresse eines physikalischen oder logischen Geräts in einem Netzwerk, sie ist eine 32-Bit Binärzahl. Die übliche Schreibweise sind 4 durch Punkte getrennte Dezimalzahlen, wobei jede Dezimalzahl für 8 Bit (Oktett)steht.

Beispiel: 10.3.4.13

## Netzmaske (NM):
Die Netzmaske zerlegt eine IPv4-Adresse in einen Netzwerkteil und einen Rechnerteil. Im linken Teil enthält die Netzmaske eine **fortlaufende Reihe** auf '1' gesetzter Bits,die den Netzwerkteil markieren. Im rechten Teil markiert eine **fortlaufende Reihe** auf '0'gesetzter Bits den Rechnerteil.

Beispiel: 255.255.255.0

## Netzwerkadresse (NW):
Die Netzwerkadresse ist die niedrigste Rechnernummer in einem Netzwerk, d. h. alle Bits des Rechnerteils sind auf '0' gesetzt. Die Funktion dieser Adresse ist die Adressierung des Netzwerks als Ganzes. Diese Adresse wird nicht zur Datenübertragung sondern z. B. zur Routerkonfiguration genutzt. Die Angabe einer Netzwerkadresse ist nur zusammen mit der Netzmaske eindeutig. Die Netzmaske kann entweder in der Langfassung mit 4 Oktetten angegeben werden oder in der sogenannten CIDR-Schreibweise (**C**lassless **I**nter **D**omain **R**outing):

Beispiel: 10.3.4.0 /24 ⇒ /24 ist eine alternative Schreibweise für die Netzmaske, es wird die Anzahl der auf '1' gesetzten Bits der Netzmaske angegeben.

## Broadcastadresse (BC):
Die Broadcastadresse ist die höchste Rechnernummer in einem Netzwerk, d. h. alle Bits des Rechnerteils sind auf '1' gesetzt. Die Funktion dieser Adresse ist die Adressierung aller Rechner des Netzwerks. Hierbei werden Daten an alle aktiven Rechner im Netz verschickt.

Beispiel: 10.3.4.255 ist die Broadcastadresse zu 10.3.4.0 /24

## max. Rechnerzahl:
Die maximale Anzahl Rechner in einem Netzwerk ist die Anzahl der mit den Bits des Rechnerteils darstellbaren Zahlen abzüglich der beiden Adressen mit Sonderfunktion, NW und BC.

max=2ⁿ−2; n = Anzahl der Bits im Rechnerteil.

## Adressierungsarten:
- **Unicast:** Ein einzelner Rechner wird adressiert.
- **Broadcast:** Alle Rechner in einem Netzwerk werden adressiert.
- **Multicast:** Eine Gruppe von Rechnern wird adressiert.
- **Anycast:** Ein Rechner aus einer Gruppe wird adressiert.

---

## Netzklassen:
Die Netzklassen sind eine grobe historische Einteilung des IPv4-Adressraumes. Inden ersten Jahren des Internets wurden die IP-Nummern ausschließlich nach dieser Klasseneinteilung an interessierte Firmen und Institutionen vergeben, was eine Verschwendung von Adressen zur Folge hatte. Heute sind praktisch alle öffentlichen Adressen vergeben und können nur noch gemietet werden. Es sind beliebige Netzgrößen möglich (CIDR). Die Netzklassen A, B, und C haben heute keinerlei technische Bedeutung mehr, die Begriffe werden jedoch weiterhin genutzt.

**Klasse A:** NM 255.0.0.0 (/8) – Adressen 1.x.x.x bis 127.x.x.x
**Klasse B:** NM 255.255.0.0 (/16) – Adressen 128.x.x.x bis 191.x.x.x
**Klasse C:** NM 255.255.255.0 (/24) – Adressen 192.x.x.x bis 223.x.x.x
**Klasse D:** Adressen 224.x.x.x bis 239.x.x.x Verwendung für Multicast-Betrieb, auch heute noch relevant.
**Klasse E:** Adressen ab 240.x.x.x sind reserviert, d. h. sie werden nicht benutzt.

## private IPv4-Adressbereiche:
Es gibt drei Bereiche im Adressraum, die für Nutzung in privaten, nicht öffentlichen, Netzen reserviert sind. Datenpakete mit diesen Adressen werden im öffentlichen Internet nicht weitergeleitet. Hierdurch ist es möglich, in internen (=privaten) Umgebungen die gleichen Adressen zu benutzen wie in anderen privaten Umgebungen. So vergibt z.B. die FritzBox standardmäßig überall Adressen aus dem Bereich 192.168.178.0 /24.

**10.0.0.0 /8** (z.T. auch als „privates A-Netz" bezeichnet)

**172.16.0.0 /16** bis **172.31.0.0 /16** (z.T. auch als „privates B-Netz" bezeichnet)

**192.168.0.0 /16** (z.T. auch als „privates C-Netz" bezeichnet)

## weitere Spezialnetze:

**127.0.0.0 /8** Adressbereich für die 'loopback'-Adresse (oder „local host"), mit der der Rechner Datenpakete an sich selbst schicken kann.

**169.254.0.0 /16** Adressbereich für selbst konfigurierende Netze. (APIPA)

**192.0.2.0 /24** Adressbereich zur Verwendung in Dokumentation und in Beispielen.