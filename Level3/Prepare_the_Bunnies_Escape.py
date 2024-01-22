# coding: utf-8

from collections import deque

def solution(map):

    height = len(map)
    width = len(map[0])

    def bfs(map, start, remove_wall):

        queue = deque([(start, 0, remove_wall)])
        visited = set([(start, remove_wall)])

        while queue:
            (x, y), steps, can_remove = queue.popleft()

            if (x, y) == (height - 1, width - 1):
                return steps + 1

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < height and 0 <= ny < width:
                    if map[nx][ny] == 1 and can_remove and ((nx, ny), False) not in visited:
                        visited.add(((nx, ny), False))
                        queue.append(((nx, ny), steps + 1, False))
                    elif map[nx][ny] == 0 and ((nx, ny), can_remove) not in visited:
                        visited.add(((nx, ny), can_remove))
                        queue.append(((nx, ny), steps + 1, can_remove))

        return -1 # float('inf') 

    return bfs(map, (0, 0), True)

lab1 = [
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0]
]

lab2 = [
    [0, 1, 1, 0],
    [0, 0, 0, 1],
    [1, 1, 0, 0],
    [1, 1, 1, 0]
]

print(solution(lab1))
print(solution(lab2))
