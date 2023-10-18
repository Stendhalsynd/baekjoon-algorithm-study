import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

class MyStack:
  def __init__(self, deque):
    self.deque = deque()

  def show(self):
    print('deque : ', self.deque)

  def push(self, X):
    self.deque.append(X)

  def pop(self):
    deq = self.deque
    if len(deq) == 0:
      print(-1)
    else:
      print(self.deque.pop())

  def size(self):
    print(len(self.deque))

  def empty(self):
    if len(self.deque) == 0:
      print(1)
    else:
      print(0)

  def top(self):
    if len(self.deque) == 0:
      print(-1)
    else:
      print(self.deque[-1])

def switch(a, option):
  if option == 'pop':
    a.pop()
  if option == 'size':
    a.size()
  if option == 'empty':
    a.empty()
  if option == 'top':
    a.top()

a = MyStack(deque)
inputs = []

for num in range(N):
  input = sys.stdin.readline().rstrip().split()
  inputs.append(input)

for input in inputs:
  if len(input) == 2: # push
    _, value = input
    a.push(int(value))
  else: # 다른 명령어
    command = input[0]
    switch(a, command)