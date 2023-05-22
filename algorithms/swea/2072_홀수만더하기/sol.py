import sys
import os
filename = os.path.join(os.path.dirname(__file__), 'input.txt')
sys.stdin = open(filename)


T = int(input())


def solve(numbers):
    total = 0
    for num in numbers:
        if num % 2:
            total += num
    
    return total


for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    answer = solve(numbers)
    print(f'#{tc} {answer}')