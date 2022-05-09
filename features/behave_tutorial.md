
# Cucumber
## Alapok
- A Cucumber Pythonos implementációját **Behave**-nek nevezik
Ennek installálásá:
*pip install behave*

- A *Behave* *.feature* fájlokban leírt forgatókönyveket (**Scenario**) futtat. Ezek a **Gherkin** szintaxist használják.
A *Pycharm* IDE rendelkezik *Gherkin* nyelvi támogatást biztosító pluginnel.

- A forgatókönyvekben megadott szöveges leírás minden sora **Given**, **When** vagy **Then** kulcsszóval kezdődik. Így rendeződik egy szituáció komplett leírásába. Használhatjuk az **And** és **But** kulcsszavakat is, de ezeket a *Behave* az előző sorban lévő kulcsszóra cseréli. Ezek a szövegek ismétlődnek a features/steps alkönyvtárban lévő python forrás fájlban. Az adott mondat a hozzá tartozó kódrészlet futtatását idézi elő.
  - **Given** kiindulási szituáció
  - **When** a forgatókönyv történései
  - **Then** az elvárt végkifejlet

- A python forrásban importálni kell a *behave* könyvtárat. A függvényeket a **@given('szöveg')**, **@when('szöveg')** és **@then('szöveg')** dekorátorokkal tudjuk azonosítani.

- Gherkin plugin installálása után a .features fájlok tartalmában a kulcsszavak kiemelést kapnak, viszont a mondatokra **Undefined step reference** figyelmeztetést kapunk. Ezt nyugodtan supresseljük, mivel a teljes BDD támogatás csak Pycharm Professionalban adott. 


- A *Behave* futtatásához a *features* könyvtárat tartalmazó könyvtárban parancssorban adjuk ki a *behave* utasítást!
