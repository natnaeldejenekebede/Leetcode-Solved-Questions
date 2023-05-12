class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = str(x)
        index = 0
        output=True
        while output is True and index <= (len(a) // 2 - 1):
            if a[index] != a[-1 - index]:
                output = False
            index = index + 1
        return output
