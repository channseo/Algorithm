def solution(s):
    answer = 0
    if len(s) % 2 == 0:
        i = (len(s) // 2)
        answer = s[i-1] + s[i]
        
    elif len(s) % 2 != 0:
        i = (len(s) + 1) // 2
        answer = s[i-1]
    return answer