N, M = map(int, input().split())
A = list(map(int, input().split()))

total = 0
mod_count = [0] * M
mod_count[0] = 1

result = 0
for num in A:
    total += num
    remain = total % M
    if remain < 0:
        remain += M

    result += mod_count[remain]
    mod_count[remain] += 1

print(result)
