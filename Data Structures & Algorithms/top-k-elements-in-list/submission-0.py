class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        buck = [set(nums)] + [set() for _ in range(n)]
        map = {}
        for num in nums:
            map[num] = map.get(num, 0)
            buck[map[num]].remove(num)
            map[num] += 1
            buck[map[num]].add(num)
        ans = []
        fr = n
        while len(ans) < k:
            ans += list(buck[fr])
            fr -= 1
        return ans