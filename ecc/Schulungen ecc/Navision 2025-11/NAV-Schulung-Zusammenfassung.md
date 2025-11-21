# Microsoft Dynamics NAV - Schulungsnotizen Zusammenfassung

## 1. Tastenkombinationen & Shortcuts

| Aktion | Tastenkombination |
| --- | --- |
| Designer | Shift + F12 |
| Code | F9 |
| Properties | Shift + F4 |
| Windows wechseln | Strg + Tab |
| Search Funktion | Strg + F7 |
| Filter entfernen | Strg + Shift + F7 |
| Assist | Alt + Pfeil runter |
| In Flowfilter Limit setzen | Strg + Shift + F3 |
| Haken setzen | Leertaste |

## 2. Grundlegende Konzepte

| Konzept | Beschreibung |
| --- | --- |
| Fields | Felder in Tabellen |
| Records | Ein Datenbankeintrag |
| Tables | Tabellen |
| Companies | Mandanten |
| RTC | Role Tailored Client - User Interface mit Startseite |

## 3. Programmiersprachen

| Begriff | Bedeutung |
| --- | --- |
| C/AL | Client Application Language - prozedurale Programmiersprache |
| AL | Objektbasierte Programmiersprache |
| SQL | Relationale Datenbank - "Structured Query Language" |
| NoSQL | Dokumentenorientierte, spaltenbasierte, key-value- oder graphbasierte Datenbank |

## 4. Syntax & Operatoren

| Element | Syntax | Hinweis |
| --- | --- | --- |
| Zuweisung | `:=` | Entspricht `=` |
| Vergleich | `IF Amount = 1234 THEN` | Es gibt kein `==` |
| Semikolon | `;` | Bei neuem Statement |
| Operatoren | `+`, `-`, `*`, `/`, `<=`, `>=`, `<>`, `MOD` | |
| Logische Operatoren | `NOT`, `OR`, `AND`, `XOR` | |

**Beispiele:**
```
NOT OR AND XOR
IF NOT IN
IF (item = 23) OR (item = 27) AND
IF item = 27
```

## 5. Sprachkonstrukte

### Bedingungen

`IF <expr> THEN <stmt>`

`IF <expr> THEN <stmt> ELSE <stmt>`

`CASE <expr> OF <const> : <stmt> {; <const> : <stmt>} [ELSE <stmt>] END`

### Kontrollfluss

`EXIT[(<expr>)]`: Direkter Abbruch der aktuellen Funktion

**Notiz:** Ein `EXIT` in einem Trigger unterbricht die Default Action.

`BEGIN <stmt> {; <stmt>} END`: Anweisungsblock

### Schleifen

`FOR <expr> (TO|DOWNTO) <expr> DO <stmt>`: In 1er-Zählschritten, bis einschließlich Endwert

**Notiz:** Zählschritt muss explizit angegeben werden.

`WHILE <expr> DO <stmt>`: While-Schleife

`REPEAT <stmt> UNTIL <expr>`: "Until true" statt "while true"; läuft solange "until false"

## 6. Statements

**Ein Statement ist eine Anweisung, die vom Compiler interpretiert wird und eine Aktion ausführt.**

Ein Statement sagt dem System: "Mach das!"

| Typ | Beispiel |
| --- | --- |
| Zuweisung | `Variable := Wert` |
| Funktionsaufruf | `MESSAGE` (funktion-call Statement) |
| Bedingung | `IF ... THEN` |
| Loop | `FOR`, `WHILE` |

## 7. Kommentare

`//...`: Einzeilig

`{...}`: Auch mehrzeilig

## 8. Variablen

### Variablen-Operationen

`<simple-var>.INIT`: Setzt Variablenwert auf Initialwert zurück

`<record>.RESET`: Setzt Ergebnissatz, Filter u.ä. zurück

### Namensgebung

