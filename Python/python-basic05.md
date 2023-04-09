# Value copy (Shallow Copy)
얕은 복사

1 차원
```python
import copy
# primitive 복사는 메모리 주소값이 따로 존재한다
num1 = 123
copy_num1 = num1
num2 = 'abcd'
copy_num2 = num2
num3 = True
copy_num3 = num3
num4 = None
copy_num4 = num4

# 1차원 복사
list_data = [1, 2]
copy_list_data = list_data[:]  # 밑에와 같은 결과
copy_list = copy.copy(copy_list)  # 위와 같은 결과

# reference 복사
list_data = [1, 2]
copy_list_data = list_data
dict_data = {'key':'value'}
copy_dict_data = dict_data
tuple_data = (1, 2,)
copy_tuple_data = tuple_data
def func(x):
    return x
```

# Referece Copy (deep Copy)
깊은 복사

2 차원 이상 사용
```python
import copy

list_data = [
    [1, 2, 3],
    [1, 2, 3],
]
copy_list = copy.deepcopy(list_data)
```

# Call By Value
```python
# 두 결과가 다르다
num = 10

def my_func(num):
    num += 2
    return num

print(my_func(num))
print(num)
```


# Call By Reference
```python

# 두 리스트의 결과가 같다 이유? 같은 주소를 참조하기 때문에
numbers = [1, 2, 3, 4]

def my_func(my_list):
    my_list.append(5)
    return my_list

print(my_func(numbers))
print(numbers)
```

# 함수 스코프
- 전역변수 : 어디서든 알 수 있는 이름
- 지역 변수 : 함수 내에서만 알 수 있는 이름

## 변수 생명주기
- 빌트인 스코프 : 내장변수 - 영원히 유지
- 전역 스코프 : 전역변수 - 인터프리터 종료시, 종료
- 지역 스코프 : 지역변수 - 함수 종료시, 소멸


## 이름 규칙
* `L`ocal scope

* `E`nclosed scope

* `G`lobal scope

* `B`uilt-in scope

```python
# LEGB 룰 
# Built-in > Global > Local

a = 10  # Global
b = 20  # Global

# `E`nclosed
def enc():
    print('check')  # Built-in
    a = 30  # Local
    def loc():
        c = 40    # Local
        print(a)  # Enclosed
        print(b)  # Global
    loc()
    
enc()

# 전역변수 변경, 권장 x
num = 1
def local_scope():
#     num => 야 이건 함수 내부에서 찾지 말고 밖에 있는 거 말하는거야
    global num
    num = 100
    print('Local', num)
    
local_scope()
print('Global', num)
```

# 재귀함수
자기 자신을 호출하는 것

## 팩토리얼
```python
# 항상 끝나는 조건이 있어야 한다. ex) if n == 1 return 1
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

def fact_while(n):
    total = 1
    while n > 0:
        total *= n
        n -= 1
    return total
```

## 피보나치 수열

```python
def fib(n):
    if n <= 2:
        return n    
    return fib(n-1) + fib(n-2)

# while
def fib_whileloop(n):
    if n <= 2:
        return n
    
    list_data = [1, 1]
    while range(len(list_data), n+1):
         list_data.append(list_data[len(list_data)-1]+list_data[len(list_data)-2])

    return list_data[len(list_data)-1]


# for
def fib_forloop(n):
    if n < 2:
        return n
    result = [0, 1]
    for _ in range(n-1):
        result.append(result[-1]+result[-2])
    return result[-1]
```
