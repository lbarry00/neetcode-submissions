class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return []

        group_map = {}
        result = []
        for s in strs:
            sorted_text = "".join(sorted(s))
            anagrams = group_map.setdefault(sorted_text, [])
            anagrams.append(s)
            group_map[sorted_text] = anagrams

        for key in group_map:
            result.append(group_map[key])

        return result
