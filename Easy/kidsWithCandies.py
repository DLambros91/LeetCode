class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Find the max value of candies
        maxval = candies[0]
        
        for i in range(1, len(candies)):
            if maxval < candies[i]:
                maxval = candies[i]
        
        # List of possible not possible
        possible = [ ]
        
        for i in candies:
            possible.append(True) if i + extraCandies >= maxval else possible.append(False)
            
        return possible
