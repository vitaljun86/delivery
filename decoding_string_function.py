def get_decoding_string(encrypted_string: str) -> str:
    """Функция выполняет расшифровку зашифрованной строки id-132757719"""
    multiplier = 0
    current_string = ''
    stack_result = []
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for symbol in encrypted_string:
        if symbol in DIGITS:
            multiplier = multiplier * 10 + int(symbol)
        elif symbol == '[':
            stack_result.append((current_string, multiplier))
            multiplier = 0
            current_string = ''
        elif symbol == ']':
            string, number = stack_result.pop()
            current_string = string + number * current_string 
        else:
            current_string += symbol
    return current_string

if __name__ == '__main__':
    encrypted_string = input()
    result = get_decoding_string(encrypted_string)
    print(result)
