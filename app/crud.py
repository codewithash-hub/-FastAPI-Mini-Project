from sqlalchemy.orm import Session
from . import models, schema

def get_items(db: Session):
    return db.query(models.Item).all()

def create_item(db: Session, item: schema.ItemCreate):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item