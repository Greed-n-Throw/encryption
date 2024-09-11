def code_de_zinzin(sentence: str, encryption_key: str):
    sentence_int = []
    for character in sentence:
        letter = 0
        if ord(character) == 32:  # code ASCII for space
            letter = 0
        else:
            letter = ord(character) - 96
        sentence_int.append(letter)

    key_int = []
    for character in encryption_key:
        letter = 0
        if ord(character) == 32:  # code ASCII for space
            letter = 0
        else:
            letter = ord(character) - 96
        key_int.append(letter)

    encrypt_int = []
    for i in range(0, len(sentence_int), len(key_int)):
        feur = sentence_int[i:i + len(key_int)]
        sum = [x + y for x, y in zip(feur, key_int)]
        encrypt_int.extend(sum)

    encrypt_str = []
    for digit in encrypt_int:
        if digit > 26:
            digit -= 27
        if digit == 0:
            letter = 65  # code ASCII for A
        else:
            letter = digit + 96
        lettre_finale = chr(letter)

        encrypt_str.extend(lettre_finale)
        phrase_encrypt = ''.join(encrypt_str)

    return (phrase_encrypt)


def decode_de_zinzin(sentence: str, encryption_key: str):
    sentence_int = []
    for character in sentence:
        letter = 0
        if ord(character) == 65:  # code ASCII for A
            letter = 0
        else:
            letter = ord(character) - 96
        sentence_int.append(letter)

    key_int = []
    for character in encryption_key:
        letter = 0
        if ord(character) == 32:  # code ASCII for space
            letter = 0
        else:
            letter = ord(character) - 96
        key_int.append(letter)

    encrypt_int = []
    for i in range(0, len(sentence_int), len(key_int)):
        feur = sentence_int[i:i + len(key_int)]
        sum = [x - y for x, y in zip(feur, key_int)]
        encrypt_int.extend(sum)

    unencrypt_str = []
    for digit in encrypt_int:
        if digit < 0:
            digit += 27
        if digit == 0:
            letter = 32
        else:
            letter = digit + 96
        lettre_finale = chr(letter)

        unencrypt_str.extend(lettre_finale)
        phrase_unencrypt = ''.join(unencrypt_str)

    return phrase_unencrypt


sentence = ("this is a test with this code only spaces and lowercases letters can be encrypted")
cryptage_key = ("cryptage key")

code = code_de_zinzin(sentence, cryptage_key)

decode = decode_de_zinzin(code, cryptage_key)

print(code)
print(decode)