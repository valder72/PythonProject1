class PercolationExperiment:
    def __init__(self, n: int, t: int):
        """
        run T separate experiments with NxN matrix
        :param n: <int> number of rows and columns in matrix
        :param t: <int> number of experiments
        """
        ...

    def mean(self) -> float:
        ...

    def std(self) -> float:
        ...

    def confidence_interval(self) -> (float, float):
        ...


def main():
    """
    run experiments and compute mean, std, confidence interval.
    print results on screen in readable format.
    """
    ...


if __name__ == "__main__":
    main()
