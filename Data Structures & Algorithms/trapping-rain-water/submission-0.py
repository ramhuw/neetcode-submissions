class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        h = max(height)
        rocks = []
        water = []
        v = 0
        for rock in height:
            rocks.append([True if y <= rock else False for y in range(h+1)])
            water.append([False if y <= rock else True for y in range(h+1)])
            v += h - rock
        for i in range(n):
            if height[i] == h:
                break
            for j in reversed(range(h+1)):
                if rocks[i][j]:
                    break
                if i == 0 or not (water[i - 1][j] or rocks[i - 1][j]):
                    water[i][j] = False
                    v -= 1
        for i in reversed(range(n)):
            if height[i] == h:
                break
            for j in reversed(range(h+1)):
                if rocks[i][j]:
                    break
                if i == n - 1 or not (water[i + 1][j] or rocks[i + 1][j]):
                    water[i][j] = False
                    v -= 1
        return v
        
        