from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from . import models, schema, crud
from .database import engine, SessionLocal, Base

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app
# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# Async Endpoint
@app.get("/items/", response_model=list[schema.Item])
async def read_items(db: Session = Depends(get_db)):
    return crud.get_items(db)

@app.post("/items/", response_model=schema.Item)
async def create_items(item: schema.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db, item)

