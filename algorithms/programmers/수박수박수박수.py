def solution(n):
    answer = '수박'
    
    if n%2==1:
        return answer*(n//2) + answer[:1]
    else:
        return answer*(n//2)