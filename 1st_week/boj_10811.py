N, M = map(int, input().split())
num_list = [n for n in range(1, N+1)]

for _ in range(M) :
    i, j = map(int, input().split())
    while i <= j :
        num_list[i-1], num_list[j-1] = num_list[j-1], num_list[i-1]
        i+=1
        j-=1

print(*num_list, sep=' ')