class Solution:
    def isValid(self, s: str) -> bool:
        d=[]
        for i in s:
            if i=='[' or i=='(' or i=='{':
                d.append(i)
                
            elif i==']' or i==')' or i=='}':
                if len(d) == 0:
                    return False
                top = d[-1]
                if i == ']' and top != '[' or i == ')' and top != '(' or i == '}' and top != '{':
                    return False
                d.pop()
            
        
                
        if len(d) == 0 :
            return True
        else:
            return False
            
        
        