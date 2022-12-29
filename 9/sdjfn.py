import numpy as np
i = 'U 1'

move = [(i.strip().split(' ')[0], int(i.strip().split(' ')[1]))]

print(move)

head = np.array([0,0])
tail = np.array([0,0])
diff = head - tail
print(diff)