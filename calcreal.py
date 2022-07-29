import calccomplex


def CalculatorReal(eval: str) -> str:
    if "j" in eval:
        return "Этот модуль не работает с комплексными числами"
    return calccomplex.CalculatorComplex(eval)


if __name__ == '__main__':
    test0 = "(1+2)*4+3"
    test1 = "1+2*3"
    test2 = "(1+2j)*3"
    test3 = "1-2j"
    test4 = "(8*(6+3)/(12-9.8))*3.5"
    test5 = "(2+3j)*(6+12.3j)"
    print(f"{test0} = {CalculatorReal(test0)}")
    print(f"{test1} = {CalculatorReal(test1)}")
    print(f"{test2} = {CalculatorReal(test2)}")
    print(f"{test3} = {CalculatorReal(test3)}")
    print(f"{test4} = {CalculatorReal(test4)}")
    print(f"{test5} = {CalculatorReal(test5)}")
