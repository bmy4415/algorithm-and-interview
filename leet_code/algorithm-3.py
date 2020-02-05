class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # empty string
        if not s:
            return 0
        
        dic = {}    # key: char, value: last index
        max_start, max_end = 0, 0
        
        start = 0
        for end, char in enumerate(s):
            if char in dic:
                start = max(dic[char] + 1, start)
                
            # compare length and update if needed
            if (end - start) > (max_end - max_start):
                max_start, max_end = start, end
                
            dic[char] = end
            
        return max_end - max_start + 1
