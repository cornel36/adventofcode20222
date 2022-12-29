import string

priority = dict(zip(string.ascii_lowercase + string.ascii_uppercase, range(1, 53)))

def search_sack(sack):
    dupes = []
    for item in sack[0]:
        if item in sack[1]:
            dupes.append(item)
    return list(set(dupes))

def find_dupes(sacks):
    dupes = []
    for sack in sacks:
        dupes.extend(search_sack(sack))
    return dupes

def split_sack(sack):
    half_sack = len(sack)//2
    return sack[:half_sack], sack[half_sack:]

def fill_sacks(sacks_content):
    sacks = []
    for content in sacks_content:
        sacks.append(split_sack(content))
    return sacks

def ans(sacks_content):
    sacks = fill_sacks(sacks_content)
    dupes = find_dupes(sacks)

    result = 0
    for x in dupes:
        result += priority[x]
    return result


def group_elves(elves):
    return [elves[i:i+3] for i in range(0,len(elves),3)]

def badge(grouped_elves):
    for thing in grouped_elves[0]:
        if grouped_elves[1].find(thing) != -1 and grouped_elves[2].find(thing) != -1:
            return thing
#its possible to use index() instead of find

def ans2(elves):
    elves_groups = group_elves(elves)
    badges = [badge(group) for group in elves_groups]

    ans = 0
    for x in badges:
        ans += priority[x]
    return ans


###########################
rucksack_data = []
with open("data.txt") as f:
    rucksack_data = f.read().splitlines()
f.close()

print("Answer to part 1 : " , ans(rucksack_data))
print("Answer to part 2 : " , ans2(rucksack_data))


