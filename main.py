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


def main():
    encode_map, decode_map = build_lowercase_mapping()

    print("=== Lowercase ↔ CP1252 Mapper ===")
    print("1. Encode (a–z → CP1252 characters)")
    print("2. Decode (CP1252 characters → a–z)")
    choice = input("Choose (1/2): ").strip()

    if choice == "1":
        text = input("Enter lowercase text to encode: ")
        result = encode_text(text, encode_map)
        print("\nEncoded result:")
        print(result)
    elif choice == "2":
        text = input("Enter CP1252 text to decode: ")
        result = decode_text(text, decode_map)
        print("\nDecoded result:")
        print(result)
    else:
        print("Invalid choice. Please select 1 or 2.")

def UTP():
        result = encode_text(text, encode_map)
        print("\nEncoded result:")
        print(result)

if __name__ == "__main__":
    main()



