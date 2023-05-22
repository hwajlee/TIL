import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    sticks = input()
    sticks = sticks.replace('()', '*')

    total = bar = 0

    for char in sticks:
        if char == '(':
            bar += 1
        elif char == ')':
            bar -= 1
            total += 1
        else:
            total += bar

    print(f'#{tc} {total}')