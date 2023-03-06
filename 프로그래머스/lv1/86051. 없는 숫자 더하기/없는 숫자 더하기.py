def solution(numbers):
    li = []
    answer=0
    
    for i in range(0, 10):
        if i not in numbers:
            li.append(i)
    
    for a in li:
        answer += a
        
    return answer