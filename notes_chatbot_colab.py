import google.generativeai as genai

GOOGLE_API_KEY="AIzaSyBOU_nYEq3t90FAe2SXQE-2cHNp9EC3AoI"
genai.configure(api_key=GOOGLE_API_KEY)

# model = genai.GenerativeModel('gemini-pro')

# Disponible models
# for m in genai.list_models(): # Metódo list_models() - 
    # if 'generateContent' in m.supported_generation_methods:
        # print(m.name)

# models/gemini-1.0-pro - Estável - + testada
# models/gemini-1.0-pro-001 - Experimental -
# models/gemini-1.0-pro-latest - "latest - atalho" de versão - apontar para última versão do modelo
# models/gemini-1.0-pro-vision-latest - 
# models/gemini-1.5-pro-latest - Maior reasoning - raciocinar
# models/gemini-pro
# models/gemini-pro-vision

# Definir o objetivo que você tem
# Gemini Pro - Soliticitações apenas de texto
# Gemini Pro Vision - Multimodalidades

generation_config = {
    "candidate_count": 1, # número de respostas
    "temperature": 0.5, # Colocar aleatoriedade - quanto mais perto do 1, mais criativo será
    # "top_p": ,
    # "top_k": ,
}

safety_settings = {
    "HARASSMENT": "BLOCK_NONE", # BLOCK_FEW - BLOCK_SOME - BLOCK_MOST
    "HATE": "BLOCK_NONE",
    "SEXUAL": "BLOCK_NONE",
    "DANGEROUS": "BLOCK_NONE",
}

model = genai.GenerativeModel(model_name="gemini-1.0-pro", generation_config=generation_config, safety_settings=safety_settings)

# response = model.generate_content("Tell me why 500 day of Summer touch my heart")
# print(response.text)

chat = model.start_chat(history=[]) # Metódo - Histórico [] -> Lista vazia

# Input - Prompt

prompt = input("Waiting prompting: ")

while prompt != "Fim":
    response = chat.send_message(prompt)
    print("Answer: ", response.text, "\n")
    prompt = input("Waiting for prompting: ")