class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        fibonacci_numbers = [0] * (n + 1)
        fibonacci_numbers[1] = 1
        fibonacci_numbers[2] = 1

        for i in range(3, n + 1):
            fibonacci_numbers[i] = fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2]

        return fibonacci_numbers[n]
