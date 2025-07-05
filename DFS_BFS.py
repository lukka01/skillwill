from collections import deque


graph = {
    'A': ['B', 'C', 'D', 'E'],
    'B': ['A', 'F', 'G'],
    'C': ['A', 'K'],
    'D': ['A', 'M'],
    'E': ['A', 'L'],
    'F': ['B', 'H'],
    'G': ['B', 'I'],
    'H': ['F', 'J'],
    'I': ['G', 'j'],
    'J': ['H', 'J', 'Z'],
    'K': ['C', 'N', 'O'],
    'L': ['E', 'R'],
    'M': ['D', 'O'],
    'N': ['K', 'P'],
    'O': ['K', 'M', 'Q'],
    'P': ['N', 'Z'],
    'Q': ['O', 'Z'],
    'R': ['L', 'S','T'],
    'S': ['R'],
    'T': ['R'],
    'Z': ['J', 'P','Q']
}


def dfs(start, visited = None):
    if visited is None:
        visited = set()
    visited.add(start)
    result = [start]
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            result.extend(dfs(neighbor, visited))
    return result


def bfs(start):
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        vertex= queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            queue.extend([n for n in graph.get(vertex, []) if n not in visited])
    return result


print("DFS:", dfs('A'))
print("BFS:", bfs('A'))
