class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        L = 0
        R = len(people) - 1
        boats = 0

        while L <= R:
            # If the lightest and heaviest can share, move the left pointer
            if L != R and people[L] + people[R] <= limit:
                L += 1
            
            # The heavy person always leaves on this boat
            R -= 1
            boats += 1

        return boats