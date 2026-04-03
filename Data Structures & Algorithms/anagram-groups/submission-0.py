class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #we can make a dictionary, whose keys will be the sorted string and its value is the list of strings which will result in the key if they get sorted
        sample_hash={}
        for string in strs:
            x = "".join(sorted(string))
            if x in sample_hash:
                sample_hash[x].append(string)
            else:
                sample_hash[x] = [string]

        return list(sample_hash.values())