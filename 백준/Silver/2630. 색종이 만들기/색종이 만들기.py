import sys


white_cnt = 0
blue_cnt = 0
n = int(sys.stdin.readline())
paper_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def crop_paper(x, y, N):
    global white_cnt
    global blue_cnt

    base_color = paper_list[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if base_color != paper_list[i][j]:
                crop_paper(x, y, N // 2)
                crop_paper(x + N // 2, y, N // 2)
                crop_paper(x, y + N // 2, N // 2)
                crop_paper(x + N // 2, y + N // 2, N // 2)
                return
    if base_color == 0:
        white_cnt += 1
    else:
        blue_cnt += 1


crop_paper(0, 0, n)
print(white_cnt, blue_cnt)