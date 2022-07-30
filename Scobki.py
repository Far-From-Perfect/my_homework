class Stack(list):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.idx = []

    def upd(self, x):
        self.idx.append(x)

    def rem(self):
        return self.idx.pop()


def check_brackets(sym, i):
    if sym in {'[', '(', '{'}:
        stack.stack.append(sym)
        stack.upd(i)
    else:
        if len(stack.stack) == 0:
            return False
        top = stack.stack.pop()
        _ = stack.rem()
        if (top == '[' and sym != ']') or (top == '(' and sym != ')') or (top == '{' and sym != '}'):
            return False
    return True


s = input().strip()
check = ['[', ']', '(', ')', '{', '}']
stack = Stack()
idx = -1
for i, char in enumerate(s):
    if char in check:
        flag = check_brackets(char, i)
        if not flag:
            idx = i
            break
if idx != -1:
    print(idx+1)
elif len(stack.stack) > 0:
    print(stack.idx[0]+1)
else:
    print('Success')