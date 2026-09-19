def op(val1:str, val2:str, operand: str) -> int:
    val1 = int(val1)
    val2 = int(val2)
    if operand == "+":
        return val1+val2
    elif operand == "-":
            return val1-val2
    elif operand == "*":
            return val1*val2
    elif operand == "/":
            return val1/val2
    


def evalRPN(tokens: list[str]) -> int:
    stack = []
    for t in tokens:
        if t not in ("+", "-", "*", "/"):
              stack.append(t)
        else:
            first = stack.pop()   
            second= stack.pop() 
            stack.append(op(second,first,t))

    res = int(stack.pop())

    return res
