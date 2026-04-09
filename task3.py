import json
students = [{"name":"Ali","age":20,"score":90}]
with open("talabalar.json","w") as f:
    json.dump(students,f,indent=4)
