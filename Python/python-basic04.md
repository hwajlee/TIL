# 함수 (Function)
- 가독성
- 재사용성
- 유지보수

## 함수도 객체이다(주소값을 가르킨다)

```python
def cube(x):
    return x ** 3

# result 10 ^ 3
cube(10)


# 반복구간은 변수를 선언하여 처리하자 n//2
def my_list_max(list_a, list_b):
    total_a, total_b = sum(list_a), sum(list_b)
    if total_a > total_b:
        return list_a
    elif total_a < total_b:
        return list_b
    else:
        return '같음'
```
# 매개변수
## 위치 인자
```python
def cylinder(half, height):
    return 3.14 * (half ** 2) * height

# result 1*2*3*4
print(1, 2, 3, 4, sep='*', end='*')
```

# 기본 인자 값
```python
def greeting(name='익명'):
    return print(f'{name}, 안녕?')

# result '익명'
greeting()

# result '짱구'
greeting('짱구')

"""
# Error 
def greeting(name='짱구', age):
    return print(f'{name}의 나이는 {age}입니다.')
"""

def greeting(name, age, addr, phone):
    return print(f'나의 이름은 {name}이고, 나이는 {age}입니다. 현재 사는 곳은 {addr}이며, 핸드폰 번호는 {phone}입니다.')

"""
    # Error
    greeting(addr='떡잎마을',phone='010-1234-1324', '짱구', 20)
    매개변수가 자리를 차지하면 다른 매개변수가 어디에 매핑되어야할지 모름 그렇기에
    매개변수를 아래와 같이 사용할 경우, 할당하는 매개변수를 뒤에 써준다.
"""
greeting('짱구', 5, addr='떡잎마을', phone='010-0000-0000')

# 내장함수
def my_max(x, y):
    return max(x, y)
# result 100
my_max(100, 10)

def my_sum(x, y):
    return sum(x, y)
# result 30
my_sum(10, 20)
# 함수도 값이다 => 변수에 할당 가능하다
def func1(x):
    return x ** 2
f = func1
# result 9
f(3)

# result 4
f = func1(2)
```

