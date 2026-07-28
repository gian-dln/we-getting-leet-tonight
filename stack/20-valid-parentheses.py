def isValid(s: str) -> bool:

    match = { ')' : '(', ']' : '[', '}' : '{'}
    stack = []

   
    
    for i in range(len(s)):
        if s[i] in match:
            if stack and stack[-1] == match[s[i]]:
                stack.pop()
            else:
                return False
        else:
            stack.append(s[i])


            
    return True if not stack else False