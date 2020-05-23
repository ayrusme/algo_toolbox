#!/usr/bin/python3

# A tail recursive function to
# calculate nth fibnacci number

def tail_recursivefib(limit, first=0, second=1):
    if limit == 0:
        return first
    if limit == 1:
        return second
    return tail_recursivefib(limit - 1, second, first + second)

n = int(input())

print(tail_recursivefib(n))
