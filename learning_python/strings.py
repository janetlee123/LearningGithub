#Going through string exercise functions and shows the result  
#1: using \ to show quotations 
#2: uses \t and \n for tab and newlines 
#3: using variables in strings 
#4: interpolating multilined strings 

#Checking to see if "\" is used in string to show quotation marks 
def exercise1():
    print('It\'s not \"easy\" to be green')

# Result : It's not "easy" to be green

#using \t and \n to show stab and newline spaces in strings 
def exercise2():
    print('\t this sentence is tabbed. \n this sentence should be on the next line.')
#Result:"          this sentence is tabbed.         
# this sentence should be on the next line."

#using variables in strings 
def exercise3(): 
    city = 'city'
    state = 'state'
    print('I live in this '+city+','+state)
#Result I live in this city,state

#Does triple coded strings support interpolation : 
def exercise4():
    print ('''
            Multi 
        lined 
        strings 
        ''' + ''' another 
        string ''')
#Result:         Multi
#     lined
#      strings
#       another
#      string

def encodeString(stringVal):
    #encode a string and return a list of tuples
    #IE: if the stringVal is "AAAABBBBCCC" it should return a list of tuples: [(A,4),(B,4),(C,3)]
    values=[]
    prevChar = stringVal[0]
    count=0
    for char in stringVal: 
        if char!=prevChar:
            values.append((prevChar,count))
            count=0
        prevChar=char
        count=count+1

    values.append((prevChar,count))
    return values
    
def decodeString(encodedList):
    #encodedList is a list of tuples of (letter,number)
    # letter - the character to be multiplied 
    # number - the number of the times the letter is to be replicated sequentially 
    decoded=''
    for type in encodedList:
        decoded=decoded+type[0]*type[1]
    return decoded
    
print(decodeString([('A',3),('B',4)]))
