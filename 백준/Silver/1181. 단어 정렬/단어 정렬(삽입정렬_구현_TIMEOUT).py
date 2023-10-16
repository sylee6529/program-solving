import sys


# 1 ~ n-1 인덱스 순회하며, i가 가르키는 것보다 짧은 것이 있으면 맞는 위치(j로 위치 탐색)에 삽입
def insertion_sort(s_list):
    s_len = len(s_list)
    for i in range(1, s_len):
        j = i
        tmp = s_list[i]
        while j > 0 and len(s_list[j - 1]) >= len(tmp):  ## 길이가 같은 것도 비교해야 함
            s_list[j] = s_list[j - 1]
            j -= 1
        s_list[j] = tmp
    return s_list


# 길이가 같은 두 문자열의 사전식 순서 판단 (s1 < s2, then True)
def is_lexical_order(s1, s2):
    for i in range(len(s1)):
        if s1[i] > s2[i]:
            return False
    return True


n = int(sys.stdin.readline())
s_list = [sys.stdin.readline().strip() for _ in range(n)]
s_list_dist = list(set(s_list))
result_list = insertion_sort(s_list)


for i in result_list:
    print(i)
