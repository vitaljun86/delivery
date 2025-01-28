def count_the_platforms_amount(weights: list[int], limit: int) -> int:
    """Функция находит минимальное количество платформ  id_132081924."""
    weights_of_robots = sorted(weights)
    left_pointer, right_pointer = 0, len(weights_of_robots) - 1
    count_platforms = 0
    while left_pointer <= right_pointer:
        count_platforms += 1
        if weights_of_robots[left_pointer] + weights_of_robots[right_pointer] <= limit:
            left_pointer += 1
        right_pointer -= 1
    return count_platforms


if __name__ == '__main__':
    input_weight = input().split()
    weights = [int(x) for x in input_weight]
    limit = int(input())
    result = count_the_platforms_amount(weights, limit)
    print(result)

    
