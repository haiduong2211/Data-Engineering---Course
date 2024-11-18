# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = 5
                self.parent = [4,-1,4,1,1]

        def compute_height(self):
                # Replace this code with a faster implementation
                #maxHeight = 0
                '''
                for vertex in range(self.n):
                        height = 0
                        i = vertex
                        while i != -1:
                                height += 1
                                i = self.parent[i]
                        maxHeight = max(maxHeight, height)
                return maxHeight'''
        def compute(self):
                height = [None for _ in self.parent]
                todo = list(range(self.n))
                while 0 < len(todo):
                        node = todo.pop()
                        if self.parent[node] == -1:
                                height[node] = 1
                        elif height[node] is None:
                                if height[self.parent[node]] is None:
                                        todo.append(node)
                                        todo.append(self.parent[node])
                                else:
                                        height[node] = height[self.parent[node]] +1
                        print(height, todo)
                return max(height)

def main():
    tree = TreeHeight()
    tree.read()
    print(tree.compute())

threading.Thread(target=main).start()
