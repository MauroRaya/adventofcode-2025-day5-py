import time
from typing import Callable, Any


def time_it(func: Callable, *args, **kwargs) -> Any:
    start: float = time.perf_counter()
    result: Any = func(*args, **kwargs)
    end: float = time.perf_counter()

    print(f"Tempo decorrido: {end - start:.6f}s")
    return result


def binary_search(start: int, end: int, target: int) -> int:
    l: int = start
    r: int = end

    while l <= r:
        m: int = (l + r) // 2

        if target > m:
            l = m + 1
        elif target < m:
            r = m - 1
        else:
            return m

    return -1


def standard_iteration(start: int, end: int, target: int) -> int:
    for i in range(start, end + 1):
        if target == i:
            return i
        
    return -1


def count_available_fresh_ingridient_ids(
    search_func: Callable[[int, int, int], int]
) -> int:
    count: int = 0

    with open('files/ranges.txt') as f1:
        ranges: list[str] = f1.read().splitlines()

    with open('files/inputs.txt') as f2:
        for line in f2:
            input: int = int(line.strip())

            for range in ranges:
                nums: list[str] = range.split('-')

                start: int = int(nums[0])
                end:   int = int(nums[1])

                if search_func(start, end, input) != -1:
                    count += 1
                    break

    return count


def main():
    time_it(count_available_fresh_ingridient_ids, binary_search)
    time_it(count_available_fresh_ingridient_ids, standard_iteration)


if __name__ == '__main__':
    main()