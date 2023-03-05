def solution(n):
    li = []
    b = 1
    
    while b < n + 1:
        if n % b == 0:
            li.append(b)
        b += 1
    
    answer = 0
    for a in li:
        answer = answer + a
    

    return answer