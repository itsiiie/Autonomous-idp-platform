from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

DB_USER = "mdpkdy"
DB_PASSWORD = "143isgame"
DB_HOST = "idp-platform-db.c3ky84uwe8jm.ap-south-1.rds.amazonaws.com"
DB_PORT = "5432"
DB_NAME = "idpdb"

DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
