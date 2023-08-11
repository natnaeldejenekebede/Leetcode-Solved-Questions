class Solution:
    def isValid(self, s: str) -> bool:
        Stack = []
        closeTOopen = {"}" : "{" , ")" : "(" , "]" : "["}

        for c in s:
            if c in closeTOopen:
                if Stack and Stack[-1] == closeTOopen[c]:
                    Stack.pop()
                else:
                    return False
            else:
                Stack.append(c)
        return True if not Stack else False       

