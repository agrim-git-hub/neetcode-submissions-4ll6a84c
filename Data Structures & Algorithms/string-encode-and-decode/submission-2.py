class Solution:

    def encode(self, strs: List[str]) -> str:
        #using list and then join as the time complexity is O(N)
        encoded_str = []
        for string in strs:
            encoded_str.append(f"{len(string)}#{string}")
        return "".join(encoded_str)


    def decode(self, s: str) -> List[str]:
        #Using pointer shifting method
        result, i = [], 0

        while i < len(s):

            j = i
            
            while s[j] != '#':
                j+=1
            
            length = int(s[i:j])

            result.append(s[j + 1 : j + 1 + length])
            i = j+1+length
        
        return result


