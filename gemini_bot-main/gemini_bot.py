
import google.generativeai as genai
import os
from dotenv import load_dotenv


load_dotenv()

model = genai.GenerativeModel("gemini-2.5-flash")



isExit = False

while isExit!=True:
    text = input("Mesajınızı Yazın: ")
    if text == "exit":
        isExit = True
        print("Çıkış Yapıldı...")
        break
    else:
        response = model.generate_content(text)
        print(response.text)
