#Chapter9 Function - Generator

# Asynchronous function
'''
#Exception

def div_calc(a,b):      #  나누기 프로그램
    """
    나누기 함수
    :param a: 분자
    :param b: 분모
    :return: 계산결과
    """
    return a/b

print(div_calc(15,3))
print(div_calc(15,0))       #ZeroDivisionError 발생
'''

#Try, Except로 예외 처리

while True:
    try:
        expr = input('분자, 분모 입력(띄어쓰기로 구분):').split()
        print(int(expr[0]) / int(expr[1]))
        break
    except ZeroDivisionError as err:
        #print(err) 혹은 f스트링
        print(f"'0'은 분모가 될 수 없습니다.({err})")
    except ValueError as err:
        print(f"숫자를 입력하세요.({err})")
    except IndexError as err:
        print(f"입력 값의 범위에 문제가 있습니다.({err})")
    except Exception as others:
        print(f"예외 발생!({others})")
    # else:                       #  예외가 발생하지 않았을 때 // while과는 같이 못 쓰는 듯
    #     print("프로그램 정상",end=' ')
    # finally:                    #  예외 발생 여부와 상관없이 무조건 실행 // while하고는 안 써도 되는 거 같음
    #     print("종료")

print("="*60)

# Making Exception

try:
    raise Exception("쉬는 시간")              #  강제로 예외를 던지는 키워드 // 예외
    expr = input('분자, 분모 입력(띄어쓰기로 구분):').split()
    print(int(expr[0]) / int(expr[1]))
except ZeroDivisionError as err:
    #print(err) 혹은 f스트링
    print(f"'0'은 분모가 될 수 없습니다.({err})")
except ValueError as err:
    print(f"숫자를 입력하세요.({err})")
except IndexError as err:
    print(f"입력 값의 범위에 문제가 있습니다.({err})")
except Exception as others:
    print(f"예외 발생!({others})")
else:                       #  예외가 발생하지 않았을 때 // while과는 같이 못 쓰는 듯
    print("프로그램 정상",end=' ')
finally:                    #  예외 발생 여부와 상관없이 무조건 실행 // while하고는 안 써도 되는 거 같음
    print("종료")