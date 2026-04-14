TOP = "top"
BOTTOM = "bottom"
class Percolation:
    def __init__(self, number: int):
        """
        create NxN matrix with all closed cells
        :param number: <int> number of rows and columns
        """
        self._matrix = [i for i in range(number ** 2)]
        self._size = [1 for i in range(number ** 2)]
        self._count = number ** 2
        self._matrix[ : number] = [TOP] * number
        self._matrix[-number : ] = [BOTTOM] * number

    def opened_count(self) -> int:
        """
        opened cells count
        :return: <int> opened cells count
        """
        

    def open(self):
        """
        open random cell if it is not opened yet
        """
        ...

    def is_opened(self, i: int, j: int) -> bool:
        """
        check if cell is opened yet
        :param i: <int> row index
        :param j: <int> column index
        :return: <bool> is cell opened
        """

    def percolates(self) -> bool:
        """
        check if system percolates
        :return: <bool> percolates
        """
