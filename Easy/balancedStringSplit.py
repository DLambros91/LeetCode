class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        balance = 0
        for i in s:
            # Ternary operator slower in python
            #balance += 1 if i == 'R' else -1
            if i =='R':
                balance +=1
            else: 
                balance -=1
                
            if balance == 0:
                count += 1 
        return count
