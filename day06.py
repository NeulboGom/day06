#Chapter9 Function - Generator

#Single resposibility -> 단일 뭐시기...

#Generator function
def my_range(first=0, last=10, step=1):
    number=first
    while number<last:
        yield number
        number+=step

ranger=(my_range(1,5))
for x in ranger:
    print(x)

print(my_range(1,5))

for try_it_again in ranger:     #  한 번 더 출력하면 안 나옴 // generator는 한 번만 순회 가능
    print(try_it_again)


def a():        #  Generator
    yield 1     #return과 다르게 하나 출력해도 바로 종료되지 않고 마지막 yield까지 종료
    yield 2
    yield 3


def b():        #  Normal Function
    return 1    #  return인 경우 맨 위에 하나만 return하고 바로 함수를 종료 // stop iteration
    return 2
    return 3

print(a(),'\n',b())
c=a()
print(c)
for i in c:
    print(i)


#  Generator Comprehension
genobj = (pair for pair in zip (['a','b'],['1','2']))
print(genobj)
for thing in genobj:
    print(thing)

