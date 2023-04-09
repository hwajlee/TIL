# `map`(function, iterable)



```python
s = '3 3 4 5 8'
# map(모두 할 일/함수, 자료)
# map(int(), s.split()) => 0
list(map(int, s.split()))

s = '3 3 4 5 8'
new_list = []

for char in s.split():
    new_list.append(int(char))

print(new_list)
x, y = new_list
# x = 3, y = 3

# 리스트 컴프리핸션
[n+1 for n in range(10)]
```

# `filter`(function, iterable)

```python
members = [
    {'name':'aaaa', 'age':20, 'gender':'F'},
    {'name':'aaaa', 'age':15, 'gender':'F'},
    {'name':'aaaa', 'age':24, 'gender':'M'},
    {'name':'aaaa', 'age':11, 'gender':'F'},
    {'name':'aaaa', 'age':65, 'gender':'M'},
    {'name':'aaaa', 'age':34, 'gender':'F'},
    {'name':'aaaa', 'age':8, 'gender':'M'},
    {'name':'aaaa', 'age':28, 'gender':'M'},
    {'name':'aaaa', 'age':31, 'gender':'F'},
]

target_members = []
# age에서 20보다 높고, gender에서 M인 놈만 뽑겠다
for member in members:
    if member['age'] >= 20 and member['gender'] == 'M':
        target_members.append(member)
        
print(target_members)


# 함수명이 is로 시작하면, return이 T/F
def is_adult_and_male(member):
    if member['age'] >= 20 and member['gender'] == 'M':
        return True
    return False

for member in members:
    print(is_adult_and_male(member))

# 함수 인자가 1개여야 한다.
# filter는 True인 애들만 뽑아낸다
list(filter(is_adult_and_male, members))

# 람다식
list(filter(lambda m : m['age'] >= 20 and m['gender']=='M', members))
```

# lambda
- 익명함수
```python
def f1(x, y):
    return x + y

print(f1(1, 2))

print((lambda x, y: x + y)(1, 2))
```

# 자료구조

- 순서가 있음
  - 문자열 (불변)
  - 리스트 (가변)
  - 튜플 (불변)
- 순서가 없음
  - 셋 (가변)
  - 딕셔너리 (가변)

# 문자열
>**변경불가** 항상 return 값이 나옴

## 조회 탐색
1. `.find(x)`

    없으면, -1 반환
   
    x의 첫번째 위치 반환
```python
a = 'apple'
# result 1
a.find('ppl')
# 오류
a.find('z')
```

2. `.index(x)`

    없으면 오류
```python
a = 'apple'
a.index('p')
# 오류
a.index('z')
```

3. `.replace(old, new, [count])`
```python
a = 'yaya!'
b = 'wooooowoo'

new_a = a.replace('y', 'h')

print(a)
print(new_a)
```
4. `.strip([chars])`

```python
a = '   hello!  \n'
b = 'hihihihahahahihi'
c = 'monty python'
# result 'hello'
a.strip()

# result 'hello!  \n'
a.lstrip()

# 오른쪽에서 hi 모두 제거 result 'hihihihahaha'
b.rstrip('hi')
```

5. `.split([chars])`

    잘라서 리스트 형태로 반환한다.
```python
a = 'a_b_c'
lists = a.split('_')
print(lists)
```

6. `.join()`

```python
word = '배고파'
words = ['안녕', 'hello']

# result '배!고!파'
'!'.join(word)

# result '안녕 hello'
' '.join(words)

s = '123456789'
# 다 붙어있는 문자열을 리스트로 바꾸려면 list()
list(map(int, s))
```

# 리스트(List)

1. `.append(x)`

    데이터 추가 => 마지막 위치에 추가


```python
cafe = ['starbucks', 'tomntoms', 'hollys']
cafe.append('banapresso')
```

2. `.index(x)`

    해당 리스트의 인덱스 값을 리턴
```python
a = [1, 2, 3, 4, 5]
a.index(3)

```
3. `sort()`

    순서대로 만든다

    reverse=True : 역순

```python
import random

lucky = random.sample(range(1, 46), 6)
lucky.sort()

lucky.sort(reverse=True)
```