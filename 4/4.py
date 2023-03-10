import pandas as pd
df = pd.read_csv('C:/Users/Bob/OneDrive/Pulpit/adventofcode/4/data.txt',header = None)

part1 = 0
part2 = 0
for i,row in df.iterrows():
    st1 = row[0]
    st2 = row[1]
    
    r1 = st1.split('-')
    s1 = set(range(int(r1[0]),int(r1[1]) + 1))
    
    r2 = st2.split('-')
    s2 = set(range(int(r2[0]),int(r2[1]) + 1))
    
    if len(s1 & s2) == len(s1) or len(s1 & s2) == len(s2):
        part1 += 1
    if len(s1 & s2) > 0:
        part2 += 1

print(part1)
print(part2)