from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contact_manager.models import Base

DATABASE_URL = "sqlite:///contacts.db"

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
