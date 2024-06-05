import random


def destined_tea():
    """it will choose your tea"""
    tea = random.choice(['black', 'green'])
    return tea


def main():
    print("Slowpoker")
    print(destined_tea())


if __name__ == "__main__":
    main()
