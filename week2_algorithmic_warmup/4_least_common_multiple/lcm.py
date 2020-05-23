#!/usr/bin/python3


def lcm(a, b):
    for l in range(1, a*b + 1):
        if l * a % b == 0:
            return l * a
    return a*b


if __name__ == '__main__':
    a, b = map(int, input().split())
    # print(lcm_naive(a, b))
    print(lcm(a, b))
