import graph


class CC:
    def __init__(self, graph):
        self._marked = []
        self._id = []
        self._count = 0
        self._graph = graph
        for i in range(0, graph.vertex_count()):
            self._id.append(i)
            self._marked.append(False)

        for i in range(0, graph.vertex_count()):
            if not self._marked[i]:
                self._dfs(i)
                self._count += 1

    def _dfs(self, v):
        self._marked[v] = True
        self._id[v] = self._count
        for w in self._graph.adj(v):
            if not self._marked[w]:
                self._dfs(w)

    def count(self):
        return self._count

    def component_id(self, v):
        return self._id[v]


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

    graph.add_edge(7, 8)

    graph.add_edge(9, 10)
    graph.add_edge(9, 12)
    graph.add_edge(9, 11)
    graph.add_edge(11, 12)
    print(graph)

    source = 0
    cc = CC(graph)
    print(f'Count of components: {cc.count()}')
    for i in range(0, graph.vertex_count()):
        print(f'Vertex {i} is in {cc.component_id(i)} component')

