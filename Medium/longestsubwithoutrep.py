class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        largest = 0
        count = 0
        chars = { }
        
        for i in range(len(s)):
            if s[i] in chars:
                if count > largest: largest = count
                n = count
                for j in range (n):
                    if s[i-(n-j)] is not s[i]:
                        count -= 1
                        chars.pop(s[i-(n-j)])
                    else: break
                count -= 1
            chars[s[i]] = i
            count += 1
        
        return count if count > largest else largest
