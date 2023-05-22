import sys
sys.stdin = open('input.txt')

T = int(input())


def solve(numbers):
    pass


for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    ans = solve(numbers)
    print(f'#{tc} {ans}')