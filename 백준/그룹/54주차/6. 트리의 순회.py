import sys
sys.setrecursionlimit(10 ** 5)
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))


def preorder(start, end, pstart, pend):
    if start > end:
        return

    print(postorder[pend], end=' ')

    left = inorder.index(postorder[pend]) - start
    right = end - inorder.index(postorder[pend])

    preorder(start, inorder.index(postorder[pend])-1, pstart, pstart+left-1)
    preorder(inorder.index(postorder[pend])+1, end, pend-right, pend-1)


preorder(0, n-1, 0, n-1)