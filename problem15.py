def number_of_routes(n):
    grid = [[1 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            grid[i][j] = grid[i-1][j] + grid[i][j-1]
    return grid[n][n]


print(number_of_routes(2)) # expect 137846528820
