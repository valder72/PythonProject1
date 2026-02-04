def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

if __name__ == "__main__":
    print(gcd(30, 12))
    print(gcd(8, 9))