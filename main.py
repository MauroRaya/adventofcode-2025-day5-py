import os.path

def count_available_fresh_ingredients_ids(
    fresh_ingredients_ranges_ids_path: str,
    ingredients_ids_path: str
) -> int:
    count: int = 0

    with open(fresh_ingredients_ranges_ids_path) as f1:
        ranges: list[str] = f1.read().splitlines()

    with open(ingredients_ids_path) as f2:
        for line in f2:
            ingredient_id: int = int(line.strip())

            for range in ranges:
                nums: list[str] = range.split('-')

                start: int = int(nums[0])
                end:   int = int(nums[1])

                if start <= ingredient_id <= end:
                    count += 1
                    break

    return count


def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key=lambda x : x[0])
    merged: list[list[int]] = [intervals[0]]

    for current in intervals[1:]:
        previous: list[int] = merged[-1]

        if current[0] <= previous[1]:
            previous[1] = max(previous[1], current[1])
        else:
            merged.append(current)
    
    return merged


def count_all_fresh_ingredients_ids(
    fresh_ingredients_ranges_ids_path: str
) -> int:
    # if os.path.isfile('files/ingredients/fresh/merged-range-ids.txt'):
    #     return

    with open(fresh_ingredients_ranges_ids_path) as f:
        lines: list[str] = f.read().splitlines()

    ranges: list[list[int]] = []

    for line in lines:
        range: list[int] = [int(id) for id in line.split('-')]
        ranges.append(range)

    merged: list[list[int]] = merge_intervals(ranges)

    count = 0

    for range in merged:
        count += range[1] - range[0] + 1

    return count


def main():
    print("Contando ingredientes frescos disponiveis...")
    count = count_available_fresh_ingredients_ids(
        'files/ingredients/fresh/range-ids.txt',
        'files/ingredients/available/ids.txt'
    )
    print(f"{count} ingredientes frescos disponiveis encontrados\n")

    print("Contando todos os ingredientes frescos...")
    count = count_all_fresh_ingredients_ids(
        'files/ingredients/fresh/range-ids.txt'
    )
    print(f"{count} ingredientes frescos encontrados\n")


if __name__ == '__main__':
    main()
