import sys
sys.stdin = open('input.txt')

T = int(input())

# 집합 A
A = [_ for _ in range(1, 13)]
# 집합 A의 부분집합을 저정한 2차원 리스트
# 참고) 원소 개수가 n인 집합 s의 전체 부분집합의 개수는 2**n
subsetA = [[] for _ in range(2**12)]
print(2<<3)
# 집합A의 부분집합
for i in range(2<<3):
    print(i)