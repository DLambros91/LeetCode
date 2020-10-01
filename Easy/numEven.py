class Solution:
    def numEven(self, num: int) -> int:
        return len(str(num))%2
    
    def findNumbers(self, nums: List[int]) -> int:
        length = [self.numEven(i) for i in nums]
        return len(nums) - sum(length)
        
