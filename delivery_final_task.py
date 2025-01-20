def delivery(data: list[int], limit: int) -> int:
    """Функция находит минимальное количество платформ"""
    data.sort()
    left, right = 0, len(data) - 1
    count_platforms = 0
    while left <= right:
        if left == right:
            count_platforms += 1
            break
        if data[left] + data[right] <= limit:
            left += 1
            right -= 1
            count_platforms += 1
        else:
            right -= 1
            count_platforms += 1
    return count_platforms


if __name__ == '__main__':
    input_data = input().split()
    data = list(map(int, input_data))
    limit = int(input())

    result = delivery(data, limit)
    print(result)
    
