import sys

input = sys.stdin.readline

n = int(input())

t = [" "] * (n - 1) + ["*"] + [" "] * (n - 1)
print("".join(t))
recent_layer = t

for i in range(n - 1):
    new_layer = []

    j = 0
    while j < len(recent_layer):
        if recent_layer[j:j + 3] == ["*", "*", "*"]:
            new_layer[-1] = "*"
            cnt = 0
            while j < len(recent_layer):
                if recent_layer[j] == ' ':
                    if cnt > 0:
                        new_layer.pop()
                        break
                    else:
                        new_layer.append(' ')
                        cnt = 1
                else:
                    cnt = 0
                    new_layer.append(' ')
                j += 1
            new_layer.append('*')
        elif recent_layer[j:j + 3] == ["*", " ", "*"]:
            new_layer[-1] = "*"
            new_layer.extend(["*", "*", "*", "*"])
            j += 4
        elif recent_layer[j] == "*":
            new_layer[-1] = "*"
            new_layer.extend([" ", "*"])
            j += 2
        else:
            new_layer.append(recent_layer[j])
            j += 1
    print("".join(new_layer))
    recent_layer = new_layer