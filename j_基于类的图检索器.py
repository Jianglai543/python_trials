class Graph():
    def __init__(self, label, extra=None):
        self.name = label
        self.data = extra
        self.arc = []

    def __repr__(self):
        return self.name

    def search(self, goal):
        Graph.solns = []
        self.generate([self], goal)
        Graph.solns.sort(key = lambda x : len(x))
        return Graph.solns

    def generate(self, path, goal):
        if path[-1] == goal:
            Graph.solns.append(path)
        else:
            for arc in self.arc:
                if arc not in path:
                    self.generate(path + [arc], goal)

if __name__ == '__main__':
    # exec 不知道为什么不好用。
    """for name in 'ABCDEFG':
        print(name)
        exec("%s.Graph('%s')" % (name, name))"""

    A = Graph('A')
    B = Graph('B')
    C = Graph('C')
    D = Graph('D')
    E = Graph('E')
    F = Graph('F')
    A.arc = [B, C, F]
    B.arc = [C, F]
    C.arc = [B, E, F]
    print(A.search(B))


