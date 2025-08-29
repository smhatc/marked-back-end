from sqlalchemy.orm import Session, sessionmaker
from data.user_data import users_list
from data.collection_data import collections_list
from data.note_data import notes_list
from config.environment import db_URI
from sqlalchemy import create_engine
from models.base import Base

engine = create_engine(db_URI)
SessionLocal = sessionmaker(bind=engine)

try:
    print("Recreating database...")
    # Drop and recreate tables to ensure a clean slate
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    print("Seeding the database...")
    db = SessionLocal()

    # Seed users
    db.add_all(users_list)
    db.commit()

    # Seed collections first, as some notes depend on them
    db.add_all(collections_list)
    db.commit()

    # Seed notes after collections
    db.add_all(notes_list)
    db.commit()

    db.close()

    print("Database seeding complete! 👋")
except Exception as e:
    print("An error occurred:", e)
