def get_decoding_string(encrypted_string: str) -> str:
    """Функция выполняет расшифровку зашифрованной строки id-132700773"""
    current_number = 0
    current_string = ''
    stack_result = []

    for item in encrypted_string:
        if item.isdigit():
            current_number = current_number * 10 + int(item)
        elif item == '[':
            stack_result.append((current_string, current_number))
            current_number = 0
            current_string = ''
        elif item == ']':
            string, number = stack_result.pop()
            current_string = string + number * current_string 
        else:
            current_string += item
    return current_string

if __name__ == '__main__':
    encrypted_string = input()
    result = get_decoding_string(encrypted_string)
    print(result)
