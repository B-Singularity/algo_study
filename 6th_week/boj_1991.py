def pre_order(tree, now, visited):
    result = [now]
    if now == '.' or visited[ord(now) - 65]:
        return []
    visited[ord(now) - 65] = True
    result.extend(pre_order(tree, tree[ord(now) - 65][0], visited))
    result.extend(pre_order(tree, tree[ord(now) - 65][1], visited))
    return result

def in_order(tree, now, visited):
    result = []
    if now == '.' or visited[ord(now) - 65]:
        return []

    result.extend(in_order(tree, tree[ord(now) - 65][0], visited))
    visited[ord(now) - 65] = True
    result.append(now)
    result.extend(in_order(tree, tree[ord(now) - 65][1], visited))
    return result

def post_order(tree, now, visited):
    result = []
    if now == '.' or visited[ord(now) - 65]:
        return []
    result.extend(post_order(tree, tree[ord(now) - 65][0], visited))
    result.extend(post_order(tree, tree[ord(now) - 65][1], visited))
    visited[ord(now) - 65] = True
    result.append(now)

    return result

N = int(input())
tree = [["", ""] for _ in range(26)]
for _ in range(N):
    parent, left, right = input().split()
    idx = ord(parent) - 65  # A를 0으로 변환
    tree[idx][0] = left
    tree[idx][1] = right

visited_pre = [False] * 26
visited_in = [False] * 26
visited_post = [False] * 26

result_pre_order = pre_order(tree, "A", visited_pre)
result_in_order = in_order(tree, "A", visited_in)
result_post_order = post_order(tree, "A", visited_post)


print(''.join(result_pre_order))
print(''.join(result_in_order))
print(''.join(result_post_order))

