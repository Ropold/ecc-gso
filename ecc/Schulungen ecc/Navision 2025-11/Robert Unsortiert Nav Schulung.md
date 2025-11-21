no space for all

| designer | shift f12 |
| --- | --- |
| code  | f9 |
| properties | shift f4 |
| windows wechseln | str  tab |
| search funktion | str f7 |
| Filter entfernen | str shift f7 |
| assist | alt pfeil runter |
| in Flowfilter limit setzten | str shift f3 |
| haken setzten | leertaste |

| änderung - Compile klicken - compiled | In NAV/BC 18 bedeutet **„compiled“**, dass der Code erfolgreich übersetzt wurde und vom Server ausgeführt werden kann.**Uncompiled** = nur im Editor gespeichert, aber nicht aktiv lauffähig. |
| --- | --- |
| fields - records - tables - companies |  |
| (record ist ein db eintrag) |  |
| General Ledger Account - Sachkonto | G/L Account |
| C/AL | Client Application Language |
| C/AL | C/AL ist eine **prozedurale Programmiersprache** |
| AL | AL ist eine **objektbasierte Programmiersprache** |
| := | zuweisung wie = |
| IF Amount = 1234 THEN | gibt kein == |
| Funktionen heißen in CL | Procedures |
|  automatische Reaktion auf Systemereignisse, OnInsert(), z.b.
zeiTable Kunde speichern,
Page Seite öffnen,
Codeunit aufrufen,
Report Druck,
XML Importieren | Trigger  |
| LOCAL CreateAccountingDateFilter
(VAR Filter : Text[30];VAR Name : Text[30];FiscalYear : Boolean;Date : Date;NextStep : Integer) | ist eine Funktion |
| Funktion:
kann Parameter haben
Kann local oder global sein
Wird Manuell aufgerufen
Frei Wählbarer Name
Kann Rückgabewert haben | Trigger:
Nein
Nein
Automatisch
Fester Name
Nein |
| `[External] 
ConvertToUtcDateTime
(LocalDateTime : DateTime) :
 DateTime` → | Funktionsname
Parameter
Rückgabewert |
| Ein **Statement** ist in der Programmierung eine **Anweisung**, die **vom Compiler interpretiert wird** und **eine Aktion ausführt**. | Ein Statement sagt dem System: „Mach das!“:
Zuweisung
Funktionsaufruf
Bedinung
Loop |
| MESSAGE | funktion-call Statement |
| semikolon bei neues statement | ; |

numerische Nomenklatur

| 1-49.999 ms | bis 10k w1 worldwird → ab 10k de |
| --- | --- |
| 50.000-99.999 | Kundenspezifisch Entw. NUR HIER |
| 100.000-999.999 | Temporär - upgrate kp |
| 1.000.000 - 9.999.999 | zertifizierte Modul, brachen lösungung. Gob, Cosmo, Kumavision, 
WIR NICHT |
| 99.000.000 | Navision manugactoring |
|  |  |
| opi - extention | 5.000.000 |

| dataPerCompany | nie auf null | sharen |
| --- | --- | --- |
| Posten - Entry |  |  |
| Permissions | Rechte  auf Objekte |  |
| DataCaptionsFields | im frontend oben  die namen |  |
| LookUpFormId | z.b. Postcode, macht pfeil |  |
| onDelete |  |  |
| onModify | führt erst am ende aus |  |
| OnInsert |  |  |
| OnRename | nur Navision spezifisch |  |
| rec  | aktuelles |  |
| xRec | altes db model |  |
| Salesperson/Purchaser | Einkäufer/verkäufer |  |
| validateTableRelation | Yes |  |
| bei posten ist integer pk |  |  |
| autoSplitKeys (nicht verwenden) | findet man bei Page properties

