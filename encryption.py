from itertools import cycle


class Encryption:
    def __init__(self, missings_char: str = "") -> None:
        self._int_to_char: str = ",?;.:/!'ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz0123456789" + missings_char
        self._size: int = len(self._int_to_char)
        self._char_to_int: dict = {c: i for i, c in enumerate(self._int_to_char)}

    def _str_to_ints(self, sentence: str) -> list[int]:
        return [self._char_to_int[c] for c in sentence]

    def _ints_to_str(self, ints: list[int]) -> str:
        return "".join(self._int_to_char[v] for v in ints)

    def encrypt(self, sentence: str, key: str) -> str:
        sentence = self._str_to_ints(sentence)
        key = self._str_to_ints(key)

        encrypted = [(i + k) % self._size for i, k in zip(sentence, cycle(key))]

        return self._ints_to_str(encrypted)

    def decrypt(self, sentence: str, key: str) -> str:
        sentence = self._str_to_ints(sentence)
        key = self._str_to_ints(key)

        decrypted = [(t - k) % self._size for t, k in zip(sentence, cycle(key))]

        return self._ints_to_str(decrypted)


if __name__ == "__main__":
    cipher = Encryption("-")
    sentence = (
        "I won't lose too much, just myself. There are always some things that are more important than others."
        "-- Klein Moretti 1360 LOTM"
    )
    cryptage_key = "cryptage key"

    code = cipher.encrypt(sentence, cryptage_key)
    decode = cipher.decrypt(code, cryptage_key)

    print(code, "\n\n", decode)
