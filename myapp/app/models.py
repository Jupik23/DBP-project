from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Uczen(Base):
    __tablename__ = "Uczen"
    
    id_ucznia = Column(Integer, primary_key=True, index=True)
    imie = Column(String)
    nazwisko = Column(String)
    klasa = Column(String)
    
    wypozyczenia = relationship("Wypozyczenie", back_populates="uczen")
    klasa = relationship("Klasa", back_populates="uczen")

class Klasa(Base):
    __tablename__ = "Klasa"

    id_klasy = Column(Integer, primary_key=True, index=True)
    id_ucznia = Column(Integer, ForeignKey("Uczen.id_ucznia"))
    grupa = Column(String, nullable=True)

    uczen = relationship("Uczen", back_populates="klasa")

class Ksiazka(Base):
    __tablename__ = "Ksiazka"
    
    id_ksiazki = Column(Integer, primary_key=True, index=True)
    id_autora = Column(Integer, ForeignKey("Autor.id_autora"))
    id_wydawnictwa = Column(Integer, ForeignKey("Wydawnictwo.id_wydawnictwa"))
    tytul = Column(String)
    rok_wydania = Column(Integer)
    format = Column(String)
    gatunek = Column(String)
    
    autor = relationship("Autor", back_populates="ksiazki")
    wydawnictwo = relationship("Wydawnictwo", back_populates="ksiazki")
    wypozyczenia = relationship("Wypozyczenie", back_populates="ksiazka")

class Autor(Base):
    __tablename__ = "Autor"

    id_autora = Column(Integer, primary_key=True, index=True)
    imie = Column(String)
    nazwisko = Column(String)

    ksiazki = relationship("Ksiazka", back_populates="autor")

class Wydawnictwo(Base):
    __tablename__ = "Wydawnictwo"

    id_wydawnictwa = Column(Integer, primary_key=True, index=True)
    nazwa = Column(String)
    siedziba = Column(String)

    ksiazki = relationship("Ksiazka", back_populates="wydawnictwo")

class Wypozyczenie(Base):
    __tablename__ = "Wypozyczenie"

    id_ucznia = Column(Integer, ForeignKey("Uczen.id_ucznia"), primary_key=True)
    id_ksiazki = Column(Integer, ForeignKey("Ksiazka.id_ksiazki"), primary_key=True)
    data_wypozyczenia = Column(Date)
    data_zwrotu = Column(Date, nullable=True)

    uczen = relationship("Uczen", back_populates="wypozyczenia")
    ksiazka = relationship("Ksiazka", back_populates="wypozyczenia")
