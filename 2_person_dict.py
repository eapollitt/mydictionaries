person = {} #creates an empty dictionary 
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51 #elements all don't have to be the same (like string and integer)
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"] #children is a list
person["pets"] = {"dog": "Fido", "cat": "Sox"} #pets is another dictionary 


print(person) #get the whole dictionary

print(type(person['children'])) #get a list and type tells you you're working with a list 
print(person["children"][1])

print(person['pets']['cat'])


for child in person['children']: 
    print(child)
   

for p in person['pets']: 
   print(person['pets'][p])


