class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:       
        n_count = collections.Counter(str(n))
        power = 1
        while len(str(power)) <= len(str(n)):
            if collections.Counter(str(power)) == n_count:
                return True
            power *= 2
        
        return False

