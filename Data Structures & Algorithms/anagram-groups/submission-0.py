class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        strs = ["act","pots","tops","cat","stop","hat"]

        act: act
        pots: pots, tops, stop
        hat: hat

        """
        hashmap = {}
        hashmap_values = []

        for word in strs:
            if "".join(sorted(word)) in hashmap:
                hashmap["".join(sorted(word))].append(word)
            else:
                hashmap["".join(sorted(word))] = [word]
        
        for j in hashmap.values():
            hashmap_values.append(j)
        
        return hashmap_values
        
                 

       


        