# 객체지향 프로그램 (OOP)
python에서 모든 것은 객체이다
- 코드의 직관성
- 활용의 용이성
- 변경의 유연성

# `self`
객체 자신

```python
# 오류
"""
class Person:
    def __init__(name, age):
        self.name = name
        self.age = age
my_person = Person('짱구', 5)
"""

# self를 사용해야 함, self로 자신의 attribute를 변경하기 위함
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
my_person = Person('짱구', 5)
```

# 생성자 메서드
`__init__`
```python
class Person:
    # 생성자 메서드(최초 Person Instance 생성시 호출)
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # 메서드
    def talk(self):
        return f'나의 이름은 {self.name}입니다. 나이는 {self.age}입니다'

my_person = Person('짱구', 5)
my_person.talk()

# 두 객체는 다른 객체
person1 = Person('신짱아', 3)
person2 = Person('신영만', 30)

# person1 객치의 attribute name의 속성을 변경
person1.name = '홍길동'
person1.age = 35

type(person1)
type(person2)
```

# 객체 비교법
- `is` : 객체의 주소값을 비교한다.
- `isinstance` : 객체의 주소값을 보고 같은 주소값인지 비교
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def my_self(self):
        return self

my_list1 = []
my_list2 = []

# 객체 안의 attribute들을 비교
my_list1 == my_list2

# 객체의 주소값을 비교
my_list1 is my_list2

person1 = Person('짱구', 5)

person1 == person1.my_self()
person1 is person1.my_self()
```

## dir
객체가 가지고 있는 메소드들을 확인가능
```python
dir([])
dir(123)
dir('')
```

# 소멸자 메서드
`__del__`

```python
class Person:
    def __init__(self):
        print('생성')
    def __del__(self):
        print('죽음')

person = Person()
```

# `__str__(self)` 메서드
특정 객체를 출력(`print()`)할 때 보여줄 내용 정의
```python
class Person:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):  # displayname
        return f'나는 {self.name}'
    
    def __repr__(self):  # username
        return f'I am {self.name}'

person = Person('짱구')
print(person)
```

# 인스턴스(Instance)간 대/소 비교
`__gt__`(크냐) 또는 `__eq__`(같냐) 재정의(oerride) 하지 않으면 기본적으로 주소값을 비교한다.
```python
class Person:
    # override
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # override
    def __gt__(self, other):
        return self.age > other.age
    # override
    def __eq__(self, other):
        # 아까까진 self와 orher의 id비교였으나, 이제는 나이비교
        return self.age == other.age

p1 = Person('yu', 1)
p2 = Person('kim', 2)
p3 = Person('park', 1)


print(p1 == p3)
print(p1 == p2)
print(p1 > p2)
p1.__eq__(p3)
```
# 클래스
## 클래스 변수
- 모든 인스턴스가 공유
- 클래스의 attribute

```python
class Circle:
    pi = 314e-2
    # pi = 3.141592
    def __init__(self, r):
        self.r = r
    def area(self):
        return self.r**2 * self.pi


my_circle1 = Circle(4)
my_circle1.area()

my_circle2 = Circle(10)
my_circle2.area()
# my_circle2가 다른 attribute를 가짐
my_circle2.pi = 3.141592

# result 3.14, 3.141592
print(my_circle1.pi, my_circle2.pi)
```

## 주석
객체 사용설명서 `__doc__`
```python
type("""
이건 str인데 
왜 주석이라고하는걸까?
""")

class Person:
    """
    이건 여러줄 메모줄을 남기기 위해 쓰더라
    주석
    주석
    """

my_person = Person()
# 사용설명서
my_person.__doc__
```

# 클래스 메서드 (class method), 스태틱 메서드 (static method)
- `@classmethod` : **메소드 호출시, 첫 번째 인자로 cls가 전달됨**
- `@static method` : **JAVA static method와 동일**
```python
class MyClass:
    # method 정의시 아무말 없으면 => instance method
    def instance_method(self):
        return self
    
    @classmethod
    def class_method(cls):
        return cls
    
    @classmethod
    def cm(cls):
        return 1
    
    @staticmethod
    def static_method(arg):
        return arg
    
    @staticmethod
    def aa(self):
        print('aa')


# 같은 인스턴스인지 비교
MyClass.class_method() is MyClass
isinstance(MyClass(), MyClass.class_method())


mc = MyClass()
mc.instance_method()
mc.class_method()
```
# OOP의 핵심 개념
- 추상화
- 상속
- 다형성
- 캡슐화

## 상속(Inheritance)
부모 클래스의 모든 속성이 자식 클래스에게 상속되는 것
```python
class Person:
    population = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.population += 1
    def talk(self):
        print(f'안녕하세요, {self.name}입니다. 나이는 {self.age} 입니다.')

