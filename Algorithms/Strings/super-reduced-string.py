def superReducedString(s):
    stack=[]
    for char in s:
        if stack and stack[-1]==char: #Stack boş değilse ve en son eklenen eleman ile aynı ise
            stack.pop() 
        else:
             stack.append(char) 
    if not stack:
        return "Empty String"
    else:
        return "".join(stack) 