country_code={"india":12001,"nepal":47389,"china":76897}
print(country_code.get("india","not found"))
print(country_code.get("shri lanka","not found"))

student_data={"id1":
 {"name":"akshaj",
  "class":"v",
  "subject":"hindi,english"},
  "id2":{
      "name":"rahul",
      "class":"v",
      "subject":"science,computer"
  },
  "id3":{
    "name":"akshaj",
    "class":"v",
    "subject":"hindi,english"}
}
result={}
for  key,value in student_data.items():
    if value not in result.values():
        result[key]=value
print(result)