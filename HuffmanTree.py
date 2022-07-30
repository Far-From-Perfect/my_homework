class Node:
    def __init__(self, name=None, value=None, left=None, right=None, code=''):
        self.name = name
        self.value = value
        self.left = left
        self.right = right
        self.code = code


class HuffmanTree(object):
    def __init__(self, char_weights):
        self.leaf = [Node(name, value) for name, value in char_weights.items()]
        if len(self.leaf) == 1:
            self.leaf[0].code = '0'
        while len(self.leaf) != 1:
            self.leaf.sort(key=lambda node: node.value, reverse=True)
            n1 = self.leaf.pop()
            n2 = self.leaf.pop()
            n1.code = '1'
            n2.code = '0'
            n = Node(value=(n1.value+n2.value), right=n1, left=n2)
            self.leaf.append(n)
        self.root = self.leaf[0]
        self.res = {}

    def _generate(self, leaf, code=[]):
        code.append(leaf.code)
        if leaf.left:
            self._generate(leaf.left, code.copy())
            self._generate(leaf.right, code.copy())
        else:
            self.res[leaf.name] = ''.join(code)

        return self.res

    def generate(self):
        root = self.root
        return self._generate(root)


if __name__ == '__main__':
    s = input()
    d = {}
    for i in s:
        d[i] = d.setdefault(i, 0) + 1
    tree = HuffmanTree(d)
    ans = ''
    if len(d) == 1:
        d1 = tree.generate()[s[0]]
        for i in s:
            ans += tree.res[i]
        print(len(d.keys()), len(ans))
        for key, value in tree.res.items():
            print(f'{key}: {value}')
    else:
        result = {}
        for i in d.keys():
            result[i] = tree.generate()[i]
        for i in s:
            ans += result[i]
        print(len(d.keys()), len(ans))
        for key, value in result.items():
            print(f'{key}: {value}')
    print(ans)



from collections import deque

k, l = [int(x) for x in input().split()]
d = {}
for _ in range(k):
    key, value = [x.strip() for x in input().split(':')]
    d[value] = key
s = input().strip()
res = ''
tmp = ''
s = deque(s)
while s:
    tmp += s.popleft()
    if tmp in d.keys():
        res += d[tmp]
        tmp = ''
print(res)
