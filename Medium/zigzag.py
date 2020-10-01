class Solution:
    def convert(self, s: str, numRows: int) -> str: 
        newS = ""
        
        if numRows == 1:
            return s
        
        for row in range(1, numRows+1):
            i = row-1

            if i != 0 and i != numRows-1:
                j = 0
                while i < len(s):
                    newS += s[i]
                    if j%2 == 0:
                        i += 2*(numRows-row)
                    else:
                        i += 2*(row-1)
                    j += 1
            else:
                while i < len(s):
                    newS += s[i]
                    i += 2*(numRows-1)
                    
        return newS
                    
