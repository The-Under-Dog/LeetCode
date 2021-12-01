class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        
        sum = 0
        max_digit = 1        
        
        
        for i in range(len(s)-1, -1, -1):
            
            if  dict[s[i]] >= max_digit:
                max_digit = dict[s[i]]
                sum += dict[s[i]]
                
            else:
                sum -= dict[s[i]]
                
        return sum
