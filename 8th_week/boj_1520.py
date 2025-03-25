import sys

sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 증가
input = sys.stdin.read
data = input().split("\n")

M, N = map(int, data[0].split())  # 세로(M) x 가로(N)
matrix = [list(map(int, data[i + 1].split())) for i in range(M)]
dp = [[-1] * N for _ in range(M)]  # -1이면 아직 방문하지 않은 지점

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(y, x):
    if y == M - 1 and x == N - 1:  # 도착 지점
        return 1
    if dp[y][x] != -1:  # 이미 방문한 곳이면 메모이제이션 값 반환
        return dp[y][x]

    dp[y][x] = 0  # 초기화
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0 <= ny < M and 0 <= nx < N and matrix[ny][nx] < matrix[y][x]:  # 내리막길만 이동 가능
            dp[y][x] += dfs(ny, nx)

    return dp[y][x]

print(dfs(0, 0))  # 출발점에서 도착점까지 가는 경로의 수
