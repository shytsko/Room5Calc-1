from calc_complex import CalculatorComplex
def CalculatorReal(eval: str) -> str:
    if "j" in eval:
        return "\033[31mЭтот модуль не работает с комплексными числами\033[0m"
    return CalculatorComplex(eval)