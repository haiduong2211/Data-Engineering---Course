import sys

def number_of_components(adj):
    result = 0
    #write your code here
    visited = [0] * len(adj) #Tạo visited check list
    for i in range(len(adj)): #Check những điểm liền kề từ vị trí i
        if not visited[i]: #Nếu i chưa visited thì !explore vị trí này
            explore(adj, i, visited) #explore các node từ vị trí i xem có connected không 
            result += 1 
    return result

def explore(adj, x, visited): #Explore các node từ vị trí x 
    visited[x] = 1 #visited check
    for i in range(len(adj[x])):
        if not visited[adj[x][i]]:
            explore(adj, adj[x][i], visited) #Tiếp tục explore (Nếu visited sẽ dừng!)

if __name__ == '__main__':
    input = input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2])) #Tạo tuple trong list edges = [(2.1),(3,1)]
    adj = [[] for _ in range(n)] #Tạo list adj vertexes
    for (a, b) in edges: #(1,2) - (3,2)
        adj[a - 1].append(b - 1) #Quy đổi từ số cạnh ra index nên trừ 1
        adj[b - 1].append(a - 1)

    print(number_of_components(adj))    