def find_paths(dictt, start, final_point, way):
    way = way + [start]
    ways = []
    if start == final_point:
        return [way]
    if not dictt.get(start):
        return []
    for neighbor in dictt[start]:
        new_paths = find_paths(dictt, neighbor, final_point, way)
        ways.extend(new_paths)
    return ways


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
start = 'A'
end = 'F'
path = []

paths = find_paths(graph, start, end, path)
print("Все пути из точки A в точку F: ", *paths)