22 - buchungscode unit - Item Jnl - Post-Line | ganz unten leeres Field
erstes feld vom integer wird mit 10k gezählt, nur int sonst egal |
| autoformatExpression  | komma stellen  | 2:2 z.b. |
| autoFormatType | Legt fest, wie ein Feld oder Control automatisch formatiert wird,  | z. B. Zahl, Datum, Währung, Boolean. |
| blob | externe elemente in die db einzufügen | für Bilder |
| OnValidate | wichtig |  |
| Secendary Keys  | wichtig für lesegeschwindigkeit | aber Datenbank eintrag - kann langsamer werden |
| flowfields | zur laufzeit berechnete felder | Fieldclass ⇒ flowFlied
Editibar ⇒ NO |
| op-Liste | offene Posten |  |
| LookUp | ist description von fields |  |
| report |  muss page ⇒ codeunit ⇒ gui, design |  |
| altes page ist form - in classic |  |  |
| objekt typen sind |  z.b. table, page etc |  |
| rtc | role tailored client | User Interface mit Startseite |
| Debitoren | Kunde der Geld schuldet |  |
| Kreditoren | Lieferant der auf sein Geld wartet |  |
| Kämmerei | Finanzabteilung der Stadt die Gelder freigibt aus dem Haushalt |  |
| dataport ganz alt  | .aks, .csv, Dateien |  |
| sql speichern nur an einer stelle | normalisierung |  |
| export | in .text oder .fob format
(final object file) | .text hat keine validierung
text datei müssen objekte verglichen werden
.fob ist schon validiert und compeliert
|
| sql ist eine relationale Datenbank
| „Structured Query Language“ |  |
| NoSQL ist eine  | dokumentenorientierte, spaltenbasierte, key-value- oder graphbasierte Datenbank |  |
| quantity | menge |  |
| keine tablele ohne page | tabelle nur inser,delete, edit,  |  |
| page viel mehr | trigger und reiter |  |
| Listpage, allensäzte alle tabelle | nicht Editirbar wenn es eine Card gibt.  |  |
| Belege: | Card datstellung, mit subform mit listenpage | Buchhaltung muss nicht kalenderjahr sein,
Transcape |
|  | veränderung und saldo anzeigen |  |
| in Page SourceTable  wichtigste |  |  |
| DelayedInsert | einzelne felder in der buchhaltung z.b. ändern zu können |  |
| vermeiden programmieren uaf der page, sondern immer tabelle oder codeunit für die extension |  |  |
| properties von felder - hat immer trigger |  |  |
| on validate, on lookup, on drill noch mal angucken |  |  |
| subPagelink | nur die vk zahlen anzeigt |  |
| keys in sales header |  |  |
| pageAction | RunObject,
RunpageView,
RunPageLink | Table relation - FIELD muss manuel gemacht werden |
| onAction trigger programmieren |  |  |
| pageTypes | CardPart, ListPart, Document, Worksheets | navigate in der Buchhaltung z.b. |
| Buchungsblätter  | buchungsblatt forlage, zeile, name |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |


codeuUnit

| var lokal und gobal |  |  |
| --- | --- | --- |
| eher lokal nicht global |  |  |
| integer, decimal, Bigint und option | zahlen | optionstring = namen |
| char, text, code | zb.2, 30, 10 length |  |
| boolean | 0,1 |  |
| date, time, Datetime,  |  |  |
| var_typ record | subtype item,  |  |
| var_page | Page | um auf funktionen zuzugreifen,  |
| car_codeunit | Coudeunit | umekehrt auch  |
| var_file | Files importieren |  |
| var_dialog | messagebox | z.b. 3 sachen zur auswahl |
| var_recordRef | Spalte aus einem record (db) |  |
| var_fileref |  |  |
| var_keyref |  |  |
| var_intr(stream) | instream |  |
| var_out(stream) |  |  |
| var var | alles |  |
| var_bt  | bigtext bis 2gb |  |
| var_rep | report |  |
| validate | immer onValidate() | in zuweisung nur in ausnahmen. |
| parameter | +-/* , <= , = >, <> , MOD,  |  |
|  | := | zuweisung wie = |
|  | IF Amount = 1234 THEN | gibt kein == |
| Var_text2 := COPYSTR(Var_text) | kopiert |  |
| Var_Integer := MAXSTRLEN(Var_Text) | - länge von strings |  |
| OP-Plus |  |  |


Var_text2 := COPYSTR(Var_text)	kopiert
Var_Integer := MAXSTRLEN(Var_Text)	- länge von strings
OP-Plus		
symbol menu zeigt verfügbare funktionen		
MESSAGE('The value of %1 is %2','Amount',Amount);	%1 und %2 sind platzhalter
"When Was It" := DMY2DATE(9,10,2004);		
expressions	einfache formeln +- etc
7*5 > 6*6	wird 35 mit 36 verglichen
G_	Gloabal
L_	Lokal
record var wie die tabelle		
statement	IF WHILE etc, 	
bei parameter der haken links ist für return und verändert den wert	call by value, call by referenz
& macht punkte 	+/ zeilenumbruch
wichtig!!!		
customer.SETCURRENTKEY()	vorschlag für sql, 	
customer.SETRANGE()	(”No”, ’d10000’, ‘D69999’)
customer.SETFILTER()	(Name, ‘M??er’)

customer.find(’-’);		
customer.get	ein datensatz anhand des keys
Var_Dec.init	var auf 0 setzten
customer.reset	filter etc entfernen

customer.insert(true)	bei true wird onInsert getriggert	