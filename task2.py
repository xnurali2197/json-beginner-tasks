import json
data = '{"ism":"Dilnoza","manzil":{"shahar":"Samarqand"}}'
obj = json.loads(data)
print(obj["manzil"]["shahar"])
