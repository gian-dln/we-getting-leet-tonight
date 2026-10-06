class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # pre[0] = 1 pre[1] = 0, false
        # pre[1] = 0 // course, prerequisite
        # pre[0] = 1 0 -> 1
        # pre[1] = 0 1 -> 0
        
        map = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            map[course].append(pre)

        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if map[course] == []:
                return True

            visited.add(course)

            for p in map[course]:
                if not dfs(p):
                    return False
            visited.remove(course)
            map[course] = []

            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True


        




        