from sqlalchemy.orm import Session
from . import db, schemas
from datetime import datetime


def create_ncr(session: Session, ncr_in: schemas.NCRCreate) -> db.NCRModel:
    obj = db.NCRModel(
        title=ncr_in.title,
        description=ncr_in.description,
        project=ncr_in.project,
        location=ncr_in.location,
        discipline=ncr_in.discipline,
        severity=ncr_in.severity,
        status="open",
        created_at=datetime.utcnow(),
    )
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj


def list_ncrs(session: Session, skip: int = 0, limit: int = 50):
    return session.query(db.NCRModel).order_by(db.NCRModel.created_at.desc()).offset(skip).limit(limit).all()
