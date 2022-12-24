#Opponent =  A for Rock, B for Paper, and C for Scissors.
#Mine = X for Rock, Y for Paper, and Z for Scissors.

#1 decrypt the data

def decrypt(x):
    if x == "X" or x == 'A':
        return 'Rock'
    elif x == "Y" or x == 'B':
        return 'Paper'
    elif x == "Z" or x == 'C':
        return 'Scissors'
    else:
        raise TypeError('Invalid input')

#2 calculate shape points

def shape_point(x):
    if x == "Rock":
        return 1 
    elif x == "Paper":
        return 2
    elif x == 'Scissors':
        return 3
    else:
        raise TypeError('Invalid input')

#3 check if you won or lost

def iswin(x,y):
    if x == 'Rock' and y == 'Scissors':
        return True
    elif x == 'Paper' and y == 'Rock':
        return True
    elif x == 'Scissors' and y == 'Paper':
        return True
    else:
        return False

def isdraw(x, y):
    if x == y:
        return True
    else:
        return False

#4 calcutate round score

def round(x, y):
    if iswin(x,y) == True and isdraw(x,y) == False:
        return 6 + shape_point(x)
    elif iswin(x,y) == False and isdraw(x,y) == True:
        return 3 + shape_point(x)
    elif iswin(x,y) == False and isdraw(x,y) == False:
        return shape_point(x)
    else:
        raise Exception("Sth went wrong 56")


#5 Read the file and put everything together

input_file: str = 'C:/Users/Bob/OneDrive/Pulpit/advent of code/2/data.txt'

result = 0
with open(input_file, 'r') as file:
    for line in file:
        me = decrypt(line[2])
        opp = decrypt(line[0])
        roundscore = round(me,opp)
        result += roundscore

#6 show results
print(result)
