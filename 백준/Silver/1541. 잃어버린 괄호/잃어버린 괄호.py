import sys


n = sys.stdin.readline().strip()
m = n.split('-')

answer = 0

# 첫번째 수가 음수(-)면 따로 처리
x = sum(map(int, (m[0].split('+'))))
if n[0] == '-':
    answer -= x
else:
    answer += x

# -를 기준으로 나눈 배열을 기준으로 합한다
for x in m[1:]:     # 인덱스 1부터 시작, +로 이루어진 식을 합하고, 이를 뺀다
    x = sum(map(int, (x.split('+'))))
    answer -= x
print(answer)