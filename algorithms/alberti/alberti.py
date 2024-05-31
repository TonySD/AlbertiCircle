import re
from typing import List, Tuple
from algorithms.alberti.config import *

def encrypt(letter: str, key: str):
    index = ALPHABET.find(letter)
    return key[index]

def decrypt(letter: str, key: str):
    index = key.find(letter)
    return ALPHABET[index]

def rotate_key(key: str, shift: int = 1):
    return key[-shift:] + key[:-shift]

def basic_decrypt_text(text: str, key: str):
    result = list()
    for char in text:
        result.append(
            decrypt(char, key)
        )
        key = rotate_key(key)
    return ''.join(result)

# MODE 1
def mode1(text: str, key: str):
    while key[0] != text[0]:
        key = rotate_key(key)

    return basic_decrypt_text(text, key)

# MODE 2
def mode2(text: str, key: str):
    while decrypt(decrypt(text[0], key), key) != ALPHABET[0]:
        key = rotate_key(key)
    
    return basic_decrypt_text(text, key)

# MODE 3
# If indicator letter not specified - return all variations. Choose one and specify to decrypt
def mode3(text: str, key: str, indicator_letter = None) -> str | List[str]:
    if indicator_letter is not None:
        #     key.find(indicator_letter) != 0
        while key.find(indicator_letter) != ALPHABET.find('А'):
            key = rotate_key(key)

        return basic_decrypt_text(text, key)

    # Not given indicator -> broot
    # Return format: [indicator] decrypted texts
    result = list()
    for shift in range(len(key)):
        current_key = rotate_key(key, shift)
        result.append(f"[{current_key[0]}] {basic_decrypt_text(text, current_key)}")
    return result

# MODE 4
def mode4(text: str, key: str):
    result = list()
    for char in text:
        # if char uppercase - change keys
        if char in ALPHABET:
            while key.find(char) != 0: key = rotate_key(key)
            continue
        
        result.append(decrypt(
            char.upper(), key
        ))
    return ''.join(result)

def find_tallest_substr(text: str, index: int, length: int):
    start_count = text.count(
        text[index : index + length]
    )
    while text.count(text[index : index + length]) == start_count:
        length += 1

    return text[index : index + length - 1]

def find_all_substr(text: str, min_len: int = 4):
    result = list()
    i = 0
    while i < len(text) - 4:
        window = text[i : i + min_len]
        if text.count(window) > 1:
            result.append(
                find_tallest_substr(
                    text,
                    i,
                    min_len
                )
            )
            i += len(result[-1]) - 1
        i += 1
    return result

def index_all_substr(text: str, substr: str):
    return [m.start() for m in re.finditer(substr, text)]

def split_to_delims(number: int):
    delimiters = list()
    for i in range(2, int(number ** (1/2))):
        if number % i == 0:
            delimiters.append(i)
            delimiters.append(number // i)
    if (number ** (1/2)).is_integer():
        delimiters.append(int(
            number ** (1/2)
        ))

    return delimiters

def encrypt_mode_5(text: str, key: str, password: str):
    encrypted = list()
    for i in range(len(text)):
        while key.find(password[i % len(password)]) != 0:
            key = rotate_key(key)
        
        encrypted.append(
            encrypt(text[i], key)
        )
    return "".join(encrypted)

def mode5(text: str, key: str, password = None) -> str | List[int]:
    if password is not None:
        result = list()
        for i in range(len(text)):
            while key.find(password[i % len(password)]) != 0:
                key = rotate_key(key)
            
            result.append( 
                decrypt(text[i], key)
            )
        return ''.join(result)
    
    # Without spaces
    mono_text = text.replace(' ', '')

    sequences = find_all_substr(
        mono_text
    )
    sequences_delimiters: List[set] = None
    for sequence in sequences:
        indexes = index_all_substr(mono_text, sequence)
        indexes = [indexes[i + 1] - indexes[i] for i in range(len(indexes) - 1)]
        # delims = [split_to_delims(i) for i in indexes]
        delims = [set(split_to_delims(i)) for i in indexes]

        if sequences_delimiters is None: sequences_delimiters = delims[0]

        for i in range(1, len(delims) - 1):
            sequences_delimiters = sequences_delimiters.intersection(delims[i])

    return sorted(list(sequences_delimiters))
             

if ENABLE_TESTS:
    assert mode1(MODE1_CIPHER, LECTION_KEY) == MODE1_PLAIN

    assert mode2(MODE2_CIPHER, LECTION_KEY) == MODE2_PLAIN
    # Broot test
    assert any([MODE3_PLAIN in mode for mode in mode3(MODE3_CIPHER, LECTION_KEY)])
    # Indicator letter test
    assert mode3(MODE3_CIPHER, LECTION_KEY, 'Х') == MODE3_PLAIN

    assert mode4(MODE4_CIPHER, LECTION_KEY) == MODE4_PLAIN
    
    assert mode5(MODE5_CIPHER, LECTION_KEY, MODE5_PASSWORD) == MODE5_PLAIN

    # Kasiski
    text = "Криптография - это область науки, посвященная защите информации от несанкционированного доступа путем преобразования ее в нечитаемую форму. Она использует различные методы и алгоритмы для шифрования данных таким образом, чтобы только авторизованные пользователи могли получить к ним доступ. Криптография играет ключевую роль в обеспечении безопасности информации в сети Интернет, банковской сфере, государственных организациях и других сферах, где важна конфиденциальность данных. С развитием криптографических методов также возрастает уровень защиты, что помогает предотвращать кибератаки и сохранять конфиденциальность коммуникаций."
    text = text.replace('.', '').replace('-', '').replace(',', '').replace(' ', '').upper()
    key = "МОЙКЛЮЧИ"
    encrypted = encrypt_mode_5(text, LECTION_KEY, key)
    assert len(key) in mode5(encrypted, LECTION_KEY)

