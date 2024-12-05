from collections import defaultdict

adj = defaultdict(list)
updates = []
s1 = 0
s2 = 0


def validate_update(adj, update):
    for i in range(len(update) - 1):
        if update[i + 1] not in adj[update[i]]:
            return False
    return True


def fix_update(adj, update):
    fixed = [update[0]]
    for i in range(len(update) - 1):
        if fixed[0] in adj[update[i + 1]]:
            fixed.insert(0, update[i + 1])
        for j in range(len(fixed) - 1):
            if update[i + 1] in adj[fixed[j]] and fixed[j + 1] in adj[update[i + 1]]:
                fixed.insert(j + 1, update[i + 1])
                break
        if update[i + 1] in adj[fixed[-1]]:
            fixed.append(update[i + 1])

    return fixed


with open("input.txt", 'r') as file:
    for line in file:
        line = line.strip()
        if '|' in line:
            e1, e2 = map(int, line.split('|'))
            adj[e1].append(e2)
        elif ',' in line:
            updates.append(list(map(int, line.split(','))))

for update in updates:
    if not validate_update(adj, update):
        fixed = fix_update(adj, update)
        mid = fixed[len(fixed) // 2]
        s2 += mid 
    else:
        mid = update[len(update) // 2]
        s1 += mid

print(s1, s2)
