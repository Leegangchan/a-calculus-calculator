from sympy import *
import sys


def differential(fx, var):
    Cal1 = Derivative(fx, var).doit()
    return Cal1

def integral(fx, var, intvl):
    Cal2 = Integral(fx, (var, intvl[0], intvl[1])).doit()
    return Cal2

while true:
    
    Calculus = input('미분할건가요?적분할건가요?아니면 멈추나요?(입력예:미분, 적분, 멈춰): ')
    if Calculus == '미분':
       fx = input('미분할 함수식을 입력하세요(입력예:x**2): ')
       var = input('그냥 미분에 기준이되는 변수를 입력하세요: ')

       var = Symbol(var)

       Cal1 = differential(fx, var)

       print('result:f(x) = {0}'.format(Cal1))
    elif Calculus == '적분':
        var = input('적분변수를 입력하세요: ')
        fx = input('피적분 함수를 입력하세요(입력예:x**2+1): ')
        a, b = input('적분 구간을 입력하세요(입력예:0 1): ').split()

        var = Symbol(var)

        intvl = [a, b]

        Cal2 = integral(fx, var, intvl)

        print('result1: {0}'.format(Integral(fx, var).doit()))
        print('result2: {0}'.format(Cal2))
    elif Calculus == '멈춰':
        print('작동을 정지합니다')
        break
    
    else:
        print('저가 물어본건 그게 아닌데요?')
        continue


        

