class Heap:
    def __init__(self, arr: list) -> None:
        self.arr = arr      
        
    def shift_up(self, i):
        while i != 0 and self.arr[i] < self.arr[(i-1) // 2]:
            self.arr[i], self.arr[(i-1) // 2] = self.arr[(i-1) // 2], self.arr[i]
            i = (i-1) // 2
                
    def shift_down(self, i):
        while 2*i+1 < len(self.arr):
            j = i
            if self.arr[i*2+1] < self.arr[i]:
                j = i * 2 + 1
            if 2*i+2 < len(self.arr) and self.arr[i*2+2] < self.arr[j]:
                j = i * 2 + 2
            if i == j:
                break            
            self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
            i = j

    def print_curr(self, elem):
        print(*reversed(self.arr[0]))
        self.arr[0][0] += elem
        self.shift_down(0)

num, tasks = map(int, input().split())
lst = [int(x) for x in input().split()]
heap = Heap([[0, int(x)] for x in range(num)])
for i in lst:
    heap.print_curr(i)