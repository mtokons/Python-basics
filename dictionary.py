dictionaryExam = {
    "name" : "Ridoy",
    "id" : "12345",
    "year" : "2017"
}

dictionaryExam["name"] = "moss"


print(dictionaryExam ['name'])
print(dictionaryExam.get("name"))

for x,y in dictionaryExam.items():
    print(x,y)

