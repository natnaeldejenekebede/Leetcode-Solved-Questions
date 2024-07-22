class Solution:
    def done(self, arr):
        _int = 0
        for a in arr:
            _int += type(a) == int
        return _int == 1

    def findTheWinner(self, n: int, k: int) -> int:

        array = [i for i in range(n)]
        i = 0 

        while not self.done(array):
            while type(array[i % n]) != int:
                i += 1
            count = 1
            while count < k:
                if type(array[i%n]) == bool:
                    i += 1
                    continue
                else:  
                    count += 1
                    i += 1
            while type(array[i % n]) != int:
                i += 1
            array[(i) % n] = False
            i += 1

        for ans in array:
            if ans:
                return ans + 1
        
        return 1