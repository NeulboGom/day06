#Chapter 10 객체와 클래스

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

class Pikachu(Pokemon):             #  Pikachu가 Pokemon으로부터 상속을 받음
    pass

pi1 = Pikachu('피카츄','한지우', "50만 볼트/100만 볼트/번개")
pi1.info()

# Pikachu에는 아무것도 없는데, Pokemon 클래스에 있는 걸 이용  // 만약 복붙하면 중복된 코드가 발생