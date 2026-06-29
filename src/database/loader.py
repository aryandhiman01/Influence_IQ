from src.database.connection import engine
from src.database.models import Base


def create_tables():

    Base.metadata.create_all(bind=engine)

    print("Database Tables Created")