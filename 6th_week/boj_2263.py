import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

in_index = {}
for i, num in enumerate(inorder):
    in_index[num] = i

output = []

def preorder(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return

    root = postorder[post_end]
    output.append(root)

    i = in_index[root]
    left_count = i - in_start

    preorder(in_start, i - 1, post_start, post_start + left_count - 1)
    preorder(i + 1, in_end, post_start + left_count, post_end - 1)

preorder(0, n - 1, 0, n - 1)
sys.stdout.write("\n".join(map(str, output)))
