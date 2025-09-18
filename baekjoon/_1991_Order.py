import sys
input = sys.stdin.readline

# 내가 짠 초창기 코드
# n = int(input())
# alpabetToInt = {chr(65+i): i+1 for i in range(n)}
# intToAlpabet = {i+1: chr(65+i) for i in range(n)}
# tree = [[] for _ in range(n+1)]


# def preOrder(start):
#     print(intToAlpabet[start], end='')
#     preOrderLeft(start)
#     preOrderRight(start)


# def preOrderLeft(left):
#     for lc, rc in tree[left]:
#         if (lc != 0):
#             preOrder(lc)


# def preOrderRight(right):
#     for lc, rc in tree[right]:
#         if (rc != 0):
#             preOrder(rc)


# def inOrder(start):
#     inOrderLeft(start)
#     print(intToAlpabet[start], end='')
#     inOrderRight(start)


# def inOrderLeft(left):
#     for lc, rc in tree[left]:
#         if (lc != 0):
#             inOrder(lc)


# def inOrderRight(right):
#     for lc, rc in tree[right]:
#         if (rc != 0):
#             inOrder(rc)


# def postOrder(start):
#     postOrderLeft(start)
#     postOrderRight(start)
#     print(intToAlpabet[start], end='')


# def postOrderLeft(left):
#     for lc, rc in tree[left]:
#         if (lc != 0):
#             postOrder(lc)


# def postOrderRight(right):
#     for lc, rc in tree[right]:
#         if (rc != 0):
#             postOrder(rc)


# for i in range(n):
#     parent, leftChild, rightChild = input().strip().split()
#     if (leftChild == '.' and rightChild == '.'):
#         continue
#     elif (leftChild == '.'):
#         tree[alpabetToInt[parent]].append((0, alpabetToInt[rightChild]))

#     elif (rightChild == '.'):
#         tree[alpabetToInt[parent]].append((alpabetToInt[leftChild], 0))
#     else:
#         tree[alpabetToInt[parent]].append(
#             (alpabetToInt[leftChild], alpabetToInt[rightChild]))


# preOrder(alpabetToInt['A'])
# print()
# inOrder(alpabetToInt['A'])
# print()
# postOrder(alpabetToInt['A'])

n = int(input())
tree = {}

for _ in range(n):
    parent, leftChild, rightChild = input().strip().split()
    tree[parent] = (leftChild, rightChild)


def preOrder(node):
    if (node == '.'):
        return

    print(node, end='')
    preOrder(tree[node][0])
    preOrder(tree[node][1])


def inOrder(node):
    if (node == '.'):
        return

    inOrder(tree[node][0])
    print(node, end='')
    inOrder(tree[node][1])


def postOrder(node):
    if (node == '.'):
        return

    postOrder(tree[node][0])
    postOrder(tree[node][1])
    print(node, end='')


preOrder('A')
print()
inOrder('A')
print()
postOrder('A')
