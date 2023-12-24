A, I = map(int, input().split(' '))

for i in range(int(A*I*0.9),A*I+1):
    if i/A>I-1:
        print(i)
        break;
