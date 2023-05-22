import sys
sys.stdin = open('input.txt')

# 테스트 케이스 수
T = int(input())

# T만큼 테스트 케이스 반복
for TC in range(1, T+1):
    # 카드 장수 N
    N = int(input())
    # 받아올 카드
    numbers = list(map(int, input()))

    # 0~9까지 담을 리스트
    card = [0] * 10
    # 카운팅
    for i in numbers:
        card[i] += 1

    # 개수가 가장 큰 값 찾기
    max_num = 0
    card_num = 0
    # j = 0~9
    for j in range(len(card)):
        if max_num <= card[j]:
            max_num = card[j]
            card_num = j

    print(f'#{TC} {card_num} {max_num}')