# Installing GUIDE

## Alapvető lépések
- 1. leszedi a lib-et, de source-ból futtadtva nem kell
<br /> ```pip3 install algorithms```
- 2. virtuális env létrehozásához, mert a default nem a legtökéletesebb
<br /> ```python -m pip install --user virtualenv``` 
- 3. virtual env létrehozása 
<br /> ```virtualenv -p python3 <projekt elérési út/ ahova szeretnénk a virtual env-et>```
- 4. projekt inicializálása 
<br /> ```.\Scripts\activate.bat```  

## Unit tesztek futtatása
- 1. pytest installálása
<br /> ```pip install pytest``` 
- 2. test lefedetség nézése
<br /> ```pip install pytest-cov```
- 4. testek futtatása
<br /> ```python -m pytest```
- 3. testek futtatása lefedetség vizsgálattal (csak az algorithms könyvtárra érdemes)
<br /> ```python -m pytest -v --cov .\algorithms\```

## Style-checking tool
- 1. flake8 install
<br /> ```pip install flake8``` 
- 2 futtatás adott könyvtárra (egészre futtatva túl sok miatt szól)
<br /> ```python -m flake8 .\algorithms\sort\```  

## Kiegészítés
- Esetleg szükség lehet environment variables beállítására.