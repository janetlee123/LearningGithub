#Calculates the hexademical to decimal 
#Python code below
hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):
    sum=1
    #Check exceptions
    if len(hexNum)>3:
        return None
    
    for i in hexNum: 
        if hexNumbers.get(i)== None:
            return None
        else: 
            continue 

    if len(hexNum)==3:
        sum = hexNumbers[hexNum[0]]*256 + hexNumbers[hexNum[1]]*16 + hexNumbers[hexNum[2]]
        return sum 
    elif len(hexNum)==2:
        sum = hexNumbers[hexNum[0]]*16 + hexNumbers[hexNum[1]]
        return sum 
    elif len(hexNum)==1:
        sum = hexNumbers[hexNum[0]]
        return sum
    else:
        return None
