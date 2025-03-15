import sys
sys.setrecursionlimit(10**6)

def post_order(start, end):
    if start >= end:
        return []
    root = preorder[start]
    partition = start + 1
    while partition < end and preorder[partition] < root:
        partition += 1
    return post_order(start + 1, partition) + post_order(partition, end) + [root]

preorder = []
while True:
    line = sys.stdin.readline().strip()
    if not line:
        break
    # 숫자로 변환
    preorder.append(int(line))

result = post_order(0, len(preorder))
for num in result:
    sys.stdout.write(str(num) + "\n")
