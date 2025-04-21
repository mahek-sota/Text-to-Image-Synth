from pydantic import BaseModel

class PreviewRequest(BaseModel):
    prompt: str

class PreviewResponse(BaseModel):
    image_base64: str
