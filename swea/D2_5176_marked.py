T = int(input())


def inorder(i):
    global num
    if (i <= n):
        inorder(i*2)
        tree[i] = num
        num += 1
        inorder(i*2+1)


for tc in range(1, T+1):
    n = int(input())
    num = 1
    tree = [0 for _ in range(n+1)]
    inorder(1)
    print(f"#{tc} {tree[1]} {tree[n//2]}")
