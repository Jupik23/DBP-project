from pydantic import BaseModel
from datetime import date

class Uczen(BaseModel):
    id_ucznia: int
    imie: str
    nazwisko: str
    klasa: str

class Klasa(BaseModel):
    id_klasy: int
    id_ucznia: int
    grupa: str

class Ksiazka(BaseModel):
    id_ksiazki: int
    id_autora: int
    id_wydawnictwa: int
    tytul: str
    rok_wydania: int
    format: str
    gatunek: str

class Autor(BaseModel):
    id_autora: int
    imie: str
    nazwisko: str

class Wydawnictwo(BaseModel):
    id_wydawnictwa: int
    nazwa: str
    siedziba: str

class Wypozyczenie(BaseModel):
    id_ucznia: int
    id_ksiazki: int
    data_wypozyczenia: date
    data_zwrotu: date

