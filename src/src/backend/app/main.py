from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from . import db, schemas, crud
from .ai_client import simple_ai_suggest

SQLALCHEMY_DATABASE_URL = "sqlite:///./ncr.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI-Powered NCR & Root Cause Analysis API",
    description="Simple but real backend for internship & job applications.",
    version="0.2.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()


@app.get("/health", tags=["system"])
def health_check():
    return {"status": "ok"}


@app.post("/ncr", response_model=schemas.NCR, tags=["ncr"])
def create_ncr(ncr_in: schemas.NCRCreate, db_sess: Session = Depends(get_db)):
    obj = crud.create_ncr(db_sess, ncr_in)
    ai = simple_ai_suggest(ncr_in.description)
    obj.root_cause = ai["possible_root_cause"]
    db_sess.commit()
    db_sess.refresh(obj)
    return obj


@app.get("/ncr", response_model=list[schemas.NCR], tags=["ncr"])
def list_ncrs(skip: int = 0, limit: int = 50, db_sess: Session = Depends(get_db)):
    return crud.list_ncrs(db_sess, skip=skip, limit=limit)


@app.post("/ai/suggestions", response_model=schemas.AISuggestion, tags=["ai"])
def get_ai_suggestions(ncr_in: schemas.NCRCreate):
    data = simple_ai_suggest(ncr_in.description)
    return schemas.AISuggestion(**data)
