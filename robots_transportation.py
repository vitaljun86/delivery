def delivery(data: list[int], limit: int) -> int:
    """Функция находит минимальное количество платформ  id_132081924"""
    data.sort()
    left, right = 0, len(data) - 1
    count_platforms = 0
    while left <= right:
        count_platforms += 1
        if data[left] + data[right] <= limit:
            left += 1
        right -= 1
    return count_platforms


if __name__ == '__main__':
    input_data = input().split()
    data = list(map(int, input_data))
    limit = int(input())

    result = delivery(data, limit)
    print(result)
    
