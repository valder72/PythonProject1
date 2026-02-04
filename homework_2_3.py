def replicate(times, number):
    if times <= 0:
        return []

    return [number] + replicate(times - 1, number)

if __name__ == "__main__":
    print(replicate(5, 1))
    print(replicate(-2, 10))