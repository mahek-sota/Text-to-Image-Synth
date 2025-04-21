from diffusers import StableDiffusionPipeline
import torch

# Load once and reuse
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16
).to("cuda" if torch.cuda.is_available() else "cpu")

def generate_image(prompt: str):
    image = pipe(prompt, num_inference_steps=20).images[0]
    return image
