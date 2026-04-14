"""
WARNING: this Graph implementation has an issue.
Find it to get extra scores
"""


class Graph:
    def __init__(self):
        self._vertex_count = 0
        self._edges_count = 0
        self._adj = []

    def vertex_count(self):
        return self._vertex_count

    def edges_count(self):
        return self._edges_count

    def add_edge(self, v: int, w: int):
        if len(self._adj) <= v or len(self._adj) <= w:
            self._extend(max(v, w))
        if w not in self._adj[v]:
            self._adj[v].append(w)
        if v not in self._adj[w]:
            self._adj[w].append(v)
        self._edges_count += 1

    def _extend(self, v: int):
        while len(self._adj) <= v:
            self._adj.append([])
        self._vertex_count = len(self._adj)

    def degree(self, v: int) -> int:
        """
        the degree (or valency) of a vertex of a graph is the number of
        edges that are incident to the vertex
        :param v: vertex index
        :return: vertex degree
        """
        if v >= len(self._adj):
            return -1
        return len(self._adj[v])

    def adj(self, v: int) -> list:
        """
        the list of incident edges
        :param v:
        :return:
        """
        return self._adj[v]

    def __str__(self):
        res = f'{str(self._vertex_count)} vertices, {str(self._edges_count)} edges \n'
        i = 0
        for v in self._adj:
            res += str(i) + ": "
            res += str(v)
            res += "\n"
            i += 1
        return res


if __name__ == "__main__":
    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 5)
    graph.add_edge(0, 6)
    graph.add_edge(3, 4)
    graph.add_edge(3, 5)
    graph.add_edge(3, 5)
    graph.add_edge(4, 5)
    graph.add_edge(4, 6)
    graph.add_edge(7, 8)
    graph.add_edge(9, 10)
    graph.add_edge(9, 11)
    graph.add_edge(9, 12)
    graph.add_edge(11, 12)

    print(f'degree 0: {graph.degree(0)}')
    print(graph)
    print(graph._edges_count)


