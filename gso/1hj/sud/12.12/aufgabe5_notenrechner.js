
// Schritt 1: Gesamtpunktzahl eingeben
const gesamtpunktzahl = parseInt(prompt("Geben Sie die Gesamtpunktzahl ein (gerade Zahl): "));
let weiter = "j";

while (weiter === "j") {
    // Schritt 2: Erreichte Punkte eingeben
    const erreichtePunkte = parseInt(prompt("Geben Sie die erreichten Punkte ein (gerade Zahl): "));

    // Schritt 3: Prozent berechnen
    const prozent = Math.round((erreichtePunkte / gesamtpunktzahl) * 100);
    console.log("Der/die Schüler/in hat " + prozent + "% erreicht.");

    // Schritt 4: Note bestimmen
    let note = "";
    if (prozent >= 92) {
        note = "Sehr gut";
    } else if (prozent >= 81) {
        note = "Gut";
    } else if (prozent >= 67) {
        note = "Befriedigend";
    } else if (prozent >= 50) {
        note = "Ausreichend";
    } else if (prozent >= 30) {
        note = "Mangelhaft";
    } else {
        note = "Ungenügend";
    }
    console.log("Die Note nach IHK Notenschlüssel ist: " + note);

    // Schritt 5: Weiteren Schüler eingeben?
    weiter = prompt("Weiteren Schueler eingeben?j ");
}

console.log("bis zum nächsten Mal");