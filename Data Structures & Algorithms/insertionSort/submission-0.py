# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
import copy
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        n = len(pairs)
        ans = []
        for i in range(n):
            j = i
            while j >= 1:
                if pairs[j].key >= pairs[j - 1].key:
                    break
                (pairs[j], pairs[j-1]) = (pairs[j-1], pairs[j])
                j -= 1
            snapshot = copy.copy(pairs)
            ans.append(snapshot)
        return ans