class Solution:
    def romanToInt(self, s: str) -> int:
           dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
           num = 0
           index = 0
           while index < len(s):
               try:
                   if dict[s[index]] < dict[s[index + 1]]:
                        num = num + dict[s[index + 1]] - dict[s[index]]
                        index = index + 2
                   else:
                       num = num + dict[s[index]]
                       index = index + 1
               except:
                    num = num + dict[s[index]]
                    index = index + 1
               
                    
           return num
