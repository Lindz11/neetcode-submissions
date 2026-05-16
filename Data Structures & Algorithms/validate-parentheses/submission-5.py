class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if len(stack) > 0:
                if char == ')' and stack[-1] == '(':
                    stack.pop()
                elif char == '}' and stack[-1] == '{':
                    stack.pop()
                elif char == ']' and stack[-1] == '[':
                    stack.pop()
                else: 
                    stack.append(char)
            else: 
                stack.append(char)

        
        if len(stack) == 0:
            return True
        
        return False

                


