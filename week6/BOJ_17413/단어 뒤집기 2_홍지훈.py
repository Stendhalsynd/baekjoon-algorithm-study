import sys
input = sys.stdin.readline().rstrip

S = input()
stack = []

def print_reverse_stack_with_empty_string(stack):
    while stack:
      print(stack.pop(), end='')
    print(' ', end='')

def print_reverse_stack(stack):
    while stack:
      print(stack.pop(), end='')

def print_stack(stack):
    print(''.join(stack),end='')
    stack.clear()

if S.count('>') == 0:
  for i in range(len(S)):
    if S[i] != ' ':
      stack.append(S[i])
    else:
      print_reverse_stack_with_empty_string(stack)
  print_reverse_stack_with_empty_string(stack)
  print()
else:
  tag = False
  for i in range(len(S)):
    if S[i] == '<':
      tag = True
      if stack:
        print_reverse_stack(stack)
    if tag:
      stack.append(S[i])
      if S[i] == '>':
        tag = False
        print_stack(stack)
    elif not tag:
      if S[i] != ' ':
        stack.append(S[i])
      else:
        print_reverse_stack_with_empty_string(stack)
  print_reverse_stack_with_empty_string(stack)
  print()