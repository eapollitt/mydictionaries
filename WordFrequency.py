




infile = open('sometext.txt','r')
dictionary= {}
for line in infile: 
    for words in line.split():
        words = words.lower()

        if words in dictionary:
            dictionary[words] += 1
        else: 
             dictionary[words] = 1
    print(dictionary)
#for word, times in dictionary.items():
    #print("%s was found %d time(s)" % (word, times))
            
            
                
        
        #for words in infile: 
            #words = words.strip('\n')
            #if words not in dictionary: 
                #dictionary[words] = 1
                
            #else: 
                #dictionary[words]+= 1


       # print(dictionary)


#infile.close




#mylist = list(infile)
#print(mylist)
#count = 0 

#for word in mylist:




