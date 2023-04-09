# 식별자
예약어, 공백, 특수문자 사용불가\

```python
# bad SyntaxError
True = 100
False = 100
print = 300
my None = 100
my#$!Var = 200

# good
myTrue = 100
myFalse = 100
myprint = 300
myNone = 100
myVar = 200 
```

# 주석
\# 사용

docstring `__doc__` 사용
```python
# 주석 사용하기
def my_sum(x, y):
    """
    이함수는 인자 x와 y를 더합니다
    더한 값을 리턴합니다
    이런 주석을 docstring 이라고 부릅니다.
    """
    return x + y

print(my_sum.__doc__)
```

# 변수
메모리 할당 `=`

자료형 확인 `type()`

메모리 주소 확인 `id()`

```python
# result 김현수, str, 23145231
name = '김현수'
print(name)
print(type(name))
print(id(name))
```

## 값 동시에 할당
```python
# result 100, 100
x = y = 100
print(x, y)
```

## 스왑(Sawp)
```python
# result x = 2, y = 1
x = 1
y = 2
c = 0

c = y
x = y
y = c

print(x, y)

# result x = 2, y = 1
x = 1
y = 2

x, y = y, x
print(x, y)

# result x = 2, y = 1
x = 1
y = 2
x = x + y
y = x - y
x = x - y
print(x, y)
```

## 변수의 갯수 오류
```python
# Error 변수의 값이 더 적음
x, y, z = 1, 2
print(x, y, z)

# Error 변수의 값이 더 많음
x, y = 1, 2, 3
print(x, y)

# result 1, 2, 3
x, y, z = 1, 2, 3
print(x, y, z)

# result 1, 2
x, y = 1, 2
print(x, y)
```

# 숫자 형 `int` (integer) 
2진수 : 0b, 8진수 : 0o, 16진수 : 0x
## arbitrary-precision arithmetic
메모리를 유동적으로 변환시키는 작업 4바이트가 부족하다면 5바이트 더 부족하다면 6바이트까지 사용

```python
# result 100
num = 100
print(num)

# result 9223372036854775807
import sys
big_num = sys.maxsize
print(big_num)

giant_num = big_num + big_num
print(giant_num)

# 2진수 result 2
bi_num = 0b10
print(bi_num)

# 8진수 result 8
oct_num = 0o10
print(oct_num)

# 16진수 result 16
hex_num = 0x10
print(hex_num)
```

# 실수형 `float`
```python
# result 3.5, float
f_num = 3.5
print(f_num)
print(type(f_num))
```

## 컴퓨터식 지수 표현 방식
e, E를 사용가능
```python
# result 30000000000
big_num = 30000000000
print(big_num)

# result 30000000000.0
big_num = 3e10
print(big_num)

# result 3.14
small_num = 314e-2
print(small_num)
```

## 실수의 연산
```python
# result 6.62
first_num = 3.5
seconde_num = 3.12
sum_num =  first_num + seconde_num
print(sum_num)

# result 0.3799999999999999
minus_sum = first_num - seconde_num
print(minus_sum)
```

## `round()` 함수
반올림 하는 함수 반올림 방식에 따라 다름
```python
# result 0.38
number = 3.5 - 3.12
round(number,2)
```

## 실수 equal
```python
# result False
number1 = 3.5 - 3.12
print(number1 == round(number1,2))

# result True
number2 = 0.38
abs(number1-number2) <= 1e-10

# result True
import sys
abs(number1-number2) <= sys.float_info.epsilon

# result True
import math
math.isclose(number1,number2)
```
# 복소수 `complex` (complex number)
```python
# result 3-4j, complex
number = 3 - 4j
print(number)
print(type(number))

# result 3
print(number.real)

# result 4j
print(number.imag)
```
# bool (boolean)
`True`, `False`
```python
# result bool
print(type(True))
print(type(False))

# result False
print(bool(0))

# result True 0 빼고 모두다 True
print(bool(1), bool(-1), bool(2), bool(1.2))

# result False
print(bool(None))

# result False, True, True
print(bool([]), bool([1,2,3]), bool(['']))

# result False, True
print(bool(''), bool('asas'))
```

# None
값이 없음
```python
# result None
print(type(None))

# result None
none_var = None
print(none_var)
```
# 문자형
``` python
# result 'abc', 'abc', 'asdasd'
print('abc', "abc", 'asdasd')

# result '김현수', str
name = '김현수'
print(name)
print(type(name))
```
## 따옴표 사용
```python
# result 안녕하세요 '처음뵙겠습니다'
print('안녕하세요.\'처음뵙겠습니다.\'')
print('안녕하세요.',"'처음뵙겠습니다.'")
```
## 문자열 +연산 *연산
```python
# result 'HaHaHa 너무 재미있다.'
laugh = 'Ha'
print((laugh*3)+' 너무 재미있다.')
```
## 이스케이프 문자
|예약문자|내용(의미)|
|-|-|
|`\n`|줄 바꿈|
|`\t`|탭|
|`\0`|널(Null)|

```python
# result '첫번째 텍스트\n 개행 후 텍스트   탭한 후 텍스트'
print('첫번째 텍스트 \n 개행 후 텍스트 \t 탭한 후 텍스트')
```
## end
print 함수는 default로 end='\n'이다.
```python
# result '안녕하세요 반갑습니다.^^'
print('안녕하세요', end='')
print('반갑습니다.', end='^^')
```

## String interpolation
```python
# result '제 이름은 김현수 입니다.'
name = '김현수'
print('제 이름은 %s 입니다.'% name)

# result '제 이름은 김현수 입니다.'
print('제 이름은 {} 입니다.'.format(name))

# result '제 이름은 김현수 입니다.'
print(f'제 이름은 {name} 입니다.')

# result '오늘은 22년 12월 14일 Wednesday요일 입니다.'
import datetime
today = datetime.datetime.now()

f'오늘은 {today:%y}년 {today:%m}월 {today:%d}일 {today:%A}요일 입니다.'
```

# 산술 연산자
나눗셈(/)은 항상 float를 돌려준다.
```python
# result 2^1000
print(2 ** 1000)

# result 2.5
print(5/2)

# result 2
print(5//2)

# result 1 3
x, y = divmod(7, 4)
print(x, y)

# result -4 -10 10
pos = 4
neg = -10
print(-pos)
print(+neg)
print(-neg)
```
# 비교 연산자

|연산자|내용|
|----|---|
|`<`|미만|
|`<=`|이하|
|`>`|초과|
|`>=`|이상|
|`==`|같음|
|`!=`|같지않음|
|`is`|객체 아이덴티티|
|`is not`|부정된 객체 아이덴티티|
```python
# result False
print(2 < 1)

# result True
print(3 > 1)

# result True
print(10 >= 10)

# result True
print(10 != 20)

# result True
print('hi' == 'hi')
print('hi' == 'Hi')
```

# 논리 연산자
|연산자|
|-|
|`a and b`|
|`a or b`|
|`not a`|

## And 진리표

|값1|값2|결과|
|-|-|-|
|0|0|False(0)|
|0|1|False(0)|
|1|0|False(0)|
|1|1|True(1)|


## Or 진리표

|값1|값2|결과|
|-|-|-|
|0|0|False(0)|
|0|1|False(1)|
|1|0|False(1)|
|1|1|True(1)|

## Not 진리표
|값1|결과|
|-|-|
|0|True(1)|
|1|False(0)|

```python

# result True
print(True or False)

# result False
print(False and True)

# result False
print(not True)

# result True
print(not 0)

# result True
print(not '')

# result True
print(not [])

# result False
print(not [''])
```

## 단축평가 (short-circuit evaluation)
And는 False(0)가 보이면 더이상 보지 않고 False 처리함
Or는 True(1)가 보이면 더이상 보지 않고 True 처리함

```python
# result 0
print(1 and 2 and 0 and 4)

# result 'a'
print('a' or 'b')

# result 0
print(0 and 1)

# result 11
print(10 and 11)

# result ''
print(0 or '')

# result 1
print(1 or 2)

# result 100
print(0 or 100)

# result 10
print(10 or None)
```

# 복합 연산자

|연산자|내용|
|----|---|
|a += b|a = a + b|
|a -= b|a = a - b|
|a \*= b|a = a \* b|
|a /= b|a = a / b|
|a //= b|a = a // b|
|a %= b|a = a % b|
|a \*\*= b|a = a ** b|

```python
# result 2
num = 0
num = num + 1
num += num
print(num)
```

# 기타 연산자
## Concatenation
```python
# result 'python'
print('py' + 'thon')

# result [1, 2, 3, 4]
print([1, 2] + [3, 4])
```
## Containment Test
```python
# result True
print('a' in 'aeiou')

# result False
print('b' in 'asfd')

# result True
print(1 in [4,3,1,2,3])

# result False
print(100 in [4,3,1,2,3])

# result True
print(1 in range(10))

# result False
print(11 in range(10))

# result False
print(10 in range(10))
```

# Identity
파이썬에서 -5 부터 256 까지의 id(메모리주소값)는 동일하다.

```python
# result  1272353194352,  1272353194352 (같음)
num1 = 5
num2 = 5
print(id(num1), id(num2))

# result 1272477573584, 1272477573296 (다름)
num1 = 257
num2 = 257
print(id(num1), id(num2))


# result 1272477573584, 1272477573296 (다름)
str1 = str2 = '가나다'
print(id(str1), id(str2))

# result 1272353194352,  1272353194352 (같음)
str1 = str2 = 'abcdefg'
print(id(str1), id(str2))
```

# Indexing/Slicing
```python
# result p, o, o, thon, thon
book_name = 'python'
print(s[0], s[4], s[-2], s[2:], s[2:6])

# result my name is kim
names = 'my name is kim'
print(namse[0:])

# result name is
print(names[3:10])
```

# 기초 형변환
## 명시적 형 변환
내가 직접 형변환 하는 것
```python
# result True
print(bool(100))

# result 123
print(int('123'))

# result '1100'
print(str(1100))

# bad Error ValueError
num = '3.5'
print(int(a))
```

## 암시적 형 변환
자동으로 변환되는 것
```python
# result 4, 0
print(True + 3, False * 100)

num = 3
f_num = 5.0
j_num = 2+4j

# result 8.0
print(num + f_num)
# result float
print(type(num + f_num))

# result 5+4j
print(num + j_num)
# result complex
print(type(num + f_num))
```



















