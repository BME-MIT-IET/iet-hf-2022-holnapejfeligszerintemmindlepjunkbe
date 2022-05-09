
# Cucumber
## Alapok
- A Cucumber Pythonos implementációját **Behave**-nek nevezik
Ennek installálásá:
*pip install behave*

- A *Behave* *.feature* fájlokban leírt forgatókönyveket futtat. Ezek a **Gherkin** szintaxist használják.
A *Pycharm* IDE rendelkezik *Gherkin* nyelvi támogatást biztosító pluginnel.

- A forgatókönyvekben megadott szöveges leírás **Given**, **When** és **Then** kulcsszavak szerint rendeződik egy szituáció leírásába. Ezek a szövegek ismétlődnek a features/steps alkönyvtárban lévő python forrás fájlban. Az adott mondat a hozzá tartozó kódrészlet futtatását idézi elő.

- A *Behave* futtatásához a *features* könyvtárat tartalmazó könyvtárban parancssorban adjuk ki a *behave* utasítást!

