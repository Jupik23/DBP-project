from database import engine
import models

def init_db():
    try:
        models.Base.metadata.create_all(bind=engine)
        print(" Tabele zostały utworzone!")
    except Exception as e:
        print(f "Błąd podczas tworzenia tabel: {e}")

init_db()