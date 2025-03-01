T = int(input())

for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())
    x5, y5, x6, y6 = map(int, input().split())

    white_area = (x2 - x1) * (y2 - y1)


    def intersect_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        lx = max(ax1, bx1)
        rx = min(ax2, bx2)
        ly = max(ay1, by1)
        ry = min(ay2, by2)
        return max(0, rx - lx) * max(0, ry - ly)

    area1 = intersect_area(x1, y1, x2, y2, x3, y3, x4, y4)
    area2 = intersect_area(x1, y1, x2, y2, x5, y5, x6, y6)

    L = max(x1, x3, x5)
    R = min(x2, x4, x6)
    B = max(y1, y3, y5)
    Tt = min(y2, y4, y6)
    area12 = max(0, R - L) * max(0, Tt - B)

    covered = area1 + area2 - area12

    if white_area - covered > 0:
        print("YES")
    else:
        print("NO")