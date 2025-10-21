# cp1252_lowercase_mapper.py
import arrr
from pyscript import document


def get_cp1252_chars():
    """
    Returns a list of CP1252 characters from codepoints 161–191, excluding 173.
    """
    chars = []
    for code in range(161, 192):
        if code == 173:
            continue
        chars.append(bytes([code]).decode('cp1252'))
    return chars


def build_lowercase_mapping():
    """
    Builds a reversible map between 'a'-'z' and CP1252 characters.
    """
    alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]  # ['a', ..., 'z']
    cp1252_chars = get_cp1252_chars()

    if len(cp1252_chars) < len(alphabet):
        raise ValueError("Not enough CP1252 characters to map all lowercase letters.")

    encode_map = {letter: cp1252_chars[i] for i, letter in enumerate(alphabet)}
    decode_map = {v: k for k, v in encode_map.items()}
    return encode_map, decode_map




def decode_text(text, decode_map):
    """
    Decodes CP1252-mapped characters back to lowercase letters. Leaves others unchanged.
    """
    return ''.join(decode_map.get(c, c) for c in text)

if __name__ == "__main__":
    main()




