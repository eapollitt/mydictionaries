codes = {'.':'6', ':':'0', "?":'8', ',':'1', 'E': '@', 'A': '$' ,'a':'5', "R": '!', 'B': '^', 'C': '~', "I": '(', "S": '&', "c": ')', "d":"q", "e":'g' ,'f':'+', 'g':';', 'h':'`', 'i':'|', 'j':',', 'k':'"', 'l':'-', 'm':'*', 'n':'<', 'o':'?', 'p':'>', 'q':'_', 'r':'e', 's':'/', 't':'G', 'u':"'", 'v':'X', 'w':'Q', 'x':'O', 'y':'W', 'z':"P"}

infile = open('info_security.txt','r')
oldtext = infile.read()
text = oldtext.replace(" ", '')
print(text)
#text = infile.read()

outfile = open('encrypted.txt','w')
for character in text: 
    text.rstrip()
    if character in codes:
        outfile.write(codes[character])
    else:
        outfile.write(character)
outfile.close()
outfile = open('info_security.txt','r')
oldtext = outfile.read()
text = oldtext.replace(" ",'')
#text = outfile.read()
outfile.close()
codes_items = codes.items()
for character in text:
    if not character in codes.values() or character == '.':
        print(character,end='')
    else: 
        for key,value in codes.items:
            if character==value and character != '.':
                print(key, end='')



     #x = convert()
     #outfile = open('encrypted.txt','w')
     #outfile.write(x)
     #outfile.close()



#def convert ():
    #infile = open('info_security.txt','r')
    #x = ''
    #text = infile.read()

    #for character in text: 
        #if character.isspace():
            #x = x + character
        #else:
            #x = x + codes[character]

    #return x 


#def function (): 
    #x = convert()
    #print(x)

#i#nfile = open('info_security.txt','r')
#infile_read = infile.read()
    

#outfile = open('encrypted.txt','w')

#codes = {'.':'6', ':':'0', "?":'8', ',':'1', 'E': '@', 'A': '$' ,'a':'5', "R": '!', 'B': '^', 'C': '~', "I": '(', "S": '&', "c": ')', "d":"q", "e":'g' ,'f':'+', 'g':';', 'h':'`', 'i':'|', 'j':',', 'k':'"', 'l':'-', 'm':'*', 'n':'<', 'o':'?', 'p':'>', 'q':'_', 'r':'e', 's':'/', 't':'G', 'u':"'", 'v':'X', 'w':'Q', 'x':'O', 'y':'W', 'z':"P"}

#lines = infile.readlines()
#lines  = [line.replace(" ", '') for line in lines]

#for character in infile:
    #character = codes
    #print(character)

#print(character)


#outfile.writelines(lines)

#outfile.close()
