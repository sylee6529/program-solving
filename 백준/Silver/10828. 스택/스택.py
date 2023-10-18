import sys


class Stack:
    def __init__(self, capacity=256):
        self.stk = []

    def push(self, value):
        self.stk.append(value)
        # print(value)

    def pop(self):
        if self.is_empty():
            return -1
        return self.stk.pop()

    def is_empty(self):
        if len(self.stk) == 0:
            return 1
        return 0

    def __len__(self):
        return len(self.stk)

    def peek(self):
        if self.is_empty():
            return -1
        return self.stk[-1]


n = int(sys.stdin.readline())

stack = Stack()
for _ in range(n):
    comm = sys.stdin.readline().split()

    if comm[0] == "push":
        stack.push(comm[1])
    elif comm[0] == "top":
        print(stack.peek())
    elif comm[0] == "pop":
        print(stack.pop())
    elif comm[0] == "size":
        print(len(stack))
    elif comm[0] == "empty":
        print(stack.is_empty())