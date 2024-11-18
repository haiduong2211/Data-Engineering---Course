import sys
import queue
import collections

class graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

def bipartite(adj): # [[3], [4, 3], [3], [1, 2, 0], [1]]
    visited = [False] * len(adj)
    visited[0] = True

    chart = [-1]*len(adj)
    chart[0] = 0

    queue = []
    queue.append(0)

    while queue: #BFS
        v = queue.pop(0)
        for u in adj[v]: #Trong ds liền kề của v (0) 
            if chart[u] == chart[v]: #Nếu giá trị so sánh = nhau thì là không bipartite
                return 0
            else:
                if not visited[u]: #Nếu chưa visit (not False = True)
                    visited[u] = True
                    chart[u] = 1 - chart[v]
                    queue.append(u)
    return 1 


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))