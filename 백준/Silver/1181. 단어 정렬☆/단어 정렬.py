import sys

N = int(sys.stdin.readline())
arr = []


for i in range(N):
    arr.append(sys.stdin.readline().strip())

# 중복제거, 알파벳순 정렬
arr = list(set(arr))
arr.sort()


arr_seq = []  # [길이, arr_idx]를 요소로 가짐
for i in range(len(arr)):
    arr_seq.append([len(arr[i]), i])

# 길이 정렬
arr_seq.sort()

for i in range(len(arr_seq)):
    str_index = arr_seq[i][1]
    print(arr[str_index])
