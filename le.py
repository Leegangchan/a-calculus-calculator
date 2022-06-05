from sympy import *
import sys


def differential(fx, var):
    Cal1 = Derivative(fx, var).doit()

def integral(fx, var, intvl):
    Cal2 = Integral(fx, (var, intvl[0], intvl[1])).doit()


while true:


#입력 받기
    var = input('적분변수를 입력하세요: ')
    fx = input('피적분 함수를 입력하세요(입력예:x**2+1): ')
    a, b = input('적분 구간을 입력하세요(입력예:0 1): ').split()

#symbol 생성
    var = Symbol(var)



#적분구간
    intvl = [a, b]


#결과 출력
    print(Integral(fx, var).doit())
    print(Integral(fx, (var, intvl[0], intvl[1])).doit())

    while true:
        co = input('다른것도 적분하나요?(y, n): ')
        if co == 'y':
            break

        elif co == 'n':
            sys.exit()

        else:
            print('음...그거맞나요?')
            continue



