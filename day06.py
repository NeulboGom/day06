#Chapter9 Function - Generator

#  Namespaces and Scope

g=1     #  global variable

def print_global():
    # g=1   #  local variable
    print(g)

# print_global()   #  지역변수로 인식하니까 출력 오케이
# print(g)        #  함수 영역에 g가 가려져서 출력 불가 - 에러 발생


def change_and_print_global():
    global g        #  전역변수 g를 아래 프린트 g에 할당
    print(g)
    g =2/            #  지역변수로 g를 2에 할당 -> 아래 프린트 g에 할당됨
    print(g)


change_and_print_global()
print(g)

print(locals())
print(globals())
print(__name__)

print("="*60)

#  Recursion  재귀함수 - 자기 자신을 호출하는 함수 // inner함수와 다름
def factorial_iter(n):
    """
    반복문을 사용한 팩토리얼 함수
    :param n: n!
    :return: integer 팩토리얼 계산 결과 값
    """
    result = 1
    for k in range(1,n+1):
        result = result * k
    return result

print(factorial_iter(4))

def factorial_recu(n):
    """
    재귀 함수를 사용한 팩토리얼 함수
    :param n: n!
    :return: 자기 자신을 호출 또는 1
    """
    if n != 1:
        return factorial_recu(n-1)*n
    elif n == 1 or n == 0:        #  끝나는 조건
        return 1
    elif n < 0:
        return 0

print(factorial_iter(4))
print(factorial_iter(0))
print(factorial_iter(2))
print(factorial_iter(-3))
