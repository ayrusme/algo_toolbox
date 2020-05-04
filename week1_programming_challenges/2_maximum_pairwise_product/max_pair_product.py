# python3


def max_pairwise_product(numbers):
    # find largest element
    first = max(numbers)
    numbers.remove(first)
    return first * max(numbers)


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
