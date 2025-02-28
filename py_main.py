'''튜플은  () 괄호를 사용해 정의 한다 리스트와 차이점은 튜플은 값을 변경할수없다'''

a = (1,2,[3,4])

a[2][0] = 6
# indexing 할떄 [] 로 접근
# [] 는 인덱스로 위치에 접근할떄 , 리스트 생성할떄만 사용
# () 는 함수호출할떄 , 튜플 생성할떄사용 요소가 하나일때는 , 붙이고 ,함수정의시 매개 변수 
#{} 는 문자열 안에 변수나 표현식을 넣을때 , 셋 생성할떄 

def add(a,b):
    return a + b

# 위 함수는 add 라는 이름이고입력으로 2개의 값을 받는다  출력값은 입력값을 더한값이다
    
def add(a, b): # a,b는 매개변수이다 파라미터
    return a+b 

print(add(3,4)) # 3,4는 인수이다 어그먼트 
#파라미터는 함수에 입력으로  전달된 값을 받는 변수
# 인수는 함수를 호출할떄  전달하는값


# *args 여러개의 인자를 받을수있음
#키워드 매개변수는 **를 붙임
# 함수는 return값을만나는순간출력하고 빠져버린다 그래서 return 두개 못씀

def say_nick(nick): 
    if nick == "바보": 
        return # 이렇게 되어있으면 return값은 바로 빠져나간다 
    print("나의 별명은 %s 입니다." % nick)
    
'''
>>> say_nick('야호')
나의 별명은 야호입니다.
>>> say_nick('바보')
>>>
''' 

# https://wikidocs.net/28 클래스 이해 개잘된다

# 아래 a는 객체이고 cookie클래스의 인스턴스다
# a = cookie() 
# 클래스 안에 구현된 함수는 매서드다

# foorcal 클래스
class FourCal:
    # 매서드
    def setdata(self, first, second): # 매서드의 매개변수
        self.first = first # 매서드의 수행문 
        self.second = second # 매서드의 수행문 


# . 연산자는 객체의 속성접근, 
# person.name은 person 객체의 name 속성에 접근합니다
# 매서드 호출
# string.upper()는 string 객체의 upper() 메서드호출
# 모듈내의 요소접근
#  math.sqrt(16)은 math 모듈의 sqrt 함수를 호출합니다.
# 네임스페이스 구분 
# module.class.method()와 같은 계층적 접근 가능 url 에서 / 랑 비슷하네

# a.setdata(4, 2) 면 def setdata(self, first, second):  에서 
# self 에  a가 들어가서 매개변수가 2개만 있어도 되는구나

# 객체에 생성되는 객체만의 변수를 ‘객체변수’ 또는 ‘속성’이라고 부른다. 
# a.first = 4 에서 4는 객체변수, 속성이다

# 클래스로 만든 객체의 객체변수는 다른 객체의 객체변수에 상관없이 독립적인 값으로 유지된다

# a에 setdata 매서드가 없으면 다른 매서드들이 실행이안된다 그래서 초기값 매서드가 있어야한다 근데 초기값 매서드를 생성하는것보다 생성자를 구현하는것이 더 안전한 방법이다 
# 생성자를 constructor라 부르고  객체가 생성될떄 자동으로 호출되는는 매서드를 의미한다
# 파이썬 매서드 명으로는 __init__ 를 사용하면 이매서드는 생성자가 된다

>>> class FourCal:
...     def __init__(self, first, second): # setdata를 __init__ 으로 바꿨다 
...         self.first = first
...         self.second = second
...     def setdata(self, first, second):
...         self.first = first
...         self.second = second
...     def add(self):
...         result = self.first + self.second
...         return result
...     def mul(self):
...         result = self.first * self.second
...         return result
...     def sub(self):
...         result = self.first - self.second
...         return result
...     def div(self):
...         result = self.first / self.second
...         return result

# 메서드 이름을 __init__로 했기 때문에 생성자로 인식되어 객체가 생성되는 시점에 자동으로 호출된다는 차이점이 setdata와 있다

# __init__이 자동으로 생성되서
a = FourCal()을 수행할 때 생성자 __init__가 호출되어 위와 같은 오류가 발생했다. 
오류가 발생한 이유는 생성자의 매개변수 first와 second에 해당하는 값이 전달되지 않았기 때문이다.

이 오류를 해결하려면 다음처럼 first와 second에 해당하는 값을 전달하여 객체를 생성해야 한다.
a = FourCal(4, 2)
이렇게 
a = FourCal() 예전과 같이 
>>> a = FourCal()
>>> a.setdata(4, 2) 
이렇게 정의 하고 넘어가지 않는다

# 클래스의 상속

# 부모클래스의 있는 매서드를 동일한이름으로 다시 만드는것 > 변형하는것  이게 메서드 오버라이딩(method overriding 이다
# 이렇게 매서드를 오버라이딩하면 부모클래스 매서드대신 오버라이딩한 매서드가 호출됨
# 그래서 자녀클래스의 매서드를 바꿔 오버라이딩해도 부모클래스는 영향을 받지 않다


# 클래스변수는 "클래스_이름.클래스변수 " 로 사용할수있더
>>> class Family:
...     lastname = "김"
>>> Family.lastname
김

# 헌업에서는 객쳐번수를 훨씬 많이써서 클래스변수보다 중요도가 높다
