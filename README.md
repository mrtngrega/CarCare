# CarCare Detailing
Ročníkový projekt - webová aplikácia

Webová aplikácia CarCare Online je moderný informačný systém určený pre detailingové štúdio CarCare Detailing. Jej hlavným cieľom je zjednodušiť rezerváciu služieb a správu zákazníkov. Používatelia sa môžu zaregistrovať, prihlásiť do svojho účtu a jednoducho si rezervovať termín podľa dostupnosti. Aplikácia ponúka prehľad detailingových služieb, pri ktorých sa cena automaticky vypočíta podľa veľkosti vozidla. Zákazníci zároveň získavajú vernostné body, ktoré môžu neskôr využiť na odmeny alebo bezplatné služby. Vo svojom profile majú prehľad o rezerváciách, histórii služieb, vozidlách a nazbieraných bodoch. Súčasťou aplikácie je aj systém súťaží o atraktívne ceny. Administrátor môže spravovať služby, rezervácie, zákazníkov, ceny a vernostný program. Webová aplikácia je responzívna, takže funguje na počítači, tablete aj mobilnom telefóne. Jej cieľom je zvýšiť komfort zákazníkov a zefektívniť každodennú prevádzku detailingového štúdia.

---

## 🛠️ Použité technológie (Technologický stack)

### **Frontend (Klientska časť)**
* **HTML5:** Štruktúra webových stránok a formulárov.
* **CSS3:** Responzívny dizajn prispôsobený pre PC, tablety aj mobilné zariadenia.
* **JavaScript (ES6+):** Dynamická funkcionalita, komunikácia s backendom prostredníctvom Asynchrónneho API (`fetch`).

### **Backend (Serverová časť)**
* **Python:** Hlavný programovací jazyk pre logiku aplikácie.
* **Flask:** Lahký webový framework zabezpečujúci obsluhu HTTP požiadaviek a routing.
* **JWT (JSON Web Tokens):** Bezpečná autentifikácia a autorizácia používateľov a administrátorov.
* **Werkzeug:** Hashovanie a overovanie používateľských hesiel pre vyššiu bezpečnosť.

### **Databáza**
* **SQLite:** Relácia databáza pre bezpečné ukladanie dát o používateľoch, vozidlách, službách, rezerváciách a súťažiach.

---

## ⚙️ Ako aplikácia funguje

Aplikácia funguje na princípe architektúry **Client-Server** a REST API:

1. **Autentifikácia a Bezpečnosť:** 
   * Používateľ sa zaregistruje, pričom jeho heslo sa do databázy ukladá v zahashovej podobe.
   * Pri prihlásení server vygeneruje šifrovaný **JWT token**, ktorý sa ukladá na strane klienta a slúži na overovanie identity pri chránených operáciách.

2. **Dynamická Kalkulácia Ceny:**
   * Ceny služieb nie sú pevné. Pri výbere služby a konkrétneho vozidla backend automaticky prepočíta výslednú cenu podľa kategórie vozidla (napr. *Malé auto*, *Sedan*, *SUV/Van*).

3. **Rezervačný a Vernostný Systém:**
   * Zákazník si vybrerie službu, svoje auto a voľný termín.
   * Po absolvovaní a potvrdení rezervácie administrátorom sa zákazníkovi na konto automaticky pripíšu vernostné body, ktoré môže neskôr uplatniť na zľavy alebo špeciálne odmeny.

4. **Administrácia:**
   * Systém rozlišuje roly (`customer` a `admin`).
   * Administrátorské rozhranie umožňuje kompletnú správu (CRUD operácie) nad službami, cenníkom, rezerváciami zákazníkov a prebiehajúcimi súťažami.
ahoj skuska skuska nigr