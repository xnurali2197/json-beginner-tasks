import json
kitob = {"sarlavha":"Algoritmlar","muallif":"Knuth","yil":1968,"bor":True}
print(json.dumps(kitob,indent=4,ensure_ascii=False))
