def solution(a, b):
    answer = 0
    for i in a:
        answer += 1
    answer_1 = 0
    for x in range (0, answer):
        answer_1 += a[x]*b[x]
    
    return answer_1