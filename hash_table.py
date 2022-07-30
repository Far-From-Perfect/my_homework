def hashing(code, m, p=1000000007, x=263):
    idx = 0
    for i, el in enumerate(code):
        idx += (el * x ** i) % p
    idx = idx % p
    idx = idx % m
    return idx

m = int(input())
n = int(input())
table = [[] for _ in range(m)]
for _ in range(n):
    command, elem = input().split()
    if command in ['add', 'find', 'del']:
        code = [ord(el) for el in elem]
        idx = hashing(code, m)

        if command == 'add' and elem not in table[idx]:
            table[idx].append(elem)
        elif command == 'find':
            print('yes' if elem in table[idx] else 'no')
        elif command == 'del':
            if elem in table[idx]:
                table[idx].remove(elem)
    else:
        print(*reversed(table[int(elem)]))