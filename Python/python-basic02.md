# 시퀀스(sequence) 자료형
데이터가 순서에 맞게 나열된 형식
1. 리스트(list) : mutable (변경가능)
2. 튜플(tuple) : immutable (불변)
3. 레인지(range) : immutable (불변)
4. 문자열(string) : immutable (불변)

# 리스트 (List)
대괄호 [], `list()` 사용
```python
# result [], []
empty_List = []
create_List = list()
print(empty_List, create_List)

# result ['강남', '서초', '송파', '광진', '마포']
locations = ['강남', '서초', '송파', '광진', '마포']
# locations = ['강남' '서초', '송파', '광진', '마포'] : 실행됨, 주의! 
numbers = [
    1,
    2,
    3,
    4
    5,
    6,
    7, # trailing comma
]
print(locations)
```

## 추가 (`append()`)
```python
# result ['강남', '서초', '송파', '광진', '마포', '부산']
locations = ['강남', '서초', '송파', '광진', '마포']
locations.apped('부산')
print(locations)

# result ['value', 'value', 'value', [10], [2]]
test_list = ['value', 'value', 'value', [], [1]]
test_list[3].append(10)
test_list[4][0].append(2)
print(test_list)
```

# 튜플 (Tuple)
() 표현, (불변, immutable)

파이썬 내부에서 사용중
```python
# result (1, 2, 3)
tuple_data = (1, 2, 3)
print(tuple_data)

# result (1, 2, 3)
tuple_data = 1, 2, 3
print(tuple_date)

# result [1, 100, 3]
list_data = [1, 2, 3]
list_data[1] = 100
print(list_data)

# Error
# tuple_data = 1, 2, 3
# tuple_data[1] = 100
```

# `range()`

n ~ m-1, sep을 증가시킨다.

`range(n), range(n, m), range(n, m, sep)`
```python
import random
numbers = range(1, 46)
# result randomValue
print(random.choice(number))
# result randomValue
print(random.sample(number,2))

# result 0~-9
numbers = list(range(0, -10, -1))
print(numbers)

# result 2의 배수
numbers = list(range(0, 20, 2))
print(numbers)

# result [0, 0, 0, 0, 0, 0]
print([0] * 6)
```

## `sort()`
```python
import random
chois = 6
numbers = range(1, 46)
lucky = random.sample(numbers, chois)
lucky.sort()
print(lucky)
```

# indexing slicing
```python
locations = ['강남', '서초', '송파', '광진', '마포']

# result ['서초', '송파']
print(locations[1:3])

numbers = list(range(0, 31, 3))

# list[x:y:z] => x~y-1, step z
# result 1 3 5 7 9
print(numbers[1:10:2])
# result numbersValue 
print(numbers[:::])
```

## list method
`len()` : 배열 안의 갯수

`min(), max()` : 최소값, 최대값
```python
numbers = range(0, 31)
# result 30
print(len(numbers))

# result 0 30
print(min(numbers), max(numbers))
```

# set
1. 순서가 없는 자료구조
2. 중복 불가
3. 빈집합 {} 사용으로 할당 불가 (set() 사용)

```python
# 중복값을 제거하고 싶을때
list_data = [1, 2, 1, 3, 4, 1, 2]

# result 1, 2, 3
print(set(list_data))
```

## 집합 연산
|연산자/함수|설명|
|---|---|
|a `-` b|차집합|
|a `\|` b|합집합|
|a `&` b|교집합|
|a`.difference(b)`|차집합|
|a`.union(b)`|합집합|
|a`.intersection(b)`|교집합|
```python
set_data1 = {1, 2, 3}
set_data2 = {3, 6, 9}

# 차집합 (빼고 남은거) result 1, 2
print(set_data1 - set_data2)

# 합집합 (다합침) result 1, 2, 3, 6, 9
print(set_data1 | set_data2)

# 교집합 (두개가 교차되는 것) result 3
print(set_data1 & set_data2)
```

# dictionary
1. key, value로 이루어져 있음 (hashMap)
2. key는 중복 불가
3. `dict()`로 만들 수 있음
```python
dic_data = {
    '커피' : 'coffee',
    '우유' : 'milk',
    '물' : 'water'
}

real_data = [
    {
        '커피' : 'coffee',
        '우유' : 'milk',
        '물' : 'water'
    },
    {
        'name' : 'my',
        'contry' : '한국',
        'location' : '성동구'
    }
]

# key 값 확인
print(real_data.keys())

# value 값 확인
print(real_data.values())

# key, value 둘 다 확인
print(real_data.items())

# modify
dic_data['커피'] = '커피'
print(dic_data)

# append
dic_data['스무디'] = 'smoothie'
print(dic_data)
```



























