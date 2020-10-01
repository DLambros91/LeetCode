class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        arr = []
        freq = []
        val = []
        for i in range (0, int(len(nums)/2)):
            freq.append(nums[2*i])
            val.append(nums[2*i+1])
            
            #for i in range (0,freq):
             #   arr.append(val)
        k = 0
        for x in freq:
            for i in range (0, x):
                arr.append(val[k])
            k += 1    
        return arr        
