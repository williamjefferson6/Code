class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        anagram_dict = defaultdict(list)

        for s in strs:
            char_count = [0] * 26
            for char in s:
                char_count[ord(char) - ord('a')] += 1
            key = tuple(char_count)
            anagram_dict[key].append(s)
        for group in anagram_dict.values():
            result.append(group)
        return result