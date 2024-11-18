import sys
MAX_VAL = 1000
def belman_ford(s, adj, cost):
    arr_len = len(adj)
    dist_arr = [MAX_VAL]*arr_len
    prev_arr = [None]*arr_len
    dist_arr[s] = 0

    for u in range(arr_len):
        for i, v in enumerate(adj[u]):
            if dist_arr[v] == MAX_VAL:
                break
            if dist_arr[v] > dist_arr[u] + cost[u][i]:
                dist_arr[v] = dist_arr[u] + cost[u][i]
                prev_arr[v] = u


    #detect negative cycle
    for u in range(arr_len):
        for i, v in enumerate(adj[u]):
            if dist_arr[v] == MAX_VAL:
                break
            if dist_arr[v] < dist_arr[u] + cost[u][i]:
                return 1

    return 0


def negative_cycle(adj, cost):
    #write your code here
    return belman_ford(0,adj, cost)

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
    print(negative_cycle(adj, cost))