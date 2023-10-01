def increment_letter(char: str):
    return chr((ord(char) - ord("a") + 1) % (ord("z") - ord("a") + 1) + ord("a"))


def increment_password(password: str):
    next_password = password

    for i in range(-1, -len(next_password), -1):
        next_password = (
            next_password[:i]
            + increment_letter(next_password[i])
            + (next_password[i + 1 :] if i < -1 else "")
        )

        if next_password[i] != "a":
            break

    return next_password


def validate_password(password: str, curr_password: str):
    if password == curr_password:
        return False

    if any([letter in ("i", "l", "o") for letter in password]):
        return False

    pairs = []
    for i in range(len(password) - 1):
        if password[i] == password[i + 1] and i not in pairs:
            pairs.append(i)
            pairs.append(i + 1)

    if len(pairs) < 4:
        return False

    for i in range(len(password) - 2):
        if (
            ord(password[i + 2]) - ord(password[i + 1]) == 1
            and ord(password[i + 1]) - ord(password[i]) == 1
        ):
            return True

    return False


def get_next_password(password: str):
    next_password = password

    while not validate_password(next_password, password):
        next_password = increment_password(next_password)

    return next_password
