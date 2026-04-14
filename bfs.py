import graph


class BFS:
    def __init__(self, graph, source):
        self._graph = graph
        self._source = source
        self._edge_to = []
        self._marked = []
        for i in range(graph.vertex_count()):
            self._edge_to.append(None)
            self._marked.append(False)
        self._bfs(source)

    def _bfs(self, source):
        self._marked[source] = True
        queue = [source]
        while len(queue) > 0:
            v = queue.pop(0)
            for w in self._graph.adj(v):
                if not self._marked[w]:
                    queue.append(w)
                    self._marked[w] = True
                    self._edge_to[w] = v

    def has_path_to(self, v):
        return self._marked[v]

    def path_to(self, v):
        if not self.has_path_to(v):
            return None
        path = []
        x = v
        while x != self._source:
            path.append(x)
            x = self._edge_to[x]
        path.append(self._source)
        path.reverse()
        return path


if __name__ == "__main__":
    graph = graph.Graph()
    graph.add_edge(0, 5)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 6)
    graph.add_edge(6, 4)
    graph.add_edge(4, 3)
    graph.add_edge(4, 5)
    graph.add_edge(5, 3)

    print(graph)

    source = 0
    bfs = BFS(graph, source)
    for i in range(0, graph.vertex_count()):
        if bfs.has_path_to(i):
            print(bfs.path_to(i))
        else:
            print(f'{source} not connected with {i}')
