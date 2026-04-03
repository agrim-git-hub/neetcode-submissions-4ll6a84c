class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #to check if a string is anagram, we can map each character of the string to its count using hashmap. we make 2 different hashmaps for the 2 different strings, then we compare both hashmaps and return boolean
        if len(s)==len(t):
            hash1 ={}
            hash2 = {}
            for i in range(len(s)):
                hash1[s[i]] = hash1.get(s[i],0)+1
                hash2[t[i]] = hash2.get(t[i],0)+1
            
            return (hash1 == hash2)
        else:
            return False