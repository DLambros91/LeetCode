class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = []
        
        while n != 0:
            digits.append(n%10)
            n = int((n - n%10)/10)
        
        sumOfDigits = 0
        
        for i in digits:
            sumOfDigits += i
        
        prodOfDigits = 1
        
        for i in digits:
            prodOfDigits *= i
            
        #print ("Sum :", sumOfDigits, "Prod:", prodOfDigits)    
        return prodOfDigits - sumOfDigits    
