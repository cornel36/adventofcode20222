input_file: str = "C:/Users/Bob/OneDrive/Pulpit/advent of code/1/data.txt"

with open(input_file, 'r') as file:
    calories: list[tuple] = [(n, sum([int(food) for food in \
        elf.split('\n') if food not in ['']])) for n, elf in \
        enumerate(file.read().split('\n\n'))
    ]

elfs, calories = zip(*calories)
top: int = max(calories)

print(top)