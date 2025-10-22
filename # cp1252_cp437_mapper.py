# cp1252_cp437_mapper.py

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
    alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    cp1252_chars = get_cp1252_chars()

    if len(cp1252_chars) < len(alphabet):
        raise ValueError("Not enough CP1252 characters to map all lowercase letters.")

    encode_map = {letter: cp1252_chars[i] for i, letter in enumerate(alphabet)}
    decode_map = {v: k for k, v in encode_map.items()}
    return encode_map, decode_map

def build_uppercase_mapping():
    """
    Builds a reversible map between 'A'-'Z' and CP437 characters 1–26,
    with 'T' mapped to 27 and 'U' mapped to 28.
    """
    encode_map = {}
    decode_map = {}
    for i in range(26):
        letter = chr(ord('A') + i)
        cp437_code = i + 1
        if letter == 'T':
            cp437_code = 27
        elif letter == 'U':
            cp437_code = 28
        cp437_char = bytes([cp437_code]).decode('cp437')
        encode_map[letter] = cp437_char
        decode_map[cp437_char] = letter
    return encode_map, decode_map

def encode_text(text, encode_map_lower, encode_map_upper):
    """
    Encodes lowercase and uppercase letters using the respective maps.
    """
    result = []
    for c in text:
        if c in encode_map_lower:
            result.append(encode_map_lower[c])
        elif c in encode_map_upper:
            result.append(encode_map_upper[c])
        else:
            result.append(c)
    return ''.join(result)

def decode_text(text, decode_map_lower, decode_map_upper):
    """
    Decodes mapped characters back to lowercase and uppercase letters.
    """
    result = []
    for c in text:
        if c in decode_map_lower:
            result.append(decode_map_lower[c])
        elif c in decode_map_upper:
            result.append(decode_map_upper[c])
        else:
            result.append(c)
    return ''.join(result)

ascii_art = r"""
   __  _____________    ______                            __        __       __                           __ 
  / / / /_  __/ ___/   / ____/___  ____________  ______  / /_     _/_/  ____/ /__  ____________  ______  / /_
 / / / / / /  \__ \   / __/ / __ \/ ___/ ___/ / / / __ \/ __/   _/_/   / __  / _ \/ ___/ ___/ / / / __ \/ __/
/ /_/ / / /  ___/ /  / /___/ / / / /__/ /  / /_/ / /_/ / /_   _/_/    / /_/ /  __/ /__/ /  / /_/ / /_/ / /_  
\____/ /_/  /____/  /_____/_/ /_/\___/_/   \__, / .___/\__/  /_/      \__,_/\___/\___/_/   \__, / .___/\__/  
                                          /____/_/                                        /____/_/           
"""

def asciiprint():
    print()
    print(ascii_art)
    print()

def main():
    encode_map_lower, decode_map_lower = build_lowercase_mapping()
    encode_map_upper, decode_map_upper = build_uppercase_mapping()

    print("=== Letter Mapper: CP1252 (a–z) + CP437 (A–Z) ===")
    print("1. Encode text")
    print("2. Decode text")
    choice = input("Choose (1/2): ").strip()

    if choice == "1":
        text = input("Enter text to encode (a–z and A–Z supported): ")
        result = encode_text(text, encode_map_lower, encode_map_upper)
        print("\nEncoded result:")
        print(result)
        print()
    elif choice == "2":
        text = input("Enter text to decode: ")
        result = decode_text(text, decode_map_lower, decode_map_upper)
        print("\nDecoded result:")
        print(result)
        print()
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    asciiprint()
    while True:
        main()
