def is_input_in_range(start: int, end: int, target: int) -> int:
    l = start
    r = end

    while l <= r:
        m = (l + r) // 2

        if target > m:
            l = m + 1
        elif target < m:
            r = m - 1
        else:
            return m

    return -1


def main():
    count = 0

    ranges = open('files/ranges.txt').read().splitlines()
    lines  = open('files/inputs.txt')

    for line in lines:
        input = line.strip()
        
        for range in ranges:
            nums: list[str] = range.split('-')

            if is_input_in_range(
                int(nums[0]), 
                int(nums[1]), 
                int(input)
            ) != -1:
                count += 1
                break

    print(count)


if __name__ == '__main__':
    main()