class Student(Person):
    def __init__(self, name, age, score):
        self.score = score
        Person.population += 1
    def study(self):
        self.score += 1
        
s1 = Student('kim', 20, 90)
s1.name, s1.age
s1.talk(), s1.population
```

## 추상화(Abstraction)
여러 클래스가 공통적으로 사용할 속성 및 메서드를 추출한다.
```python
# 추상 클래스
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def talk(self):
        print(f'안녕하세요, {self.name}입니다. 나이는 {self.age} 입니다.')

class Student(Person):
    def __init__(self, name, age, score):
        self.score = score
        self.name = name
        self.age = age
    def study(self):
        self.score += 1

class Teacher(Person):
    def __init__(self, name, age, money):
        self.money = money
        self.name = name
        self.age = age
    def money(self):
        self.money += 100

student = Student('짱구', 5, 1)
teacher = Teacher('견미리', 29, 100)

student.talk()
teacher.talk()
```
## `super()`
- 자식 클래스에서 부모 클래스 호출 시, 사용

```python
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email 
        
    def greeting(self):
        print(f'안녕, {self.name}')
        
class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        super().__init__(name, age, number, email)
        self.student_id = student_id
        
        
person = Person('홍교수', 200, '0101231234', 'hong@gildong')
student = Student('학생', 20, '12312312', 'student@naver.com', '190000')

person.greeting()
student.greeting()
```

## 다형성
- 동일한 메서드가 클래스에 따라 다르게 행동 할 수 있음을 뜻함

> ## 메서드 오버라이딩(override)
- 부모의 메서드를 재정의하는 것
```python

class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email 
        
    def talk(self):
        print(f'안녕, {self.name}')

        
class Soldier(Person):
    # override
    def __init__(self, name, age, number, email, army):
        super().__init__(name, age, number, email)
        self.army = army
    # override
    def talk(self):
        print(f'충성, 상병 {self.name}')


class Animal:
    # 이 클래스를 상속받은 클래스들은 모두 name을 알고 있음
    name = ''
    def __init__(self, name):
        # Animal 클래스의 name을 변경함
        Animal.name = name        
    def talk(self):
        print('으르렁')
    def my_func(self):
        return f'나의 이름은 {self.name} 입니다. 내 이메일은 {self.email}'

class Person(Animal):
    def __init__(self, name, email):
        # 따로 attribute를 가지지 않고 Animal 클래스의 name이 변경됨
        super().__init__(name)
        self.email = email
    def talk(self):
        print('안녕')
        
dog = Animal('강아지')
dog.talk()

person = Person('kim','@namer.com')
person.talk()
person.my_func()
```

# 캡슐화(Encapsulation)
- public
- protected
- default
- private

## public
- 어디에서나 호출가능
- 언더바(_)가 없음

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

student = Student('짱구', 5)
```

## protected

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        # _가 붙은 객체 속성(age)은 부모 자식만 가능
        self._age = age
    def get_age(self):
        return self._age
    def set_age(self, age):
        if age > 0:
            self._age = age
        else:
            print('응 안되!')  # Developper eXerience
    def talk(self):
        print('hi')
        
p1 = Person('kim', 30)

print(p1.get_age())
p1.set_age(-10)
print(p1.get_age())
# 되지만 하지 않는다.
p1._age = 20
```

## private
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    def get_age(self): 
        return self.__age
    def set_age(self, age):
        self.__eat()
        self.__age = age
    def __eat(self):
        print('냠냠')

p1 = Person('ua', 20)
print(p1.get_age())
# 접근불가
# p1.__eat()
```
# 다중상속
```python
class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        return f'안녕, {self.name}'

class Mom(Person):
    gene = 'XX'
    def swim(self):
        return '어푸어푸'

mom = Mom('봉미선')
print(mom.greeting(), mom.swim())

class Dad(Person):
    gene = 'XY'
    def walk(self):
        return '성큼성큼'

dad = Dad('신형만')
print(dad.greeting(), dad.walk())


class FirstChild(Dad, Mom):
    # override
    def swim(self):
        return '첨벙첨벙'
    def dance(self):
        return '부리부리'

fc = FirstChild('신짱구')
print(fc.greeting(), fc.walk(), fc.swim(), fc.dance())

class SecondChild(Mom, Dad):
    pass
sc = SecondChild('짱아')
# result XX Mom 클래스를 먼저 상속받았기 때문
print(sc.gene)
```


