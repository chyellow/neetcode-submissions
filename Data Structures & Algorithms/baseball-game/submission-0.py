class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        result = 0
        stack = []

        for string in operations:
            if string == "+":
                stack.append(int(stack[-1] + stack[-2]))
            elif string == "D":
                stack.append(int(stack[-1] * 2))
            elif string == "C":
                stack.pop()
            else:
                stack.append(int(string))
        
        for num in stack:
            result += num
        
        return result