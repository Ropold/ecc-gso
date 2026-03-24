
let weiter = "j";

while (weiter === "j") {
    // Schritt 1: Gesamtpunktzahl eingeben
    const gesamtpunktzahl = parseInt(prompt("Geben Sie die Gesamtpunktzahl ein (gerade Zahl): "));
    const erreichtePunkte = parseInt(prompt("Geben Sie die erreichten Punkte ein (gerade Zahl): "));

    // Schritt 2: Prozent berechnen
    const prozent = Math.round((erreichtePunkte / gesamtpunktzahl) * 100);
    console.log("Der/die Schüler/in hat " + prozent + "% erreicht.");

    // Schritt 3: Note bestimmen
    let note = "";
    if (prozent >= 92) {
        note = "sehr gut";
    }
    else if (prozent >= 81) {
        note = "gut";
    }
    else if (prozent >= 67) {
        note = "befriedigend";
    }
    else if (prozent >= 50) {
        note = "ausreichend";
    }
    else if (prozent >= 30) {
        note = "mangelhaft";
    }
    else {
        note = "ungenügend";
    }
    console.log("Die Note nach IHK ist: " + note);

    // Schritt 4: Weitermachen?
    weiter = prompt("Weiteren Schüler eingeben? (j/n): ");

}
console.log("bis zum nächsten Mal!");