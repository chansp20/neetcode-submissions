class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        int_stack = []
        operators = ["+","-","/","*"]
        for i in tokens:
            
            if i not in operators :
                int_stack.append(i)
            else:
                val1=int_stack.pop()
                val2=int_stack.pop()
                if i == "+":
                    exp = int(val2) + int(val1)
                elif i == "-":
                    exp = int(val2)-int(val1)
                elif i == "*":
                    exp = int(val2) * int(val1)
                elif i == "/":
                    exp = int(int(val2)/int(val1))
                int_stack.append(exp)
        return int(int_stack[-1])

                
        
        