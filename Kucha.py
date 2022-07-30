class Heap:
    def __init__(self):
        self.arr = []
        self.size = 0

    def shift_up(self, i):
        while i != 0 and self.arr[i] > self.arr[(i-1)//2]:
            self.arr[i], self.arr[(i-1)//2] = self.arr[(i-1)//2], self.arr[i]
            i = (i-1) // 2

    def shift_down(self, i):
        while 2*i+1 < self.size:
            j = i
            if self.arr[2*i+1] > self.arr[i]:
                j = 2 * i + 1

            if 2*i+2 < self.size and self.arr[2*i+2] > self.arr[j]:
                j = 2 * i + 2

            if i == j:
                break
            self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
            i = j

    def insert(self, x):
        self.arr.append(x)
        self.size += 1
        self.shift_up(self.size - 1)

    def extractMax(self):
        if not self.size:
            return None
        tmp = self.arr[0]
        self.arr[0] = self.arr[-1]
        self.arr.pop()
        self.size -= 1
        self.shift_down(0)
        return tmp


n = int(input())
tree = Heap()
for _ in range(n):
    s = input().split()
    if len(s) == 1:
        print(tree.extractMax())
    else:
        num = int(s[1])
        tree.insert(num)