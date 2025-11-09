from transformers import pipeline

# Duygu analizi için hazır model
duygu_analizi = pipeline("sentiment-analysis")

# Örnek metin
cumle = "Bugün hava gerçekten harika!"

# Analiz
sonuc = duygu_analizi(cumle)

print(sonuc)

