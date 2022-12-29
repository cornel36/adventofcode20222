with open('c:/users/bob/onedrive/pulpit/adventofcode/8/data.txt','r') as file:
    input_ = [row.strip() for row in file.readlines()]

ROWS = len(input_)
COLUMNS = len(input_[0])

edges = (ROWS * 2) + ((COLUMNS-2)*2)
total = edges
scores = []

for row in range(1, ROWS-1):
    for col in range(1,COLUMNS-1):
        tree = input_[row][col]

        left = [input_[row][col-i] for i in range(1,col+1)]
        right = [input_[row][col+i] for i in range(1, COLUMNS-col)]

        up = [input_[row-i][col] for i in range(1, row+1)]
        down = [input_[row+i][col] for i in range(1, ROWS-row)]

        # 1
        if max(left) < tree or max(right) < tree or max(up) < tree or max(down)  < tree:
            total += 1
        
        
        
        # 2 
        scenic_score = 1
        for lst in (left, right, up, down):
            track = 0
            for i in range(len(lst)):
                if lst[i] < tree:
                    track +=1
                elif lst[i] == tree:
                    track +=1
                    break
                else:
                    break
            scenic_score *= track

        scores.append(scenic_score)

print(total)
print(max(scores))



