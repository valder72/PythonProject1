import math
from random import randint


class Percolation:
    def __init__(self, number: int):
        """
        create NxN matrix with all closed cells
        :param number: <int> number of rows and columns
        """
        self._count = number ** 2
        self._top = self._count
        self._bottom = self._count + 1

        self._matrix = [None for _ in range(self._count + 2)]
        self._matrix[self._top] = self._top
        self._matrix[self._bottom] = self._bottom

        self._size = [1 for _ in range(self._count + 2)]
        self._opened = 0

    def get_opened_count(self) -> int:
        """
        opened cells count
        :return: <int> opened cells count
        """
        return self._opened

    def _union(self, p: int, q: int):
        p_root = self._find(p)
        q_root = self._find(q)

        if p_root == q_root:
            return

        if self._size[p_root] < self._size[q_root]:
            self._matrix[p_root] = q_root
            self._size[q_root] += self._size[p_root]
        else:
            self._matrix[q_root] = p_root
            self._size[p_root] += self._size[q_root]

    def _find(self, p: int) -> int:
        while p != self._matrix[p]:
            p = self._matrix[p]
        return p

    def open(self):
        """
        open random cell if it is not opened yet
        """
        random_n = randint(0, self._count - 1)
        n_size = int(self._count ** 0.5)

        if self._matrix[random_n] is None:
            self._matrix[random_n] = random_n

            if random_n < n_size:
                self._union(random_n, self._top)

            if random_n >= self._count - n_size:
                self._union(random_n, self._bottom)

            if (random_n % n_size != n_size - 1
                    and self._matrix[random_n + 1] is not None):
                self._union(random_n, random_n + 1)

            if (random_n % n_size != 0
                    and self._matrix[random_n - 1] is not None):
                self._union(random_n, random_n - 1)

            if (random_n - n_size >= 0
                    and self._matrix[random_n - n_size] is not None):
                self._union(random_n, random_n - n_size)

            if (random_n + n_size < self._count
                    and self._matrix[random_n + n_size] is not None):
                self._union(random_n, random_n + n_size)

            self._opened += 1

    def is_opened(self, i: int, j: int) -> bool:
        """
        check if cell is opened yet
        :param i: <int> row index
        :param j: <int> column index
        :return: <bool> is cell opened
        """
        n_size = int(self._count ** 0.5)
        if 0 <= i < n_size and 0 <= j < n_size:
            return self._matrix[i * n_size + j] is not None
        return False

    def percolates(self) -> bool:
        """
        check if system percolates
        :return: <bool> percolates
        """
        return self._find(self._top) == self._find(self._bottom)


class PercolationExperiment:
    def __init__(self, n: int, t: int):
        """
        run T separate experiments with NxN matrix
        :param n: <int> number of rows and columns in matrix
        :param t: <int> number of experiments
        """
        self._t = t
        self._fractions = []

        for _ in range(t):
            p = Percolation(n)
            while not p.percolates():
                p.open()
            self._fractions.append(p.get_opened_count() / (n ** 2))

    def mean(self) -> float:
        return sum(self._fractions) / self._t

    def std(self) -> float:
        if self._t <= 1:
            return 0.0
        m = self.mean()
        variance = sum((x - m) ** 2 for x in self._fractions) / (self._t - 1)
        return math.sqrt(variance)

    def confidence_interval(self) -> tuple[float, float]:
        m = self.mean()
        s = self.std()
        margin = 1.96 * s / math.sqrt(self._t)
        return m - margin, m + margin


def main():
    """
    run experiments and compute mean, std, confidence interval.
    print results on screen in readable format.
    """
    n = 200
    t = 100

    print(f"{n} {t}")
    experiment = PercolationExperiment(n, t)

    mean_val = experiment.mean()
    std_val = experiment.std()
    interval = experiment.confidence_interval()

    print(f"mean = {mean_val}")
    print(f"std = {std_val}")
    print(f"95% confidence interval = {interval[0]}, {interval[1]}")


if __name__ == "__main__":
    main()