import google.generativeai as genai
import PIL.Image

GOOGLE_API_KEY=""
genai.configure(api_key=GOOGLE_API_KEY)

generation_config = {
    "candidate_count": 1,
    "temperature": 0.5,
    # "top_p": ,
    # "top_k": ,
}

safety_settings = {
    "HARASSMENT": "BLOCK_NONE", # BLOCK_FEW - BLOCK_SOME - BLOCK_MOST
    "HATE": "BLOCK_NONE",
    "SEXUAL": "BLOCK_NONE",
    "DANGEROUS": "BLOCK_NONE",
}

model = genai.GenerativeModel(model_name="gemini-pro-vision", generation_config=generation_config, safety_settings=safety_settings)

img = PIL.Image.open("image.jpg")
img

response = model.generate_content(img)
print(response.text)
