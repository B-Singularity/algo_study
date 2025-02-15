T = int(input())
for tc in range(1,T+1):
    m,d = map(int,input().split())
    month_lst = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    day = [3,4,5,6,0,1,2]
    index = (sum(month_lst[:m])+d) % 7

    print(f"#{tc} {day[index]}")