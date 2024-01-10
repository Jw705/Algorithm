import sys
n = int(sys.stdin.readline())

stack = []

for _ in range(n):
    data = list(map(int, sys.stdin.readline().split()))

    if data[0] == 1:
        stack.append(data[1])
    elif data[0] == 2:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif data[0] == 3:
        print(len(stack))
    elif data[0] == 4:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif data[0] == 5:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack) - 1])
