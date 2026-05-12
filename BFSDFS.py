# def dfs(g, s):
#     stack = [s]
#     vis = []

#     while stack:
#         node = stack.pop()   # LIFO
#         if node not in vis:
#             print(node, end=" ")
#             vis.append(node)

            
#             for c in reversed(g[node]):
#                 if c not in vis:
#                     stack.append(c)



def dfs(g,s,vis): 
    vis.append(s) 
    print(s,end=" ") 
    for c in g[s]: 
        if c not in vis: 
            dfs(g,c,vis)

def bfs(g,s):
    q=[s]
    vis=[s]
    while q:
        cur=q.pop(0)
        print(cur,end=" ")
        for c in g[cur]:
            if c not in vis:
                q.append(c)
                vis.append(c)

n=int(input("Enter number of cities(vertices): "))
cities=[]

print("Enter city names:")
for _ in range(n):
    cities.append(input())

g={city:[] for city in cities}

e=int(input("Enter number of connections(edges): "))

print("Enter connections (city1 city2 ): ")

for _ in range(e):
    c1,c2=input().split()
    g[c1].append(c2)
    g[c2].append(c1)

start=input("Enter starting city: ")

print("BFS traversal: ")
vis=[]
bfs(g,start)

print("\nDFS traversal: ")
dfs(g,start)