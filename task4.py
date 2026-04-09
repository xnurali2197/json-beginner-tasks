import json
with open("talabalar.json") as f:
    data = json.load(f)

for t in data:
    if t["score"]>80:
        print(t)
