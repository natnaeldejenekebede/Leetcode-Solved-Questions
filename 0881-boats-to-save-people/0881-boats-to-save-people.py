class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()

        left_ptr, right_ptr = 0, len(people) - 1
        boats = 0
        while left_ptr <= right_ptr:
            if people[left_ptr] + people[right_ptr] <= limit:
                left_ptr += 1 
            right_ptr -= 1 
            boats += 1  
        return boats
