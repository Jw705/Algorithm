N = int(input())

sum=0
cnt=0
for i in range(1, N):
    sum+=i
    cnt+=1
    if sum>N:
        cnt-=1
        break

if cnt==0:
    cnt=1
    
print(cnt)