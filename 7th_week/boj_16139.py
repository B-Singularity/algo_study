import sys
input = sys.stdin.readline

S = input().strip()
n = len(S)
q = int(input().strip())

cum = [[0] * 26 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(26):
        cum[i][j] = cum[i-1][j]
    cum[i][ord(S[i-1]) - ord('a')] += 1

output = []
for _ in range(q):
    ch, l, r = input().split()
    l, r = int(l), int(r)
    idx = ord(ch) - ord('a')
    result = cum[r+1][idx] - cum[l][idx]
    output.append(str(result))

sys.stdout.write("\n".join(output))
