def solution(price, money, count):
    li = []
    for i in range(1, count + 1):
        li.append(price * i)
    
    answer = 0
    for a in li:
        answer += a
    
    if answer > money:
        return answer - money
    else:
        return 0