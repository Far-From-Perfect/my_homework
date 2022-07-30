class Node:
    def __init__(self, name, left = -1, right = -1) -> None:
        self.name = name
        self.left = left
        self.right = right
        # self.parent = parent

class Tree:
    def __init__(self, data) -> None:
        self.data = data
        self.root = Node(data[0][0], self.insert(data[0][1]), self.insert(data[0][2]))

    def insert(self, idx):
        if idx == -1:
            return -1
        return Node(self.data[idx][0], self.insert(self.data[idx][1]), self.insert(self.data[idx][2]))

    def result(self):
        self.in_order_lst = []
        # self.pre_order_lst = []
        # self.post_order_lst = []

        self.flag = True
        node = self.root
        while node.left != -1:
            node = node.left
        self.num = node.name
        self.in_order(self.root)
        # self.pre_order(self.root)
        # self.post_order(self.root)

        # return (self.in_order_lst, self.pre_order_lst, self.post_order_lst)
        return 'CORRECT' if self.flag else 'INCORRECT'

    def in_order(self, root):
        # Решение с флагами на проверку свойства дерева поиска
        if root.left != -1:
            self.in_order(root.left)
            if self.num < root.name:
                self.num = root.name
            else:
                self.flag = False
        else:
            if self.num <= root.name:
                self.num = root.name
            else:
                self.flag = False
            # self.in_order_lst.append(root.name)
        # else:
            # self.in_order_lst.append(root.name)
        if root.right != -1:
            self.in_order(root.right)

        # if root.left == -1 and root.right == -1:
        #     self.in_order_lst.append(root.name)

    def pre_order(self, root):
        self.pre_order_lst.append(root.name)
        if root.left != -1:
            self.pre_order(root.left)
        if root.right != -1:
            self.pre_order(root.right)

    def post_order(self, root):
        if root.left != -1:
            self.post_order(root.left)
        if root.right != -1:
            self.post_order(root.right)
        return self.post_order_lst.append(root.name)


n = int(input())
# для прохождения тестов с большой глубиной рекурсии
import sys
sys.setrecursionlimit(50000)
data = []
for i in range(n):
    name, left, right = map(int, input().split())
    data.append([name, left, right])
if n == 0:
    print('CORRECT')
else:
    tree = Tree(data)
    res = tree.result()
    print(res)
