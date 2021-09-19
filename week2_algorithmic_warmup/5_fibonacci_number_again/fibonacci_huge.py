#!/usr/bin/python3
import time

def get_fibonacci_huge(n, m):
    if n <= 1:
        return n
    # TODO
    return n


if __name__ == '__main__':
    n, m = map(int, input().split())
    start_time = time.time()
    print(get_fibonacci_huge(n, m))
    print(time.time() - start_time)
