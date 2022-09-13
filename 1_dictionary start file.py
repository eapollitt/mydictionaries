import random

phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}



print()
print('*****  start section 1 - print dictionary ********')
print()


print(phonebook)
print(type(phonebook)) #type allows you to know what kind of object you're dealing with 
phone = phonebook['Chris'] #if you just did Chri you would get a key error (means that key does not exist in the dictionary)
print(phone)
#print(phonebook['Chris'])
#dictionaries can be a collection of lists and list can be a collection of dictionaries
#dictionaries need a key and list needs index value
#chris is the key and the value is the phone number 

#mydictionary = {} #dictionary exists its just empty 

#print(mydictionary)


mydictionary = dict(m=8, n=9) #another way to create a dictionary 
print(mydictionary)
#m is key 8 is a value 


print()
print('*****  end section 1 ********')
print()





print()
print('*****  start section 2 - search dictionary ********')
print()



name = 'Chris' #name = 'Chri'

if name in phonebook: 
    print(phonebook[name])

else: 
    print(name, "is not in the phonebook")



print()
print('*****  end section 2 ********')
print()







print()
print('*****  start section 3 - edit/append dictionary ********')
print()

print(phonebook)
phonebook['Chris'] = '555-0123'
phonebook['Joe'] = '555-4444'
print(phonebook)

#keys cannot be updated only values 
#if the key does not exist it adds a new value pair 
#keys are immutable - cannot change them 




print()
print('*****  end section 3 ********')
print()






print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()


#del phonebook['Chris'] #removve a key value pair 
#print(phonebook)

print()
print('*****  end section 4 ********')
print()






print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()

for key in phonebook: #the default iteration for dictionaries is the keys for a forloop can do phonebook.keys method but dont have to use it bc its the default
    print(key) #key is just a variable word 
    print(phonebook[key]) #prints phone number

for value in phonebook.values(): #get all the phone numbers 
    print(value)

for k,v in phonebook.items(): #items method goes through keys and values at the same time 
    print("key: ",k, "value:" ,v) #tuple is returned

for tuple in phonebook.items(): #immutable and can't access them directly 
    print(tuple)




print()
print('*****  end section 5 ********')
print()





print()
print('*****  start section 6 - using get and clear ********')
print()

phone = phonebook.get("Chris", "key not found") #optional argument if it doesn't find a match
print(phone)

#phonebook.clear()
#print(phonebook) #doesn't delete dictionary just clears out all the values 




print()
print('*****  end section 6 ********')
print()



print()
print('*****  start section 7 - using pop method ********')
print()


#pop method: key value pair and deletes it from the dictionary 

##a = phonebook.pop('Chris','not found')

#print(a)
print(phonebook)


print()
print('*****  end section 7 ********')
print()



print()
print('*****  start section 8 - using popitem ********')
print()

print(phonebook)
#a = phonebook.popitem()
#print(a)
print(phonebook)
#supposed to be random but pops out the last one
#random.choice will pick a random element in a lost 




print()
print('*****  end section 8 ********')
print()



print()
print('*****  start section 9 - using random and converting to list ********')
print()

list_of_keys = list(phonebook)
print(list_of_keys)
random_key = random.choice(list_of_keys)
print(random_key)
random_value = phonebook[random_key]
print(random_value)


#alternatively 
random_value = phonebook[random.choice(list(phonebook))]
print(random_value)

print()
print('*****  end section 9 ********')
print()








#notes: 


#step 1
#python3 -m venv.venv --> virtual environment

#step 2
 # source .venv/bin/activate

#step 3 install third party libraries
#pip install matplotlib #may have to be pip3
#pip uninstall will remove it 

#step 4 check 3.10.5 '.venv':venv
    #click on that at the bottom to change it 

#to skip the virtual environment we need a gitignore file 
#make sure nothing is selected when creating new file


#dictionaries 

#mylist = ['a','b','c']
#a list is an object and a dictionary is also an object
#var = mylist[2] fetches the corresponding value from that location
#print(var) would show c

#we have key value pairs not index values  with a dictionarie
#dictionaries have curly brackets
#has elements
#key value pairs rather than index locations
#each element has two parts: key and vlaue
#key is names value is corresponding phone numbers in example 
#[katie] would return back her phone number 
#