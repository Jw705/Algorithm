import sys

input = sys.stdin.readline

n = int(input())

answer = []
t = ""
for _ in range(n - 1):
    t += " "
t += "*"
for _ in range(n - 1):
    t += " "
print(t)
answer.append(t)

for i in range(n - 1):
    recent_layer = answer[-1]
    new_layer = ""

    j = 0
    while j < len(recent_layer):
        if recent_layer[j:j + 3] == "***":
            new_layer = new_layer[:-1] + "*"
            cnt = 0
            while j < len(recent_layer):
                if recent_layer[j] == ' ':
                    if cnt > 0:
                        new_layer = new_layer[:-1]
                        break
                    else:
                        new_layer += ' '
                        cnt = 1
                else:
                    cnt = 0
                    new_layer += ' '
                j += 1
            new_layer += '*'
        elif recent_layer[j:j + 3] == "* *":
            new_layer = new_layer[:-1] + "*****"
            j += 4
        elif recent_layer[j] == "*":
            new_layer = new_layer[:-1] + "* *"
            j += 2
        else:
            new_layer += recent_layer[j]
            j += 1
    print(new_layer)
    answer.append(new_layer)