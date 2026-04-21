class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for word in strs:
            small_map = [0]*26
            for letter in word:
                small_map[ord(letter) - ord('a')] += 1
            small_map = tuple(small_map)
            map[small_map] = map.get(small_map, list())
            map[small_map].append(word)
        return list(map.values())