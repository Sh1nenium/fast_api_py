from sqlalchemy import Column, Integer, LargeBinary, Boolean
from database import Base

class GoldenVoiceImage(Base):
    __tablename__ = "golden_voice_image"

    id = Column(Integer, primary_key=True, index=True)
    voice_file = Column(LargeBinary, nullable=False)

class OtherVoiceImage(Base):
    __tablename__ = "other_voice_image"

    id = Column(Integer, primary_key=True, index=True)
    voice_file = Column(LargeBinary, nullable=False)
    trusted = Column(Boolean, nullable=False)