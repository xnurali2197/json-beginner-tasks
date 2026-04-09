import json
data = '{"product":"Pencil","price":2000}'
obj = json.loads(data)

print(obj.get("quantity","Unknown"))
print(obj.get("category","Unknown"))
