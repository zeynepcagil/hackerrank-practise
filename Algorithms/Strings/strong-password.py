def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    number=False
    low=False
    upp=False
    special=False


    for char in password:
        if char in numbers:
            number=True
        if char in lower_case:
            low=True
        if char in upper_case:
            upp=True
        if char in special_characters:
            special=True
        missing_types = 0
        if not number:
            missing_types += 1
        if not low:
            missing_types += 1
        if not upp:
            missing_types += 1
        if not special:
            missing_types += 1
        needed_for_length = 0
        if n < 6:
            needed_for_length = 6 - n

    return max(missing_types, needed_for_length)  