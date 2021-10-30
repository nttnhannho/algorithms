import time
import sys


def fib_recursion(n):
    if n < 0:
        raise ValueError

    return 0 if n == 0 else (1 if n in (1, 2) else fib_recursion(n - 1) + fib_recursion(n - 2))


def fib_dp(n):
    cache = [0, 1, 1]
    for i in range(3, n + 1):
        cache.append(cache[i - 1] + cache[i - 2])
    return cache[n]


def fib_dp_memoization(n):
    cache = {
        0: 1,
        1: 1,
        2: 1
    }
    def fib_memo(n, cache):
        if n in cache:
            return cache[n]
        res = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)
        cache[n] = res
        return res
    return fib_memo(n, cache)


def fib_while_loop(n):
    if n < 0:
        raise ValueError

    first = 0
    second = 1
    while n > 0:
        second, first = second + first, second
        n -= 1
    return first


if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    number = 2169

    # print("Recursion:")
    # start1 = time.time()
    # print(fib_recursion(30))
    # print(time.time() - start1)

    print("While loop:")
    start2 = time.time()
    print(fib_while_loop(number))
    end2 = time.time()
    print(end2 - start2)

    print("DP:")
    start3 = time.time()
    print(fib_dp(number))
    end3 = time.time()
    print(end3 - start3)

    print("Memoization:")
    start4 = time.time()
    print(fib_dp_memoization(number))  # Crashed at n = 2169
    end4 = time.time()
    print(end4 - start4)
