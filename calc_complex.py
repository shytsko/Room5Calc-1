def _ConvertRPN(inputSequence: list) -> list:
    operatorsPriority = {'+': 1, '-': 1, '/': 2, '*': 2}
    outputSequence = []
    stack = []
    for token in inputSequence:
        if token == '(':
            stack.append(token)
        elif token == ')':
            while stack[-1] != '(':
                outputSequence.append(stack.pop())
            stack.pop()
        elif token in operatorsPriority.keys():
            while len(stack) > 0 and stack[-1] in operatorsPriority.keys():
                if operatorsPriority[stack[-1]] >= operatorsPriority[token]:
                    outputSequence.append(stack.pop())
                else:
                    break
            stack.append(token)
        else:
            outputSequence.append(token)
    while len(stack) > 0:
        outputSequence.append(stack.pop())
    return outputSequence

def _CalcRPN(rpnSequence: list) -> float:
    operators = {'+': lambda a, b: a + b,
                 '-': lambda a, b: a - b,
                 '/': lambda a, b: a / b,
                 '*': lambda a, b: a * b}
    stack = []
    for token in rpnSequence:
        if token in operators.keys():
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(operators[token](operand1, operand2))
        else:
            stack.append(complex(token) if token[-1] == 'j' else float(token))
    return stack[0]


def CalculatorComplex(eval: str) -> str:
    operators = {'+', '-', '/', '*', '(', ')'}
    for o in operators:
        eval = eval.replace(o, f' {o} ')
    tokens = eval.split()
    rpn = _ConvertRPN(tokens)
    return str(_CalcRPN(rpn))