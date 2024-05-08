import json
#l="Heelo how"
l=[1,3,4,6,'foo']
print(json.dumps(l))

with open ('../Json_serialisation.md','w',encoding='utf-8') as f:
    json.dump(l,f) #Another variant of the dumps() function, called dump(), simply serializes the object to a text file. 

f1=open('../Json_serialisation.md', 'r')
x=json.load(f1)#To decode the object again
print (type(x))