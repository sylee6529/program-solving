import sys
from collections import deque


class Queue:
    def __init__(self):
        self.q = deque()

    def push(self, value):
        self.q.append(value)

    def pop(self):
        if len(self.q) == 0:
            return -1
        return self.q.popleft()

    def __len__(self):
        return len(self.q)

    def is_empty(self):
        if len(self.q) == 0:
            return 1
        else:
            return 0

    def get_front(self):
        if self.is_empty():
            return -1
        return self.q[0]

    def get_back(self):
        if self.is_empty():
            return -1
        return self.q[-1]


n = int(sys.stdin.readline())

queue = Queue()
for _ in range(n):
    comm = sys.stdin.readline().split()
    if comm[0] == "push":
        queue.push(comm[1])
    elif comm[0] == "pop":
        print(queue.pop())
    elif comm[0] == "size":
        print(len(queue))
    elif comm[0] == "empty":
        print(queue.is_empty())
    elif comm[0] == "front":
        print(queue.get_front())
    elif comm[0] == "back":
        print(queue.get_back())