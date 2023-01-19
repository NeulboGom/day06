#Chapter 10 객체와 클래스

#  What is Object?
#  객체는 데이터(변수, 속성-attribute)와 코드(함수, 메서드-method)를 포함하는 커스텀 자료구조
#  ex) 도형을 그리라고 하면 여러 도형이 나옴 - 추상적임 // 삼각형을 그려라고 하면 삼각형을 그림 - 구체적인
#  객체는 개별 사물을 나타내고, 해당 메서드는 다른 사물과 상호작용하는 방법을 정의한다.
#  ex) 메서드= 잠을 자거나, 음식을 먹거나(사람마다 먹는게 다름)


#  Class 선언하기 - single로 할 때는 괄호 없어도 되는데, 상속 받을 때는 괄호 안에 부모 class가 들어가야함
class Cat:          #  클래스 생성
    pass

a_cat=Cat()         #  객체 생성
another_cat=Cat()

a_cat.age = 3
a_cat.name = "Nero"
a_cat.namesis = another_cat         # another_cat을 참조하고 있다...?

#a_cat.namesis.name          #another_cat에 name이 Attribute 되지 않았다.
a_cat.namesis = 'Navi'


#  Method - 클래스 안에 있는 함수들 / 함수랑 비슷하다. 다만 특별한 방식으로 사용된다.
#  Initialization - 초기화
class Cat:
    def __init__(self):         #  객체가 생성될 때 무조건 실행되는 코드
        pass


class Pokemon:
    def __init__(self):             #  객체가 생성될 때 무조건 실행되는 코드 / self는 자동으로 붙음
        print("포켓몬 객체 생성됨")


p1 = Pokemon()
p2 = Pokemon()
print(p1,p2)        #  다른 메모리 번지를 참조하고 있다.


class Pokemon:
    def __init__(self, name, owner, skills):               #   name이 추가된 것은, 객체 생성 시에 이름까지 지어줄 수 있음
        self.name = name
        self.owner = owner                      #  owner 설정
        self.skills = skills.split('/')
        print(f"포켓몬 {name} 생성됨")             #  전달되는 name은 self.name에 대입이 된다.

    def info(self):                             #  멤버 함수라고 한다.
        print(f"{self.owner}의 포켓몬은 {self.name}입니다.")        #  self 자리에 p1,p2,p3 등 생성되는 객체가 들어감
        for skill in self.skills:
            print(skill)


p1 = Pokemon("피카츄","한지우", "50만 볼트/100만 볼트/번개")
p2 = Pokemon("꼬부기","오바람", "고속스핀/거품/몸통박치기/하이드로펌프")

p1.info()

p2.info()
# print(p2.skills)
# print(f"{p1.owner}의 포켓몬은 {p1.name}입니다.")
# print(f"{p2.name}는 {p2.owner}의 포켓몬입니다.")
#print(p1,p2)


#  Inheritance: 상속  강한 결속 관계를 맺어주는 '상속' / 부모 클래스가 가진 자원을 자식 클래스가 가질 수 있다
#  상속의 가장 큰 장점 - 코드의 중복을 피할 수 있다.


