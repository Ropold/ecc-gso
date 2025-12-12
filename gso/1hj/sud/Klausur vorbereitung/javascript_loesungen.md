# Klausurvorbereitung - JavaScript Lösungen

## Aufgabe 1: Umrechnung

**Frage:** Ein Computer kodiert Buchstaben und Sonderzeichen als achtstellige Dualzahlen. Wie viele verschiedene Zeichen können auf diese Weise codiert werden?

**Lösung:**
- Bei 8 Bit gibt es 2^8 = **256 verschiedene Zeichen**

---

## Aufgabe 3: Größenvergleich

```javascript
// Größenvergleich von zwei Nutzereingaben

const eingabe1 = parseInt(prompt("Bitte geben Sie die erste Zahl ein:"));
const eingabe2 = parseInt(prompt("Bitte geben Sie die zweite Zahl ein:"));

if (eingabe1 > eingabe2) {
    console.log("Eingabe 1 war größer");
} else if (eingabe2 > eingabe1) {
    console.log("Eingabe 2 war größer");
} else {
    console.log("Die Eingaben waren identisch");
}
```

---

## Aufgabe 4: Summieren

**Variante 1: Mit while-Schleife**

```javascript
// Summieren mit while-Schleife

const untergrenze = parseInt(prompt("Bitte geben Sie die Untergrenze ein:"));
const obergrenze = parseInt(prompt("Bitte geben Sie die Obergrenze ein:"));

let summe = 0;
let i = untergrenze;

while (i <= obergrenze) {
    summe += i;
    i++;
}

console.log(`Die Summe von ${untergrenze} bis ${obergrenze} ist: ${summe}`);
```

**Variante 2: Mit for-Schleife**

```javascript
// Summieren mit for-Schleife

const untergrenze = parseInt(prompt("Bitte geben Sie die Untergrenze ein:"));
const obergrenze = parseInt(prompt("Bitte geben Sie die Obergrenze ein:"));

let summe = 0;

for (let i = untergrenze; i <= obergrenze; i++) {
    summe += i;
}

console.log(`Die Summe von ${untergrenze} bis ${obergrenze} ist: ${summe}`);
```

---

## Aufgabe 5: Winkelmass Umwandler

```javascript
// Winkelmass Umwandler

const wahl = parseInt(prompt("Winkelmass Umwandler\n1 - Von Gradmass zu Bogenmass\n2 - Von Bogenmass zu Gradmass\n\nBitte wählen Sie (1 oder 2):"));

if (wahl === 1) {
    // Gradmass zu Bogenmass
    const grad = parseFloat(prompt("Bitte geben Sie den Winkel in Grad ein:"));
    const bogenmass = (grad * Math.PI) / 180;
    console.log(`${grad}° = ${bogenmass} rad`);
} else if (wahl === 2) {
    // Bogenmass zu Gradmass
    const rad = parseFloat(prompt("Bitte geben Sie den Winkel in Bogenmass (rad) ein:"));
    const gradmass = (rad * 180) / Math.PI;
    console.log(`${rad} rad = ${gradmass}°`);
} else {
    console.log("Ungültige Eingabe!");
}
```

**Formeln:**
- Grad zu Bogenmass: `rad = (grad × π) / 180`
- Bogenmass zu Grad: `grad = (rad × 180) / π`

---

## Aufgabe 6: Würfelspiel

**Basis-Version:**

```javascript
// Würfelspiel - Ziel: Erreiche genau 21 Punkte

console.log("Willkommen zum Würfelspiel!");
console.log("Ziel: Erreiche genau 21 Punkte");
console.log("Regel: Bei Überschreitung fällst du auf 0 zurück\n");

let punkte = 0;
let wurfAnzahl = 0;

while (punkte !== 21) {
    confirm("Klicken Sie OK zum Würfeln");

    // Würfeln (1-6)
    const wurf = Math.floor(Math.random() * 6) + 1;
    wurfAnzahl++;

    console.log(`Wurf ${wurfAnzahl}: Du hast eine ${wurf} gewürfelt`);

    // Punkte addieren
    punkte += wurf;

    // Überprüfung
    if (punkte > 21) {
        console.log(`Oh nein! Mit ${punkte} Punkten hast du 21 überschritten!`);
        console.log("Du fällst auf 0 zurück.\n");
        punkte = 0;
    } else if (punkte === 21) {
        console.log(`\nGlückwunsch! Du hast 21 Punkte erreicht!`);
        console.log(`Du hast ${wurfAnzahl} Würfe gebraucht.`);
    } else {
        console.log(`Aktuelle Punktzahl: ${punkte}\n`);
    }
}
```

**Mit Computergegner:**

```javascript
// Würfelspiel mit Computergegner

console.log("Willkommen zum Würfelspiel mit Computergegner!");
console.log("Ziel: Erreiche genau 21 Punkte vor dem Computer\n");

let spielerPunkte = 0;
let computerPunkte = 0;
let runde = 0;

while (spielerPunkte !== 21 && computerPunkte !== 21) {
    runde++;
    console.log(`--- Runde ${runde} ---`);

    confirm("Drücken Sie OK zum Würfeln");

    // Spieler würfelt
    const spielerWurf = Math.floor(Math.random() * 6) + 1;
    console.log(`Spieler würfelt: ${spielerWurf}`);
    spielerPunkte += spielerWurf;

    if (spielerPunkte > 21) {
        console.log(`Spieler überschreitet mit ${spielerPunkte} Punkten! Zurück auf 0.`);
        spielerPunkte = 0;
    } else if (spielerPunkte === 21) {
        console.log(`Spieler gewinnt mit 21 Punkten!`);
        break;
    } else {
        console.log(`Spieler Punktzahl: ${spielerPunkte}`);
    }

    // Computer würfelt
    const computerWurf = Math.floor(Math.random() * 6) + 1;
    console.log(`Computer würfelt: ${computerWurf}`);
    computerPunkte += computerWurf;

    if (computerPunkte > 21) {
        console.log(`Computer überschreitet mit ${computerPunkte} Punkten! Zurück auf 0.`);
        computerPunkte = 0;
    } else if (computerPunkte === 21) {
        console.log(`Computer gewinnt mit 21 Punkten!`);
        break;
    } else {
        console.log(`Computer Punktzahl: ${computerPunkte}`);
    }

    console.log(`\nSpielstand: Spieler ${spielerPunkte} - Computer ${computerPunkte}\n`);
}

console.log(`\nSpiel beendet nach ${runde} Runden!`);
```

---

## Hinweise zur Ausführung:

**Im Browser:**
- Code in die Browser-Console kopieren (F12 → Console)
- Oder in HTML-Datei mit `<script>` Tags einbinden

**Als HTML-Datei:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>JavaScript Lösung</title>
</head>
<body>
    <h1>Öffne die Console (F12)</h1>
    <script>
        // Hier den JavaScript-Code einfügen
    </script>
</body>
</html>
```