import sys
sys.setrecursionlimit(10**8)


def safe_area(r, c, visited, no_water_area, h):
    global cnt

    if 0 <= r < n and 0 <= c < n and visited[r][c] == 0 and no_water_area[r][c] == False:
        visited[r][c] = 1
        safe_area(r - 1, c, visited, no_water_area, h)
        safe_area(r, c - 1, visited, no_water_area, h)
        safe_area(r, c + 1, visited, no_water_area, h)
        safe_area(r + 1, c, visited, no_water_area, h)
        

cnt = 0
global n
n = int(sys.stdin.readline())

height_list = []
for _ in range(n):
    height_list.append(list(map(int, sys.stdin.readline().split())))

visited = [[0] * n for _ in range(n)]

max_area_cnt = 0
cnt = 0
no_water_area = [[False]*n for _ in range(n)]
for i in range(max(map(max, height_list))):
    cnt = 0

    # 잠긴 영역 리스트를 만든다
    is_all_safe = True
    for j in range(n):
        for k in range(n):
            if no_water_area[j][k] == False and height_list[j][k] <= i:
                is_all_safe = False
                no_water_area[j][k] = True

    visited = [[0] * n for _ in range(n)]
    for j in range(n):
        if is_all_safe == True and max_area_cnt == 0:
            max_area_cnt = 1
            break
        for k in range(n):
            if no_water_area[j][k] == False and visited[j][k] == 0:
                safe_area(j, k, visited, no_water_area, i)
                cnt += 1
        if cnt > max_area_cnt:
            max_area_cnt = cnt


print(max_area_cnt)
