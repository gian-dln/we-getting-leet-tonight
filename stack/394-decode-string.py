def decodeString(s: str) -> str:
    stack = []
    currentStr = "" 
    currentNum = 0 # running total of whole number

    for char in s:

        if char.isdigit():
            currentNum= currentNum *10 + int(char)

        elif char == "[":
            # save current progress to stack and repeat
            stack.append((currentStr, currentNum))
            currentStr = ""
            currentNum = 0

        elif char == "]":
            # pop and expand
            previousStr, previousNum = stack.pop()
            currentStr = previousStr + currentStr * previousNum 


        else:
            currentStr += char
        

    return currentStr