| Präfix | Bedeutung |
| --- | --- |
| `L_` | Lokal |
| `G_` | Global |
| Record | UpperCamelCase des zugehörigen Tabellennamen |
| Hungarian Notation | Bedingt erlaubt, falls Datentyp zur Anwendung tatsächlich relevant |

### Variablentypen (in CodeUnits)

**Hinweis:** Eher lokal, nicht global verwenden!

| Variablentyp | Subtype | Beschreibung |
| --- | --- | --- |
| Integer, Decimal, BigInt, Option | Zahlen | OptionString = Namen |
| Char, Text, Code | z.B. 2, 30, 10 Length | |
| Boolean | 0, 1 | |
| Date, Time, DateTime | | |
| `var_typ` | Record | Subtype Item |
| `var_page` | Page | Um auf Funktionen zuzugreifen |
| `var_codeunit` | Codeunit | Umgekehrt auch |
| `var_file` | Files | Importieren |
| `var_dialog` | MessageBox | Z.B. 3 Sachen zur Auswahl |
| `var_recordRef` | | Spalte aus einem Record (DB) |
| `var_fileref` | | |
| `var_keyref` | | |
| `var_intr` | InStream | |
| `var_out` | OutStream | |
| `var_var` | Variant | Alles |
| `var_bt` | BigText | Bis 2GB |
| `var_rep` | Report | |

### Option-Variablen

Bei Variablen vom Typ _Option_: `<var>::<option-name>`

## 9. Funktionen (Functions)

Im _View → C/AL Globals_ unter Functions anlegen

### Funktionssignatur

Parameterliste einstellen: Funktion auswählen, dann über _View → C/AL Locals_ in "Parameters"

**Notiz:** Bei Aktivierung von `VAR` sind Übergabeparameter als Aliase (oder Referenzen) übergeben.

**Parameter**: Haken links ist für return und verändert den Wert (call by value, call by reference)

**Return value**: Unüblich aber möglich; eher über VAR zurückgeben

### Funktionsbeispiel
```
LOCAL CreateAccountingDateFilter
(VAR Filter : Text[30]; VAR Name : Text[30]; FiscalYear : Boolean; Date : Date; NextStep : Integer)
```

```
[External]
ConvertToUtcDateTime(LocalDateTime : DateTime) : DateTime
```
- Funktionsname
- Parameter
- Rückgabewert

## 10. Funktionen vs. Trigger

### Vergleich

| Merkmal | Funktion (Procedure) | Trigger |
| --- | --- | --- |
| Parameter | Kann Parameter haben | Nein |
| Sichtbarkeit | Kann local oder global sein | Nein |
| Aufruf | Wird manuell aufgerufen | Automatisch |
| Name | Frei wählbarer Name | Fester Name |
| Rückgabewert | Kann Rückgabewert haben | Nein |

### Trigger - Automatische Reaktion auf Systemereignisse

**Wichtige Variablen in Triggern:**

| Variable | Bedeutung |
| --- | --- |
| `rec` | Aktuelles Record |
| `xRec` | Altes DB Model (vor Änderung) |

**Trigger-Typen:**
- Table Trigger
- Page Trigger
- Field Trigger
- Codeunit Trigger
- Report Trigger
- XML Trigger

## 11. Textkonstanten

Für i18n, unter Drilldown mehrsprachige Alternativen angeben.

**Notiz:** Diese immer global anlegen, nicht lokal.

## 12. Wichtige Funktionen

### Benutzer-Interaktion

`MESSAGE('The value of %1 is %2','Amount',Amount)`: %1 und %2 sind Platzhalter

`ERROR`: Selten verwendet, da Standard-Error bereits hilfreich sind

`CONFIRM`: Eine OkCancel MsgBox

`STRMENU(<text>,<def-opt>)`: Gibt eine Auswahl als RadioGroup

**Notiz:** Die Optionen sind im Text als CSV. Zeilenumbrüche über `+/` bzw `/+` angeben (ausprobieren!). **& macht Punkte, + Zeilenumbruch**

