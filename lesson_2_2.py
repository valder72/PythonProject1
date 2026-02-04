# ABBA

def polindrom(word):
    if len(word) <= 1:
        return True
    return word[0] == word[-1] and polindrom(word[1:-1])

if __name__ == '__main__':
    print(polindrom("ABBA"))
    print(polindrom("HELLO"))