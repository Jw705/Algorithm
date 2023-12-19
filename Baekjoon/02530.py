A,B,C = map(int, input().split(' '))
D = int(input())

A= int(A+D//3600)
B= int(B+D%3600//60)
C= int(C+D%60)

if C>=60:
    C=C%60
    B+=1
if B>=60:
    B=B%60
    A+=1
if A>=24:
    A=A%24
 
print(A,B,C)