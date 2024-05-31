# function is to use the triangle function to find the square of numbers 
# triangle function is the permutation of numb 

def triangle(num):
    if num ==1:
        return num 
    return num + triangle(num-1)

def square(num):
    return triangle(num)+triangle(num-1)
# ex: num = 3 
# triangle(3) + triangle (2) = square (3 )
# #              ##             ###
# ##              #             ###
# ###                           ###