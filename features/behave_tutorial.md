
# Cucumber / Behave
## Alapok
- A Cucumber Pythonos implementációja a **Behave**.
Ennek installálásá a 
*pip install behave* paranccsal végezhető el.

- A *Behave* *.feature* fájlokban leírt forgatókönyveket (**Scenario**) futtat. Ezek a **Gherkin** szintaxist használják.
A *Pycharm* IDE rendelkezik *Gherkin* nyelvi támogatást biztosító pluginnel.

- A forgatókönyvekben megadott szöveges leírás minden sora **Given**, **When** vagy **Then** kulcsszóval kezdődik. Így rendeződik egy szituáció komplett leírásába. Használhatjuk az **And** és **But** kulcsszavakat is, de ezeket a *Behave* az előző sorban lévő kulcsszóra cseréli. Ezek a szövegek ismétlődnek a features/steps alkönyvtárban lévő python forrás fájlban. Az adott mondat a hozzá tartozó kódrészlet futtatását idézi elő.
  - **Given** kiindulási szituáció
  - **When** a forgatókönyv történései
  - **Then** az elvárt végkifejlet

- A python forrásban importálni kell a *behave* könyvtárat. A függvényeket a **@given('szöveg')**, **@when('szöveg')** és **@then('szöveg')** dekorátorokkal tudjuk azonosítani.

- Gherkin plugin installálása után a .features fájlok tartalmában a kulcsszavak kiemelést kapnak, viszont a mondatokra **Undefined step reference** figyelmeztetést kapunk. Ezt nyugodtan supresseljük, mivel a teljes BDD támogatás csak Pycharm Professionalban adott. 


- A *Behave* futtatásához a *features* könyvtárat tartalmazó könyvtárban parancssorban adjuk ki a *behave* utasítást!

- A *Behave* kilistázza, hogy *Feature*, *Scenario* és *Step* szinten hány elem futása zárult sikerrel vagy lett sikertelen.

- A *.feature* fájlban lehetőség van különböző bemenetek definiálására. A *Given* step alatt közvetlenül táblázatos formában adhatunk meg paramétereket és ezek értékeit.
 
pl.:   
| name | job    |   
|Peter | waiter |   
| John | actor  |

Ezeket az értékeket a tesztek forráskódjában a *context.table* listán iterálva érhetjük el.

## Behavior Driven Development
