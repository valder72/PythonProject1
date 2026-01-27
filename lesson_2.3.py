def sum_squares(l):
    total = 0
    for item in l:
        if isinstance(item, list):
            total += sum_squares(item)
        else:
            total += item ** 2
    return total

if __name__ == "__main__":
    print(sum_squares([1, [2, [3]]]))