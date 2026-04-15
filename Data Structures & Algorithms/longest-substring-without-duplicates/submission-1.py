class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        duplicate_map = set()
        l = 0
        max_length = 0

        for r in range(len(s)):

            while s[r] in duplicate_map:

                duplicate_map.remove(s[l])
                l+= 1
            
            duplicate_map.add(s[r])

            length = r- l + 1
            if length > max_length:
                max_length = length

        return max_length