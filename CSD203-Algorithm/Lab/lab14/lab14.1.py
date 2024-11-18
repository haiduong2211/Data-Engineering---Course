#Uses python3

import sys


def distance(adj, cost, s, t):
    dist = [float('inf')]*n
    dist[s] = 0
    stack =[]
    
    for i in range(n):
        stack.append([dist[i],i]) #append giá trị là khoảng cách đến i và vị trí i
    while stack:
        stack.sort(reverse=True)
        u = stack.pop()
        v = u[1]
        length = len(adj[v])
        for l in range(length):
            vv  = adj[v][l]
            c = cost[v][l]
            if dist[vv] > dist[v] + c:
                stack.remove([dist[vv],vv])
                dist[vv] = dist[v] +c
                stack.append([dist[vv],vv])

    return dist[t] if dist[t] != float('inf') else -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))