### Record-Operationen

`<record>.SETCURRENTKEY`: Einstellen der Sortierung der Tabelleneinträge (Vorschlag für SQL)

`<record>.SETRANGE(<field-name>[,<from>][,<to>])`: Filtert die Tabelleneinträge

Beispiel: `customer.SETRANGE("No", 'd10000', 'D69999')`

`<record>.SETFILTER(<field-name>,<text>)`: Genaue Filterangabe mit Platzhaltern

Beispiel: `customer.SETFILTER(Name, 'M??er')`

`<record>.FIND`: Datensatz suchen

**Notiz:** Bevorzuge `findfirst` statt `find('-')`.

`<record>.GET(<expr>)`: Bekomme _einen_ Eintrag abh. vom KEY

**Notiz:** Gibt Fehlermeldung zurück bei Nicht-Fund. Kann mit IF geprüft werden.

`<record>.(INSERT|MODIFY|DELETE)[(<do-validate>)]`: Einträge ändern; standardmäßig die Validierung überspringen

Bei `insert(true)` wird OnInsert getriggert

`<record>.CALCFIELDS(<field-name>[,<field-name>])`: Berechnet FlowFields für den Ergebnissatz

`<record>.init`: Variable auf 0 setzen

`<record>.reset`: Filter etc. entfernen

### Datums-Funktionen

`DMY2DATE(9,10,2004)`: Datum erstellen

### String-Funktionen

`Var_text2 := COPYSTR(Var_text)`: Kopiert String

`Var_Integer := MAXSTRLEN(Var_Text)`: Länge von Strings

### Expressions

`7*5 > 6*6`: Einfache Formeln +- etc, wird 35 mit 36 verglichen

## 13. Numerische Nomenklatur (Object IDs)

| Bereich | Verwendung | Hinweis |
| --- | --- | --- |
| 1 - 49.999 | Microsoft - bis 10k W1 worldwide, ab 10k DE | |
| 50.000 - 99.999 | **Kundenspezifische Entwicklung - NUR HIER!** | |
| 100.000 - 999.999 | Temporär - Upgrade unbekannt | |
| 1.000.000 - 9.999.999 | Zertifizierte Module, Branchenlösungen (Gob, Cosmo, Kumavision) | **WIR NICHT** |
| 99.000.000 | Navision Manufacturing | |
| 5.000.000 | OP - Extension | |

## 14. Compile-Prozess

| Schritt | Bedeutung |
| --- | --- |
| Änderung | Code bearbeiten |
| Compile klicken | Code übersetzen |
| **Compiled** | Code erfolgreich übersetzt und vom Server ausführbar |
| **Uncompiled** | Nur im Editor gespeichert, aber nicht aktiv lauffähig |

## 15. Tabellen (Tables)

### Wichtige Table Properties

| Property | Beschreibung | Hinweis |
| --- | --- | --- |
| `DataPerCompany` | Daten pro Mandant | Nie auf null, sharen |
| `Permissions` | Rechte auf Objekte | |
| `DataCaptionFields` | Im Frontend oben die Namen | |
| `LookUpFormId` | Z.B. Postcode, macht Pfeil | |
| `ValidateTableRelation` | Yes | |
| `AutoSplitKeys` | Nicht verwenden! | Findet man bei Page properties |

### Table Trigger

- `OnDelete`
- `OnModify` - Führt erst am Ende aus
- `OnInsert`
- `OnRename` - Nur Navision spezifisch

### Wichtige Konzepte

| Konzept | Beschreibung |
| --- | --- |
| Posten | Entry |
| Bei Posten ist Integer PK | Erstes Feld vom Integer wird mit 10k gezählt, nur int sonst egal |
| Secondary Keys | Wichtig für Lesegeschwindigkeit, aber Datenbank-Eintrag kann langsamer werden |
| Keine Tabelle ohne Page | Tabelle nur Insert, Delete, Edit |
| SQL speichern nur an einer Stelle | Normalisierung |

