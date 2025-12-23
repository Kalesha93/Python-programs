import heapq

def best_first_search(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    
    def heuristic(a, b):
        # Using Manhattan distance as heuristic
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
    visited = set()
    queue = []
    heapq.heappush(queue, (heuristic(start, goal), start))
    path = {start: None}
    
    while queue:
        _, current = heapq.heappop(queue)
        if current == goal:
            # Reconstruct path
            p = []
            while current:
                p.append(current)
                current = path[current]
            return p[::-1]
        
        visited.add(current)
        
        # Explore neighbors (up, down, left, right)
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = current[0]+dx, current[1]+dy
            neighbor = (nx, ny)
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0 and neighbor not in visited:
                heapq.heappush(queue, (heuristic(neighbor, goal), neighbor))
                if neighbor not in path:
                    path[neighbor] = current
    return None

# 0 = free cell, 1 = obstacle
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0]
]

start = (0, 0)
goal = (3, 4)

path = best_first_search(grid, start, goal)
print("Path found:", path)
