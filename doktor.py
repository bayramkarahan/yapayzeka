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