### Buchungscode

22 - Buchungscode Unit - Item Jnl - Post-Line (ganz unten leeres Field)

## 16. Felder (Fields)

### Field Properties

| Property | Beschreibung | Beispiel |
| --- | --- | --- |
| `AutoFormatExpression` | Kommastellen | `2:2` z.B. |
| `AutoFormatType` | Wie ein Feld formatiert wird | Z.B. Zahl, Datum, Währung, Boolean |
| `BLOB` | Externe Elemente in die DB einfügen | Für Bilder |
| `FlowFields` | Zur Laufzeit berechnete Felder | `FieldClass => FlowField`, `Editable => NO` |
| `LookUp` | Description von Fields | |

### Field Trigger

- `OnValidate` - Wichtig!
- `OnLookup()` - Noch mal angucken
- `OnDrill()` - Noch mal angucken

### Validate

- Immer `OnValidate()`
- In Zuweisung nur in Ausnahmen

## 17. Pages

### Page Properties

| Property | Beschreibung | Hinweis |
| --- | --- | --- |
| `SourceTable` | Wichtigste Property | |
| `DelayedInsert` | Einzelne Felder in der Buchhaltung z.B. ändern zu können | |
| `SubPageLink` | Nur die VK Zahlen anzeigt | |
| Properties von Feldern | Hat immer Trigger | |

### PageAction

| Property | Beschreibung |
| --- | --- |
| `RunObject` | |
| `RunPageView` | |
| `RunPageLink` | Table relation - FIELD muss manuell gemacht werden |
| `OnAction` | Trigger programmieren |

### PageTypes

| Typ | Verwendung | Beispiel |
| --- | --- | --- |
| `CardPart` | | |
| `ListPart` | | |
| `Document` | | |
| `Worksheets` | | Navigate in der Buchhaltung z.B. |
| Listpage | Alle Sätze, alle Tabelle | Nicht editierbar wenn es eine Card gibt |
| Card | Datendarstellung mit SubForm mit Listpage | |

### Wichtige Konzepte

- **Vermeiden**: Programmieren auf der Page, sondern immer Tabelle oder Codeunit für die Extension
- Page viel mehr als Table: Trigger und Reiter
- Altes Page ist Form (in Classic)
- Report muss Page => Codeunit => GUI, Design

### Belege

- Card Darstellung mit SubForm mit Listpage
- Buchhaltung muss nicht Kalenderjahr sein (Transcape)
- Veränderung und Saldo anzeigen

### Buchungsblätter

- Buchungsblatt Vorlage, Zeile, Name

## 18. CodeUnit

- Eher lokale Variablen verwenden, nicht global!

## 19. Export/Import

| Format | Beschreibung |
| --- | --- |
| .text | Keine Validierung, Objekte müssen verglichen werden |
| .fob | Final Object File - Schon validiert und compiliert |
| Dataport (ganz alt) | .aks, .csv Dateien |

## 20. Fachvokabular

| Begriff | Bedeutung | Abkürzung |
| --- | --- | --- |
| General Ledger Account | Sachkonto | G/L Account |
| Salesperson/Purchaser | Einkäufer/Verkäufer | |
| Debitoren | Kunde der Geld schuldet | |
| Kreditoren | Lieferant der auf sein Geld wartet | |
| Kämmerei | Finanzabteilung der Stadt die Gelder freigibt aus dem Haushalt | |
| Posten | Entry | |
| OP-Liste | Offene Posten | |
| OP-Plus | | |
| Quantity | Menge | |

## 21. Objekttypen

- Table
- Page
- Codeunit
- Report
- Query
- XMLPort

## 22. Sonstiges

- Symbol Menu zeigt verfügbare Funktionen
- Keys in Sales Header
- Navigate in der Buchhaltung
- **Record Var**: Wie die Tabelle