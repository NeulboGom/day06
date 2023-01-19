#Chapter9 Function - Generator


#  Decorator
def document_it(func):
    def new_function(*args,**kwargs):
        print("Running function:", func.__name__)  #  실행 중인 함수의 이름 출력
        print("Positional arguments:", args)  #  위치 기반 인수들, 튜플 출력
        print("Keyword arguments:", kwargs)   #  키워드 기반 인수들, 딕셔너리 출력
        result = func(*args,**kwargs)  #  결과=정의된 new_function의 결과
        print("Result:", result)   #  결과를 출력
        return result              #  결과를 return
    return new_function            #  new_function을 return



def add_ints(a,b):
    return a + b

print(add_ints(3,5))

cooler_add_ints=document_it(add_ints)   #  Decorator 수동 할당
print(cooler_add_ints(3,5))
#  출력 결과:
#  Running fuction: add_ints
#  Positional arguments: (3,5)
#  Keyword arguments: {}
#  Result 8
#  8

#------------------------------------------------------------
#  @Decorator_name
@document_it            #  def로 함수 만들기 이전에 @데코레이터 이름을 출력
def substract_ints(a,b):
    return a - b

substract_ints(8,5)
#  출력 결과:
#  Running fuction: substract_ints
#  Positional arguments: (8,5)
#  Keyword arguments: {}
#  Result 3
#  8

#------------------------------------------------------------------------

def square_it(func):        #  result를 제곱하는 Decorator
    def new_function(*args, **kwargs):
        result = func(*args,**kwargs)
        return result * result
    return new_function

print("="*60)

@document_it
@square_it
def add_ints(a,b):
    return a + b

add_ints(3,5)

print('='*60)

@square_it              #  순서에 따라 결과가 다르다
@document_it
def add_ints(a,b):
    return a + b

add_ints(3,5)


print("="*60)


