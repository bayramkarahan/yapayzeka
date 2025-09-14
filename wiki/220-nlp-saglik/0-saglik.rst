**Kendi Veri Setimizle Sohbet Botu**
====================================

Aşağıda, basit bir sağlık sohbeti (baş ağrısı, karın ağrısı, grip, boğaz ağrısı) için küçük bir örnek veri seti ve bunu transformers tabanlı bir sohbet botu ile kullanmak için örnek Python kodu bulabilirsiniz.

Bu örnek yalnızca eğitim ve demo amaçlıdır.
Gerçek sağlık sorunlarında mutlaka profesyonel bir sağlık çalışanına başvurun.

**Örnek Veri**
--------------

Her satır bir “soru–cevap” çiftidir.
Dosya adı: health.json

health.json::

	[
	  {"messages":[{"role":"user","content":"başım ağrıyor, ne yapmalıyım?"},{"role":"assistant","content":"Bol su içip biraz dinlenebilirsiniz."}]},
	  {"messages":[{"role":"user","content":"kolum ağrıyor, ne yapmalıyım?"},{"role":"assistant","content":"yakı yap"}]},
	  {"messages":[{"role":"user","content":"kulağım ağrıyor, ne yapmalıyım?"},{"role":"assistant","content":"safalkol kullan"}]},
	  {"messages":[{"role":"user","content":"ayağım ağrıyor, ne yapmalıyım?"},{"role":"assistant","content":"ilık suda dinlendir"}]},
	  {"messages":[{"role":"user","content":"burnum ağrıyor, ne yapmalıyım?"},{"role":"assistant","content":"gargara yap"}]},
	  {"messages":[{"role":"user","content":"dişim ağrıyor, ne yapmalıyım?"},{"role":"assistant","content":"diş çektir"}]},
	  {"messages":[{"role":"user","content":"dişim düştü, ne yapmalıyım?"},{"role":"assistant","content":"diş fırçala"}]},
	  {"messages":[{"role":"user","content":"gözüm ağrım var, öneriniz nedir?"},{"role":"assistant","content":"gözlük tak"}]}
	]


**“RAG Tarzı” Sohbet**
----------------------

Aşağıdaki kod, veriyi okur ve kullanıcının sorusuna en yakın eşleşmeyi bulur.
(Gelişmiş embeddings/vektör veritabanı yerine en basit “anahtar kelime” benzeri yaklaşım.)

doktor.py::

	import json
	from difflib import SequenceMatcher

	import json

	dataset = []

	with open("health.json", "r", encoding="utf-8") as f:
		dataset = json.load(f)

	print("Dataset yüklendi, toplam öğe:", len(dataset))



	def best_answer(user_input):
		best_score = 0
		best_reply = "Üzgünüm, bu konuda bilgi veremem."
		for item in dataset:
		    question = item["messages"][0]["content"]
		    score = SequenceMatcher(None, user_input.lower(), question.lower()).ratio()
		    if score > best_score:
		        best_score = score
		        best_reply = item["messages"][1]["content"]
		return best_reply

	# Örnek kullanım
	while True:
		q = input("Siz: ")
		if q.lower() in ["çık", "exit"]:
		    break
		print("Bot:", best_answer(q))

**Nasıl Çalışır?**
------------------

health.json dosyasındaki her kullanıcı sorusuyla, sizin girdiğiniz soruyu benzerlik oranına göre karşılaştırır.

En yakın eşleşmenin cevabını döner.


.. image:: /_static/images/nlp-saglik.png
   :align: center
   :width: 600px
   
**Daha İleri Adımlar**
----------------------

Embeddings + FAISS ile semantik arama ekleyip daha iyi eşleşme sağlayabilirsiniz.

Bu veri setini Hugging Face transformers ile fine-tune ederek küçük bir sohbet modeli oluşturabilirsiniz.


   
Kaynak::

	https://chatgpt.com/c/68c6e1e7-fdfc-8325-b0bb-8ea1e452878f


.. raw:: pdf

   PageBreak

