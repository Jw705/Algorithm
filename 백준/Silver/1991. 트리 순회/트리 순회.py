import sys
input = sys.stdin.readline

n = int(input())
graph = {}
for i in range(n):
    node, left, right = input().split()
    graph[node] = (left, right)


# 전위 순회 : (루트) -> (왼쪽 자식) -> (오른쪽 자식)
def preorder(node):
    print(node, end='')
    left, right = graph[node]
    if left != '.':
        preorder(left)
    if right != '.':
        preorder(right)


# 중위 순회 : (왼쪽 자식) -> (루트) -> (오른쪽 자식)
def inorder(node):
    left, right = graph[node]
    if left != '.':
        inorder(left)
    print(node, end='')
    if right != '.':
        inorder(right)


# 후위 순회 : (왼쪽 자식) -> (오른쪽 자식) -> (루트)
def postorder(node):
    left, right = graph[node]
    if left != '.':
        postorder(left)
    if right != '.':
        postorder(right)
    print(node, end='')


preorder('A')
print()
inorder('A')
print()
postorder('A')