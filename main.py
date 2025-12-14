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


def main():
    print("Contando ingredientes frescos...")
    count = count_available_fresh_ingredients_ids(
        'files/ingredients/available/fresh/range-ids.txt',
        'files/ingredients/available/unknown/ids.txt'
    )
    print(f"{count} ingredientes frescos encontrados\n")


if __name__ == '__main__':
    main()


# 1. injetar nome do arquivo [x]
# 2. unit test []
# 3. decorator de time it []