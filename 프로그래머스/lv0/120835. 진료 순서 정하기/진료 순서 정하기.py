def solution(emergency):
    answer = sorted(emergency, reverse=True)
    
    return [answer.index(em) + 1 for em in emergency]
