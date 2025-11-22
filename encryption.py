def convert_str_into_digit_list(string: str) -> list[int]:
    int_list = []
    for char in string:
        int_list.append(0 if ord(char) == 32 else ord(char) - 96)  # 32 code ASCII for space, 97 for a

    return int_list


def convert_digit_list_into_str(int_list: list[int]) -> str:
    str_list = []
    for digit in int_list:
        str_list.append(chr(32) if digit == 0 else chr(digit + 96))

    return "".join(str_list)


def encryption(sentence: str, key: str):
    sentence = convert_str_into_digit_list(sentence)
    key = convert_str_into_digit_list(key)

    while len(key) < len(sentence):
        key.extend(key)

    encrypt = []
    for s, k in zip(sentence, key):
        comb = s + k
        encrypt.append(comb if comb < 27 else comb - 27)

    encrypt = convert_digit_list_into_str(encrypt)

    return encrypt


def un_encryption(sentence: str, key: str):
    sentence = convert_str_into_digit_list(sentence)
    key = convert_str_into_digit_list(key)

    while len(key) < len(sentence):
        key.extend(key)

    un_encrypt = []
    for s, k in zip(sentence, key):
        comb = s - k
        un_encrypt.append(comb + 27 if comb < 0 else comb if comb < 27 else comb - 27)

    un_encrypt = convert_digit_list_into_str(un_encrypt)

    return un_encrypt


if __name__ == "__main__":
    sentence = "this is a test with this code only spaces and lowercases letters can be encrypted"
    cryptage_key = "cryptage key"

    code = encryption(sentence, cryptage_key)
    decode = un_encryption(code, cryptage_key)

    print(code, "\n\n", decode)
