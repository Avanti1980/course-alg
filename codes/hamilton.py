def hamilton(vertex):
    if vertex == start and len(cycle) == len(g) + 1:  # 找到回路
        print(cycle)
        return

    for v in g[vertex]:
        if not visited[v]:
            visited[v] = True
            cycle.append(v)
            hamilton(v)
            visited[v] = False
            cycle.pop()


g = {                           # a-----b
    "a": ["b", "c", "d"],       # |\   / 
    "b": ["a", "c"],            # | \ /   
    "c": ["a", "b", "d", "e"],  # |  c     
    "d": ["a", "c", "e"],       # | / \   
    "e": ["c", "d"],            # |/   \ 
}                               # d-----e
visited = {v: False for v in g}
start = "a"
cycle = [start]
hamilton(start)
#-------------------------------
# ['a', 'b', 'c', 'e', 'd', 'a']
# ['a', 'd', 'e', 'c', 'b', 'a']

g = {                           # a-----b
    "a": ["b", "c", "d"],       # |\   / \
    "b": ["a", "c", "f"],       # | \ /   \
    "c": ["a", "b", "d", "e"],  # |  c     f
    "d": ["a", "c", "e"],       # | / \   /
    "e": ["c", "d", "f"],       # |/   \ /
    "f": ["b", "e"],            # d-----e
}
visited = {v: False for v in g}
start = "f"
cycle = [start]
hamilton(start)
#------------------------------------
# ['c', 'a', 'b', 'f', 'e', 'd', 'c']
# ['c', 'a', 'd', 'e', 'f', 'b', 'c']
# ['c', 'b', 'f', 'e', 'd', 'a', 'c']
# ['c', 'd', 'a', 'b', 'f', 'e', 'c']
# ['c', 'd', 'e', 'f', 'b', 'a', 'c']
# ['c', 'e', 'f', 'b', 'a', 'd', 'c']
