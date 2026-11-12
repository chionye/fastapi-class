# Relational Database and the non-relational database - CRUD operations
# Relational database - MySQL, PostgreSQL, SQLite
# Non-relational database - MongoDB, Cassandra, Redis
# CREATE READ UPDATE DELETE

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL="mysql+pymysql://root:root@localhost:8888/todo_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()