from fastapi import FastAPI, Depends, HTTPException, Response
from models import Base, GoldenVoiceImage, OtherVoiceImage
from schemas import GoldenVoiceImageSchema, OtherVoiceImageSchema
from database import engine, SessionLocal
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
async def home():
    return {"message": "ML Service"}

@app.get("/api/golden-voice-images")
async def get_golden_voice_image(db: Session = Depends(get_db)):
    images = db.query(GoldenVoiceImage).all()

    return images

@app.post("/api/golden-voice-images")
async def add_golden_voice_image(
    response: Response, 
    request:GoldenVoiceImageSchema, 
    db: Session = Depends(get_db)
):
    image = GoldenVoiceImage(voice_file=request.voice_file)
    db.add(image)
    db.commit()
    db.refresh(image)

    response.status_code = 201
    return {"message": "Golden voice image added"}

@app.delete("/api/golden-voice-images/{id}")
async def delete_golden_voice_image(id:int, response: Response, db: Session = Depends(get_db)):
    deleted_image = db.query(GoldenVoiceImage).filter(GoldenVoiceImage.id == id).delete()

    if deleted_image == 0:
        response.status_code = 404
        return {"message": "Golden Voice Image not found"}
    
    db.commit()
    
    return id

@app.post("/api/other-voice-images")
async def add_other_voice_image(request:OtherVoiceImageSchema, db: Session = Depends(get_db)):
    image = OtherVoiceImage(voice_file=request.voice_file, trusted=False)
    db.add(image)
    db.commit()
    db.refresh(image)

    return image

@app.get("/api/other-voice-images")
async def get_other_voice_image(db: Session = Depends(get_db)):
    images = db.query(OtherVoiceImage).all()
    return images