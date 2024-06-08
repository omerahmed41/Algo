'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
'''
import collections


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        if not grid: 
            return island
        rows, cols = len(grid), len(grid[0])
        visited = set()
        
        def get_diractions(r,c):
            return [(r + 1, c), (r -1, c), (r, c + 1), (r, c-1)]
        def is_valid(r,c):
            return r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r, c) not in visited

        def bfs(r, c):
            visited.add((r, c))
            q = collections.deque([(r, c)])

            while q:
                r, c = q.popleft()
                for dr, dc in get_diractions(r, c):
                    if is_valid(dr, dc):
                        q.append((dr, dc))
                        visited.add((dr, dc))
                        
        for r in range(rows):
            for c in range(cols):
                if is_valid(r, c):
                    print(grid[r][c])
                    bfs(r, c)
                    island += 1
        return island
        
        