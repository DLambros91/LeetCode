class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # Create a counter to keep hold of how many jewels were found
        self.count = 0
        
        # Iterate over the String of stones that you have
        for i in range(0, len(S)):
            # Iterate over the String of jewels
            for j in range(0, len(J)):
                # Compare case-sensitive characters 
                if S[i] == J[j]:
                    # Increment the counter
                    self.count += 1
                    # Break out of the inner for-loop when found to reduce unnecessary checks
                    break
        # Return the counter            
        return self.count
