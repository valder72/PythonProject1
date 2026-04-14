def check_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        if matrix[i] != [column[i] for column in matrix]:
            return "NO"
        if matrix[i][i] != 0:
            return "NO"
    return "YES"


def test_check_matrix():
    assert check_matrix([[0, 1], [1, 0]]) == "YES"
    assert check_matrix([[1, 1], [1, 1]]) == "NO"
    assert check_matrix([[0, 1], [0, 0]]) == "NO"
    assert check_matrix([[0]]) == "YES"
    assert check_matrix([[1]]) == "NO"

    assert check_matrix([
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0]
    ]) == "YES"

    assert check_matrix([
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ]) == "NO"

    assert check_matrix([
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 0]
    ]) == "YES"

    assert check_matrix([
        [0, 1, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 1, 0]
    ]) == "YES"

    assert check_matrix([
        [0, 1, 1, 1],
        [1, 0, 1, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 0]
    ]) == "YES"

    assert check_matrix([
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]) == "YES"

    assert check_matrix([
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
        [1, 0, 0, 0]
    ]) == "NO"

    assert check_matrix([
        [1, 1, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [0, 0, 1, 0]
    ]) == "NO"


if __name__ == "__main__":
    test_check_matrix()
