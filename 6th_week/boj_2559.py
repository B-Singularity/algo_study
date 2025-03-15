import sys
sys.setrecursionlimit(10**6)


def recur(arr, start, end, total, N, K):
    if start == N - K:  # 마지막 가능한 구간까지 탐색
        return total

    # 현재 구간의 합을 구하고, 다음 구간으로 이동
    new_total = total - arr[start] + arr[end]
    return max(total, recur(arr, start + 1, end + 1, new_total, N, K))  # 최댓값 비교

N, K = map(int, input().split())
temperatures = list(map(int, input().split()))

# 첫 번째 구간 합 초기화
init_total = sum(temperatures[:K])

# 재귀 호출
result = recur(temperatures, 0, K, init_total, N, K)
print(result)
