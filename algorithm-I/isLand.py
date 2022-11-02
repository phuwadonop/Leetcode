def max_area_of_island(grid) :
    result = 0
    for row in range(len(grid)) :
        for col in range(len(grid[0])) :
            if grid[row][col] == 0 : continue
            if grid[row][col] == 1 : result = max(result,fill(grid,row,col))
    return result
            
def fill(grid,row,col) :
    deltas = [(1,0),(-1,0),(0,1),(0,-1)]
    
    def dfsFill(row,col) :
        row_boundary = 0 <= row < len(grid)
        col_boundary = 0 <= col < len(grid[0])
        if not row_boundary or not col_boundary or grid[row][col] != 1 or grid[row][col] == 0 : return 0
        grid[row][col] = 0
        ans = 1
        for delta_row , delta_col in deltas :
            ans += dfsFill(row + delta_row,col + delta_col)
        return ans
    return dfsFill(row,col)

def maxAreaOfIsland(grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        DIR = [0, 1, 0, -1, 0]

        def dfs(r, c):
            if r < 0 or r == m or c < 0 or c == n or grid[r][c] == 0: 
                return 0
            ans = 1
            grid[r][c] = 0  # Mark this square as visited
            for i in range(4):
                ans += dfs(r + DIR[i], c + DIR[i + 1])
            return ans

        ans = 0
        for r in range(m):
            for c in range(n):
                ans = max(ans, dfs(r, c))
        return ans

grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
for i in grid : print(i)
print(max_area_of_island(grid))
for i in grid : print(i)