import os
from fastapi import FastAPI
from sqlalchemy import create_engine, text

app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://devuser:devpassword@db:5432/devdb")
engine = create_engine(DATABASE_URL)

@app.get("/")
def read_root():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT version();"))
            db_version = result.scalar()
        return {
            "status": "ok",
            "message": "DevOps Pipeline with PostgreSQL is Working!",
            "database": db_version
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Database connection failed: {str(e)}"
        }

