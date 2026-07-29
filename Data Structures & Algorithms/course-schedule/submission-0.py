class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = [[] for _ in range(numCourses)]
        for p in prerequisites:
            d[p[0]].append(p[1])
        mark = [False for _ in range(numCourses)]
        searches = [i for i in range(numCourses)]
        while searches:
            search = searches.pop()
            visits = [search]
            visited = set()
            while visits:
                visit = visits.pop()
                if visit in visited:
                    return False
                if mark[visit]:
                    continue
                visited.add(visit)
                mark[visit] = True

                visits = visits + d[visit]
        return True