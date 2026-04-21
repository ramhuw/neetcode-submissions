class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = {}
        map2 = {}
        for l in s:
            map1[l] = map1.get(l, 0) + 1
        for l in t:
            map2[l] = map2.get(l, 0) + 1
        return map1 == map2