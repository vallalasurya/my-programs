def matched(s):
    stack=[]
    for char in s:
        if char=='(':
            stack.append(char)
        elif char==')':
            if not stack:
                return False
            stack.pop()
            return not stack 
#test cases
print(matched("(7)(a"))
print(matched("a)*(?"))
print(matched("((jkl)78(A)&l(8(dd(fji:)):)?)"))  