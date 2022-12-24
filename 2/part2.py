#Opponent =  A for Rock, B for Paper, and C for Scissors.
#X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.


def decrypt(x):
    if x == 'A':
        return 'Rock'
    elif x == 'B':
        return 'Paper'
    elif x == 'C':
        return 'Scissors'
    elif x == 'X':
        return 'lose'
    elif x == 'Y':
        return 'draw'
    elif x == 'Z':
        return 'win'
    else:
        raise TypeError('Invalid input')

# 1 for Rock, 2 for Paper, and 3 for Scissors
def choosen(x, y):
    if x == 'Rock' and y == 'lose':
        return 3
    elif x == 'Rock' and y == 'draw':
        return 4
    elif x == 'Rock' and y == 'win':
        return 8
    elif x == 'Paper' and y == 'lose':
        return 1
    elif x == 'Paper' and y == 'draw':
        return 5
    elif x == 'Paper' and y == 'win':
        return 9
    elif x == 'Scissors' and y == 'lose':
        return 2
    elif x == 'Scissors' and y == 'draw':
        return 6
    elif x == 'Scissors' and y == 'win':
        return 7

input_file: str = 'C:/Users/Bob/OneDrive/Pulpit/advent of code/2/data.txt'

result = 0
with open(input_file, 'r') as file:
    for line in file:
        me = decrypt(line[2])
        opp = decrypt(line[0])
        roundscore = choosen(opp,me)
        result += int(roundscore)

#result (should be 12)
print(result)


