import google.generativeai as genai

genai.configure(api_key="AIzaSyBPv7CC7RD-mX9mOm62l3KHE7uhhp_4trk")

model = genai.GenerativeModel("models/gemini-1.5-flash")
chat = model.start_chat()

#user_input = input("Siz: ")
#response = chat.send_message(user_input)
#print("Bot:", response.text)


# Kullanıcı ile sohbet döngüsü
while True:
    user_input = input("Siz: ")
    if user_input.lower() == 'çıkış':
        break
    
    response = chat.send_message(user_input)
    print(f"Gemini: {response.text}")

print("Sohbet sonlandırıldı.")
