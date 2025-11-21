# Schulung Microsoft Dynamics NAV - November 2015

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
| Bedingung | `IF NOT IN` | |
| Beispiel | `IF (item = 23) OR (item = 27) AND` | |

**Beispiele:**
```
NOT OR AND XOR
IF NOT IN
IF (item = 23) OR (item = 27) AND
IF item = 27
```

## 5. Funktionen vs. Trigger

### Vergleich

| Merkmal | Funktion (Procedure) | Trigger |
| --- | --- | --- |
| Parameter | Kann Parameter haben | Nein |
| Sichtbarkeit | Kann local oder global sein | Nein |
| Aufruf | Wird manuell aufgerufen | Automatisch |
| Name | Frei wählbarer Name | Fester Name |
| Rückgabewert | Kann Rückgabewert haben | Nein |

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

### Trigger - Automatische Reaktion auf Systemereignisse

**Beispiele:**
- `OnInsert()` - z.B. Table Kunde speichern
- `OnModify()` - Führt erst am Ende aus
- `OnDelete()`
- `OnRename()` - Nur Navision spezifisch
- `OnValidate()` - Wichtig!
- `OnLookup()` - Noch mal angucken
- `OnDrill()` - Noch mal angucken

**Weitere Trigger-Ereignisse:**
- Page: Seite öffnen
- Codeunit: Aufrufen
- Report: Druck
- XML: Importieren

### Wichtige Variablen in Triggern

| Variable | Bedeutung |
| --- | --- |
| `rec` | Aktuelles Record |
| `xRec` | Altes DB Model (vor Änderung) |

## 6. Statements

**Ein Statement ist eine Anweisung, die vom Compiler interpretiert wird und eine Aktion ausführt.**

Ein Statement sagt dem System: "Mach das!"

| Typ | Beispiel |
| --- | --- |
| Zuweisung | `Variable := Wert` |
| Funktionsaufruf | `MESSAGE` (funktion-call Statement) |
| Bedingung | `IF ... THEN` |
| Loop | `FOR`, `WHILE` |

## 7. Numerische Nomenklatur (Object IDs)

| Bereich | Verwendung | Hinweis |
| --- | --- | --- |
| 1 - 49.999 | Microsoft - bis 10k W1 worldwide, ab 10k DE | |
| 50.000 - 99.999 | **Kundenspezifische Entwicklung - NUR HIER!** | |
| 100.000 - 999.999 | Temporär - Upgrade unbekannt | |
| 1.000.000 - 9.999.999 | Zertifizierte Module, Branchenlösungen (Gob, Cosmo, Kumavision) | **WIR NICHT** |
| 99.000.000 | Navision Manufacturing | |
| 5.000.000 | OPI - Extension | |

## 8. Compile-Prozess

| Schritt | Bedeutung |
| --- | --- |
| Änderung | Code bearbeiten |
| Compile klicken | Code übersetzen |
| **Compiled** | Code erfolgreich übersetzt und vom Server ausführbar |
| **Uncompiled** | Nur im Editor gespeichert, aber nicht aktiv lauffähig |

## 9. Tabellen (Tables)

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

### Record-Operationen und wichtige Funktionen

| Operation | Syntax | Beschreibung |
| --- | --- | --- |
| `SETCURRENTKEY()` | `customer.SETCURRENTKEY()` | Vorschlag für SQL |
| `SETRANGE()` | `customer.SETRANGE("No", 'd10000', 'D69999')` | Bereichsfilter setzen |
| `SETFILTER()` | `customer.SETFILTER(Name, 'M??er')` | Filter mit Platzhaltern |
| `find('-')` | `customer.find('-')` | Datensatz suchen |
| `get` | `customer.get` | Ein Datensatz anhand des Keys |
| `init` | `Var_Dec.init` | Variable auf 0 setzen |
| `reset` | `customer.reset` | Filter etc. entfernen |
| `insert(true)` | `customer.insert(true)` | Bei true wird OnInsert getriggert |

### Weitere wichtige Funktionen

| Funktion | Syntax | Beschreibung |
| --- | --- | --- |
| Symbol Menu | | Zeigt verfügbare Funktionen |
| MESSAGE | `MESSAGE('The value of %1 is %2','Amount',Amount);` | %1 und %2 sind Platzhalter |
| DMY2DATE | `"When Was It" := DMY2DATE(9,10,2004);` | Datum erstellen |
| Expressions | `7*5 > 6*6` | Einfache Formeln +- etc, wird 35 mit 36 verglichen |

### Variablen-Präfixe

| Präfix | Bedeutung |
| --- | --- |
| `G_` | Global |
| `L_` | Lokal |

### Parameter und weitere Konzepte

- **Record Var**: Wie die Tabelle
- **Statement**: IF, WHILE etc.
- **Parameter**: Haken links ist für return und verändert den Wert (call by value, call by reference)
- **& macht Punkte, + Zeilenumbruch**

## 10. Felder (Fields)

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

### String-Funktionen

| Funktion | Beschreibung |
| --- | --- |
| `Var_text2 := COPYSTR(Var_text)` | Kopiert String |
| `Var_Integer := MAXSTRLEN(Var_Text)` | Länge von Strings |

## 11. Pages

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

## 12. CodeUnit

### Variablentypen (lokal und global)

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

### Validate
- Immer `OnValidate()`
- In Zuweisung nur in Ausnahmen

## 13. Export/Import

| Format | Beschreibung |
| --- | --- |
| .text | Keine Validierung, Objekte müssen verglichen werden |
| .fob | Final Object File - Schon validiert und compiliert |
| Dataport (ganz alt) | .aks, .csv Dateien |

## 14. Fachvokabular

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

## 15. Objekttypen

- Table
- Page
- Codeunit
- Report
- Query
- XMLPort

## 16. Sonstiges

- "no space for all" (Hinweis am Anfang der Notizen)
- Keys in Sales Header
- Navigate in der Buchhaltung
- 2-42 (unklar)
- 3-53 (unklar)