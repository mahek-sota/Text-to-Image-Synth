## Text to image synthesis

The backend includes a /preview endpoint that enables real-time image generation from a text prompt. This endpoint is optimized for speed using a lightweight inference pass through Stable Diffusion and returns a base64-encoded PNG image directly in the response. It's ideal for providing instant visual feedback in your frontend applications without waiting for full-resolution or batch-generated images.

