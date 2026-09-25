def to_numbers(text: str) -> list[int]:
    new_text = text.upper()
    numbers = []
    for char in new_text:
        if 'A' <= char <= 'Z':
            normalized_number = ord(char) - ord('A')
            numbers.append(normalized_number)

    return numbers