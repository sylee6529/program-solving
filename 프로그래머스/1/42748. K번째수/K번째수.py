def solution(array, commands):
    answer = []
    
    for c in commands:
        li = []
        li = array[c[0]-1:c[1]]
        li.sort()
        answer.append(li[c[2]-1])
        
    return answer