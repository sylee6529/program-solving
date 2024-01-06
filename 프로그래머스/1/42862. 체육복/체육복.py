def solution(n, lost, reserve):
    answer = 0
    
    li = [1 for i in range(n)]
    
    # reserve 에 해당하는 index ++1
    for r in reserve:
        li[r - 1] += 1
    
    # lost에 해당하는 애들 --1
    for ll in lost:
        li[ll - 1] -= 1
    
    lost.sort()

    # lost에 있는 인덱스, -1이 2이상이면 그거 가져오고 break, 아니면 뒤의 것 보고 가져오기, 없으면 그대로
    for l in lost:
        idx = l-1
        if li[idx] != 0:
            continue
        
        if (idx-1) >= 0 and li[idx-1] >= 2:
            li[idx-1] -= 1
            li[idx] += 1
        elif (idx + 1) < n and li[idx+1] >= 2:
            li[idx+1] -= 1
            li[idx] += 1
    
    # li에서 값이 2이상인 애들 세기
    for i in li:
        if i >= 1:
            answer += 1
    
    return answer