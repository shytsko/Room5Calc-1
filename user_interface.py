from calc_complex import CalculatorComplex
from calc_real import CalculatorReal
from history import result_logger,counter
menu='\033[32m1. Назад - нажмите "Q"\033[0m.\n\033[33m2. Справка - нажмите "S"\033[31m\n3. Выход - "E".\033[0m'
pos=counter()
def calc_comp(count=pos,msg='Complex numbers'): 
    try:
        mathExp=input('Введите выражение: ')
        if mathExp.upper()=='Q' or  mathExp.upper()=='Й': 
            UserMane(count)
        elif mathExp.upper()=='S' or  mathExp.upper()=='Ы':
            print('Работа программы с комплексными числами: \033[32m(2+3j)*(6+12.3j)\033[0m \nОтвет: \033[36m(2+3j)*(6+12.3j) = (-24.900000000000006+42.6j)\033[0m')
            calc_comp()
        elif mathExp.upper()=='E' or  mathExp.upper()=='У': return
        else:
            calc=CalculatorComplex(mathExp)
            result=(f'{mathExp} = {calc}\n')
            print(result)
            result_logger(count,result,msg)
            calc_comp(count+1)
    except:
        print('\033[31mОшибка! повторите ввод!\033[0m')
        calc_comp(count=count)
def calc_real(count=pos,msg='Rational numbers'): 
    try:
        mathExp=input('Введите выражение: ')
        if mathExp.upper()=='Q'or  mathExp.upper()=='Й': UserMane(count)
        elif mathExp.upper()=='S' or  mathExp.upper()=='Ы':
            print('Работа программы с рациональными числами:\033[32m (1+2)*4+3\033[0m\nОтвет: \033[36m(1+2)*4+3= 15.0\033[0m')
            calc_real()
        elif mathExp.upper()=='E' or  mathExp.upper()=='У': return
        else:
            calc=CalculatorReal(mathExp)
            result=(f'{mathExp} = {calc}\n')
            print(result)
            result_logger(count,result,msg)
            calc_real(count+1)
    except:
        print('\033[31mОшибка! повторите ввод!\033[0m')
        calc_real(count=count)
def UserMane(temp=pos):
    try:
        count=temp
        number = int(input('\n\033[1m\033[33m\033[44m       М Е Н Ю:       \033[0m\n\033[32m1. Комплексные числа\033[0m\n\033[35m2. Рациональные числа\033[0m\n\033[31m3. Выход\033[0m\n\033[3mВведите значение: \033[0m'))
        match number:
            case 1:
                print(f'Вы находитесь в меню расчета комплексных чисел.\n{menu}')
                calc_comp(count)
            case 2:
                print(f'Вы находитесь в меню расчета комплексных чисел.\n{menu}')
                calc_real(count)
            case 3: 
                return
    except:
        print('\033[33mОшибка! Введите число \033[0m\033[32m1   \033[0m\033[35m2   \033[0m\033[31m3\033[0\033[33m для перехода в меню.\033[0m')
        return UserMane()
