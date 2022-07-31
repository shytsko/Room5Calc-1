from calc_complex import CalculatorComplex
def CalculatorReal(eval: str) -> str:
    if "j" in eval:
        return "Этот модуль не работает с комплексными числами"
    return CalculatorComplex(eval)