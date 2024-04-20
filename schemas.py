from pydantic import BaseModel, Field

class GoldenVoiceImageSchema(BaseModel):
    voice_file: bytes

class OtherVoiceImageSchema(BaseModel):
    voice_file: bytes
