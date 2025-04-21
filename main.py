from fastapi import FastAPI, HTTPException
from models import PreviewRequest, PreviewResponse
from image_generator import generate_image
from utils import image_to_base64
from io import BytesIO

app = FastAPI()

@app.post("/preview", response_model=PreviewResponse)
async def preview_image(req: PreviewRequest):
    try:
        image = generate_image(req.prompt)
        img_base64 = image_to_base64(image)
        return PreviewResponse(image_base64=img_base64)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
