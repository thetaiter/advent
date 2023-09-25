from hashlib import md5

def get_number_for_hash_starting_with_zeros(data, zeros = 5):
    md5_hex = ""
    number = 0

    while md5_hex[:zeros] != zeros * "0":
        number += 1
        md5_hex = md5(f"{data}{number}".encode("utf-8")).hexdigest()

    return number
