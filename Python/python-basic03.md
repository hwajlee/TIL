# 제어문
1. 조건문
2. 반복문

# 조건문
참/거짓을 판단할 수 있는 조건

## `elif` 복수조건
```python
num = 10
if num > 0:
    print('양수입니다.')
else:
    print('음수입니다.')

num = 20
if num > 5:
    print('num은 5보다 큽니다.')
elif num > 10:
    print('num은 10보다 큽니다.')
elif num > 30:
    print('num은 30보다 큽니다.')


# 미세먼지 확인하기
dust = int(input('미세먼지 농도를 입력하세요 : '))

if dust > 150:
    print('매우 나쁨')
    if dust > 300:
        print('실외 할동을 자제하세요')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
elif dust >= 0:
    print('좋음')
else:
    print('값이 잘못 되었습니다.')
```
# 조건 표현식 (삼항 연산자)

```python
# result 0 보다 큼
num = 10
if num > 0:
    print('0보다 큼')
else:
    print('0보다 크지않음')

# 삼항 연산자 result '양수'
# print('0보다 큼') if num > 0 else print('0보다 작음')
value = ('양수') if num > 0 else ('음수')
print(value)

# 홀짝 표현
num = 2
if num % 2:
    result = '홀수입니다.'
else:
    result = '짝수입니다.'
print(result)

result = '홀수입니다.' if num%2 else '짝수입니다.'
print(result)
```
# fizz buzz 문제
```python
# fizz buzz = 3, 6, 9
# 사용자 입력한 숫자가
# 3의 배수일 경우, fizz 출력
# 5의 배수일 경우, buzz 출력
# 15의 배수일 경우, fizzbuzz 출력
num = int(input())

if num % 15 == 0:
    print('fizzbuzz')
elif num % 5 ==0:
    print('buzz')
elif num % 3 == 0:
    print('fizz')
else:
    print(num)
```

# `join()`
list에 있는 문자열을 다 합친다.
```python
datas = ['Life', 'is', 'too', 'short']
result = _.join(datas)
print(result)
```

# `sort()`

```python
# 오름차순
datas = [1, 3, 5, 4, 2]
datas.sort()
print(datas)
# 역순
datas.reverse()
print(datas)

# 256까지는 같은 주소값을 갖기 때문에 [1, 4, 3]
datas1 = datas2 = [1, 2, 3]
datas1[1] = 4
print(datas1, datas2)
```
# 반복문
- while
- for
```python
num = 0
while a < 5:
    print(num)
    # num = num + 1
    # result 0, 1, 2, 3, 4
    num += 1
print('끝')


menus = ['짜장면', '떡볶이', '닭칼국수', '햄버거', '탕수육']
idx = 0
while idx < len(menus):
    print(menus[idx], end=' ')
    idx += 1
print('순서대로')

idx = len(menus) -1
while idx >= 0:
    print(menus[idx], end=' ')
    idx -= 1
print('역순')

idx = 0
while idx < len(menus):
    print(menus[idx], end=' ')
    idx += 2
print('2의 배수 많큼 순서대로 출력')

while user_input != '안녕':
    print('안녕??')
    user_input = str(input('안녕이라고 말해주세요 : '))

# 1부터 사용자가 입력한 숫자까지 더하기
num = int(input())
sum(range(1,num+1))


# result ex) input 185 => 5 8 1
num = input()
idx = len(num) - 1 

while idx >= 0:
    print(num[idx])
    int(num[idx])  # 문자열 숫자로 활용하기
    idx -= 1

# result 4 3 2 1
num = 1234
while num > 0:
    print(num % 10)
    num = num // 10
```
# for문을 이용한 List 접근법
```python

# result apple, mango, banana
for fruit in ['apple', 'mango', 'banana']:
    print(fruit)
```

# for문을 이용한 Dictionary 접근법

```python

grades = {'john':  80, 'eric': 90}
for student in grades:
    print(student)

# result john 80 \n eric 90
for key, value in grades.items():
    print(key, value)
```

# `enumerate()`

```python
members = ['민수', '영희', '철수']
# result 0 민수, 1 영희, 2 철수
for idx, member in enumerate(members):
    print(idx, member)

# 숫자를 1부터 카운트 하기
for idx, member in enumerate(members, start=1):
    print(idx, member)
```

# List Comprehension(리스트 컴프리핸션)

```python
# 1~3의 세제곱 리스트 만들기
numbers = [1, 2, 3]
cubic_numbers = []
# [1, 8, 27]
for num in range(1, 4):
    cubic_numbers.append(num ** 3)
print(cubic_numbers)


# 리스트 컴프리헨션
cubic_list = [num ** 3 for num in range(1, 4)]
print(cubic_list)


# 10 * 10 체스판
# chess_board = [[0 for _ in range(5)] for _ in range(5)]
# chess_board
pan = [[0 for _ in range(10)] for _ in range(10)]
pan = [[0] * 10 for _ in range(10)]
```

# Dictionary comprehension(딕셔너리 컴프리헨션)
```python

# 1~3의 세제곱 딕셔너리 만들기
cubic = {}

for number in range(1, 4):
    cubic[number] = number**3
print(cubic)

cubic = { n: n**3 for n in range(1, 4)}
print(cubic)
```

# 반복제어 (`break`, `continue`, `for-else`)
```python
n = 0
while True:
    if n == 3:
        break
    print(n)
    n += 1

# 0부터 9까지 순회하는 for 반복문 안에서 
# 1을 초과하는 경우 '0과 1만 필요해!' 를 출력하며 종료하는 코드를 작성해봅시다.
for idx in range(10):
    if idx > 0:
        break
    print('0과 1만 필요해')
    print(idx)
    
for num in range(10):
    if num > 1:
        print('0, 1 끝')
        break
    print(num)



```

## `countinue`

```python
for i in range(6):
    if i % 2 == 0:
        continue
        # continue 이후의 코드는 실행되지 않습니다.
    print(f'{i}는 홀수다.')
```

## `pass`
아무 것도 하지 않음
```python
num = 10
if num > 0:
    pass
else:
    print('음수')
```

## `for-else`
`for-else` `for`문에 `break`가 있을 경우에만 의미가 있음

```python
for char in 'apple':
    if char == 'b':
        print('b!')
        break
else:
    print('b가 없습니다.')

for char in 'banana':
    if char == 'b':
        print('b!')
        break
else:
    print('b가 없습니다.')

numbers = [1, 3, 7, 9]
for number in numbers:
    if number == 4:
        print(True)
        break
else:
    print(False)

for number in numbers:
    if number in {4}:
        print(number in {4})
        break
else:
    print(number in {4})

```