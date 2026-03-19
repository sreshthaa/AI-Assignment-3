import heapq

n = 10
grid = [[0]*n for _ in range(n)]


grid[3][3] = 1
grid[3][4] = 1
grid[3][5] = 1

start = (0, 0)
goal = (9, 9)

def h(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def find_path(grid, start, goal):
    heap = [(0, start)]
    cost = {start: 0}
    parent = {start: None}

    moves = [(1,0), (-1,0), (0,1), (0,-1)]

    while heap:
        _, curr = heapq.heappop(heap)

        if curr == goal:
            break

        for m in moves:
            nxt = (curr[0]+m[0], curr[1]+m[1])

            if 0 <= nxt[0] < n and 0 <= nxt[1] < n:
                if grid[nxt[0]][nxt[1]] == 1:
                    continue

                new_cost = cost[curr] + 1

                if nxt not in cost or new_cost < cost[nxt]:
                    cost[nxt] = new_cost
                    priority = new_cost + h(nxt, goal)
                    heapq.heappush(heap, (priority, nxt))
                    parent[nxt] = curr


    path = []
    cur = goal
    while cur:
        path.append(cur)
        cur = parent.get(cur)

    return path[::-1]

path = find_path(grid, start, goal)
print("Path:", path)
