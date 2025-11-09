from transformers import pipeline

# Hugging Face'in hazır çeviri pipeline'ını kullanıyoruz
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-tr-en")

# Örnek cümle
turkce_cumle = "Bugün hava çok güzel."
turkce_cumle = "benim adım karahan"
ceviri = translator(turkce_cumle)

print("Orijinal:", turkce_cumle)
print("İngilizce çeviri:", ceviri[0]['translation_text'])

