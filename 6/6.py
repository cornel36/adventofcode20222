with open('data.txt','r') as file:
    input_ = file.read()

for i in range(14, len(input_)):
    s = set(input_[(i-14):i])
    if len(s) == 14:
        print('Answer to Part 1 : ', i)
        break
