# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
# """
#class GridMaster(object):
#    def canMove(self, direction: str) -> bool:
#        
#
#    def move(self, direction: str) -> bool:
#        
#
#    def isTarget(self) -> None:
#        
#

class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        
        dirs = {'U':(-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
        anti = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}
        
        isValid = {}
        isValid[(0, 0)] = master.isTarget()
        
        def dfs(r, c):
            for d in dirs:
                dr, dc = dirs[d]
                nr, nc = r+dr, c+dc
                if (nr, nc) not in isValid and master.canMove(d):
                    master.move(d)
                    isValid[(nr, nc)] = master.isTarget()
                    dfs(nr, nc)
                    master.move(anti[d])
        dfs(0, 0)
        qu = collections.deque([(0, 0, 0)])
        seen = set()
        while qu:
            r, c, step = qu.popleft()
            if isValid[(r, c)] == True:
                return step
            for nr, nc in [[r+1, c], [r-1, c], [r, c-1], [r, c+1]]:
                if (nr, nc) in isValid and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    qu.append((nr, nc, step+1))
        return -1
