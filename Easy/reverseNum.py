class Solution:
    def reverse(self, x: int) -> int:
        reversedNum = 0
        
        neg = x < 0
    
        if neg:
            x *= -1
        while x > 0:
            reversedNum += x%10 * (10**(len(str(x))-1))
            x = int(x/10)
        if neg:
            reversedNum*=-1
        if reversedNum >= 2**31 or reversedNum <= -2**31:
            return 0
        return reversedNum
