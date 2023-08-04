class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        abs_x = abs(x)
        
        reversed_str = str(abs_x)[::-1]
        reversed_num = int(reversed_str) * (-1 if is_negative else 1)
        
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        if reversed_num < INT_MIN or reversed_num > INT_MAX:
            return 0
        
        return reversed_num
