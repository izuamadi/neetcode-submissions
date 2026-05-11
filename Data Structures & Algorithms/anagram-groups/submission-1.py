class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        strs = ["act","pots","tops","cat","stop","hat"]
        groups = {
        act: [act, cat]
        pots: [pots,tops, stop]
        hat: [hat]
        }
        """
        groups = {}
        output = []

        for word in strs:
            if "".join(sorted(word)) in groups:
                groups["".join(sorted(word))].append(word)
            else:
                groups["".join(sorted(word))] = [word]
        
        for i in groups.values():
            output.append(i)
        
        return output


     