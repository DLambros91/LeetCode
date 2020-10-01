class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        # Determine if the length is 1
        if len(nums) == 1:
            return True
        
        # Count of how much needs to be changed
        count = 0
        
        for i in range(1, len(nums)):
            if count >= 2: 
                break
            if nums[i-1] > nums[i]:
                count += 1
                if i < 2 or nums[i-2] <= nums[i]:
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]
                
        return count < 2
