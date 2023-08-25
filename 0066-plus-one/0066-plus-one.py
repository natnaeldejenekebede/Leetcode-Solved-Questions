class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1 
        result = []

        for digit in reversed(digits):
            new_digit = digit + carry
            carry = new_digit // 10
            result.append(new_digit % 10)

        if carry:
            result.append(carry)

        return result[::-1]  
    
    
