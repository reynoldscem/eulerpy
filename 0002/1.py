from functools import reduce
from itertools import count
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def number_generator(max_num):
    for i in count(0):
        fib_val = fib(i)
        if fib_val >= max_num:
            break
        if fib_val % 2 == 0:
            yield fib_val

def main():
    answer = reduce(
        lambda x, y: x + y, number_generator(4 * (10**6))
    )
    print(answer)


if __name__ == '__main__':
    main()
