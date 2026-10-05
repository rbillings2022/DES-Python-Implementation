def ascii_encoding(text):
    """
        Description: 
            This function encodes text into a binary list where each element is 
            one bit.
    """
    encoding_scheme = { 
        # Control characters (0-31)
        '\x00': '00000000', '\x01': '00000001', '\x02': '00000010','\x03': '00000011',
        '\x04': '00000100','\x05': '00000101', '\x06': '00000110', '\x07': '00000111',
        '\x08': '00001000', '\t': '00001001', '\n':   '00001010','\x0b': '00001011',
        '\x0c': '00001100', '\r': '00001101', '\x0e': '00001110', '\x0f': '00001111',
        '\x10': '00010000', '\x11': '00010001', '\x12': '00010010', '\x13': '00010011',
        '\x14': '00010100', '\x15': '00010101', '\x16': '00010110', '\x17': '00010111',
        '\x18': '00011000', '\x19': '00011001', '\x1a': '00011010', '\x1b': '00011011',
        '\x1c': '00011100', '\x1d': '00011101', '\x1e': '00011110', '\x1f': '00011111',

        # Printable ASCII (32-126)
        ' ': '00100000', '!': '00100001', '"': '00100010', '#': '00100011',
        '$': '00100100', '%': '00100101', '&': '00100110', "'": '00100111',
        '(': '00101000', ')': '00101001', '*': '00101010', '+': '00101011',
        ',': '00101100', '-': '00101101', '.': '00101110', '/': '00101111',
        '0': '00110000', '1': '00110001', '2': '00110010', '3': '00110011',
        '4': '00110100', '5': '00110101', '6': '00110110', '7': '00110111',
        '8': '00111000', '9': '00111001', ':': '00111010', ';': '00111011',
        '<': '00111100', '=': '00111101', '>': '00111110', '?': '00111111',
        '@': '01000000', 'A': '01000001', 'B': '01000010', 'C': '01000011',
        'D': '01000100', 'E': '01000101', 'F': '01000110', 'G': '01000111',
        'H': '01001000', 'I': '01001001', 'J': '01001010', 'K': '01001011',
        'L': '01001100', 'M': '01001101', 'N': '01001110', 'O': '01001111',
        'P': '01010000', 'Q': '01010001', 'R': '01010010', 'S': '01010011',
        'T': '01010100', 'U': '01010101', 'V': '01010110', 'W': '01010111',
        'X': '01011000', 'Y': '01011001', 'Z': '01011010', '[': '01011011',
        '\\': '01011100', ']': '01011101', '^': '01011110', '_': '01011111',
        '`': '01100000', 'a': '01100001', 'b': '01100010', 'c': '01100011',
        'd': '01100100', 'e': '01100101', 'f': '01100110', 'g': '01100111',
        'h': '01101000', 'i': '01101001', 'j': '01101010', 'k': '01101011',
        'l': '01101100', 'm': '01101101', 'n': '01101110', 'o': '01101111',
        'p': '01110000', 'q': '01110001', 'r': '01110010', 's': '01110011',
        't': '01110100', 'u': '01110101', 'v': '01110110', 'w': '01110111',
        'x': '01111000', 'y': '01111001', 'z': '01111010', '{': '01111011',
        '|': '01111100', '}': '01111101', '~': '01111110',
        '\x7f': '01111111',  # DEL

        # Extended ASCII / Code Page 437 (128-255)
        'Ç': '10000000', 'ü': '10000001', 'é': '10000010', 'â': '10000011',
        'ä': '10000100', 'à': '10000101', 'å': '10000110', 'ç': '10000111',
        'ê': '10001000', 'ë': '10001001', 'è': '10001010', 'ï': '10001011',
        'î': '10001100', 'ì': '10001101', 'Ä': '10001110', 'Å': '10001111',
        'É': '10010000', 'æ': '10010001', 'Æ': '10010010', 'ô': '10010011',
        'ö': '10010100', 'ò': '10010101', 'û': '10010110', 'ù': '10010111',
        'ÿ': '10011000', 'Ö': '10011001', 'Ü': '10011010', '¢': '10011011',
        '£': '10011100', '¥': '10011101', '₧': '10011110', 'ƒ': '10011111',
        'á': '10100000', 'í': '10100001', 'ó': '10100010', 'ú': '10100011',
        'ñ': '10100100', 'Ñ': '10100101', 'ª': '10100110', 'º': '10100111',
        '¿': '10101000', '⌐': '10101001', '¬': '10101010', '½': '10101011',
        '¼': '10101100', '¡': '10101101', '«': '10101110', '»': '10101111',
        '░': '10110000', '▒': '10110001', '▓': '10110010', '│': '10110011',
        '┤': '10110100', '╡': '10110101', '╢': '10110110', '╖': '10110111',
        '╕': '10111000', '╣': '10111001', '║': '10111010', '╗': '10111011',
        '╝': '10111100', '╜': '10111101', '╛': '10111110', '┐': '10111111',
        '└': '11000000', '┴': '11000001', '┬': '11000010', '├': '11000011',
        '─': '11000100', '┼': '11000101', '╞': '11000110', '╟': '11000111',
        '╚': '11001000', '╔': '11001001', '╩': '11001010', '╦': '11001011',
        '╠': '11001100', '═': '11001101', '╬': '11001110', '╧': '11001111',
        '╨': '11010000', '╤': '11010001', '╥': '11010010', '╙': '11010011',
        '╘': '11010100', '╒': '11010101', '╓': '11010110', '╫': '11010111',
        '╪': '11011000', '┘': '11011001', '┌': '11011010', '█': '11011011',
        '▄': '11011100', '▌': '11011101', '▐': '11011110', '▀': '11011111',
        'α': '11100000', 'ß': '11100001', 'Γ': '11100010', 'π': '11100011',
        'Σ': '11100100', 'σ': '11100101', 'µ': '11100110', 'τ': '11100111',
        'Φ': '11101000', 'Θ': '11101001', 'Ω': '11101010', 'δ': '11101011',
        '∞': '11101100', 'φ': '11101101', 'ε': '11101110', '∩': '11101111',
        '≡': '11110000', '±': '11110001', '≥': '11110010', '≤': '11110011',
        '⌠': '11110100', '⌡': '11110101', '÷': '11110110', '≈': '11110111',
        '°': '11111000', '∙': '11111001', '·': '11111010', '√': '11111011',
        'ⁿ': '11111100', '²': '11111101', '■': '11111110', '\xa0': '11111111',
        }


    binary = []

    # Loop through the encoding dictionary
        # To find the binary representation
        # of each letter from the text list
        # Then append the binary into 
        # binary list
    for i in text:
        binary.append(encoding_scheme[i])

    # Right now the list is 8 bits for each element
        # .join all the elements then make each
        # bit into a list
    return list("".join(binary))

def ascii_decoding(text)-> list:
    decoding_scheme = {
        '00000000': '\x00', '00000001': '\x01', '00000010': '\x02', '00000011': '\x03',
        '00000100': '\x04', '00000101': '\x05', '00000110': '\x06', '00000111': '\x07',
        '00001000': '\x08', '00001001': '\t',   '00001010': '\n',   '00001011': '\x0b',
        '00001100': '\x0c', '00001101': '\r',   '00001110': '\x0e', '00001111': '\x0f',
        '00010000': '\x10', '00010001': '\x11', '00010010': '\x12', '00010011': '\x13',
        '00010100': '\x14', '00010101': '\x15', '00010110': '\x16', '00010111': '\x17',
        '00011000': '\x18', '00011001': '\x19', '00011010': '\x1a', '00011011': '\x1b',
        '00011100': '\x1c', '00011101': '\x1d', '00011110': '\x1e', '00011111': '\x1f',

        '00100000': ' ', '00100001': '!', '00100010': '"', '00100011': '#',
        '00100100': '$', '00100101': '%', '00100110': '&', '00100111': "'",
        '00101000': '(', '00101001': ')', '00101010': '*', '00101011': '+',
        '00101100': ',', '00101101': '-', '00101110': '.', '00101111': '/',
        '00110000': '0', '00110001': '1', '00110010': '2', '00110011': '3',
        '00110100': '4', '00110101': '5', '00110110': '6', '00110111': '7',
        '00111000': '8', '00111001': '9', '00111010': ':', '00111011': ';',
        '00111100': '<', '00111101': '=', '00111110': '>', '00111111': '?',
        '01000000': '@', '01000001': 'A', '01000010': 'B', '01000011': 'C',
        '01000100': 'D', '01000101': 'E', '01000110': 'F', '01000111': 'G',
        '01001000': 'H', '01001001': 'I', '01001010': 'J', '01001011': 'K',
        '01001100': 'L', '01001101': 'M', '01001110': 'N', '01001111': 'O',
        '01010000': 'P', '01010001': 'Q', '01010010': 'R', '01010011': 'S',
        '01010100': 'T', '01010101': 'U', '01010110': 'V', '01010111': 'W',
        '01011000': 'X', '01011001': 'Y', '01011010': 'Z', '01011011': '[',
        '01011100': '\\', '01011101': ']', '01011110': '^', '01011111': '_',
        '01100000': '`', '01100001': 'a', '01100010': 'b', '01100011': 'c',
        '01100100': 'd', '01100101': 'e', '01100110': 'f', '01100111': 'g',
        '01101000': 'h', '01101001': 'i', '01101010': 'j', '01101011': 'k',
        '01101100': 'l', '01101101': 'm', '01101110': 'n', '01101111': 'o',
        '01110000': 'p', '01110001': 'q', '01110010': 'r', '01110011': 's',
        '01110100': 't', '01110101': 'u', '01110110': 'v', '01110111': 'w',
        '01111000': 'x', '01111001': 'y', '01111010': 'z', '01111011': '{',
        '01111100': '|', '01111101': '}', '01111110': '~',
        '01111111': '\x7f',

        '10000000': 'Ç', '10000001': 'ü', '10000010': 'é', '10000011': 'â',
        '10000100': 'ä', '10000101': 'à', '10000110': 'å', '10000111': 'ç',
        '10001000': 'ê', '10001001': 'ë', '10001010': 'è', '10001011': 'ï',
        '10001100': 'î', '10001101': 'ì', '10001110': 'Ä', '10001111': 'Å',
        '10010000': 'É', '10010001': 'æ', '10010010': 'Æ', '10010011': 'ô',
        '10010100': 'ö', '10010101': 'ò', '10010110': 'û', '10010111': 'ù',
        '10011000': 'ÿ', '10011001': 'Ö', '10011010': 'Ü', '10011011': '¢',
        '10011100': '£', '10011101': '¥', '10011110': '₧', '10011111': 'ƒ',
        '10100000': 'á', '10100001': 'í', '10100010': 'ó', '10100011': 'ú',
        '10100100': 'ñ', '10100101': 'Ñ', '10100110': 'ª', '10100111': 'º',
        '10101000': '¿', '10101001': '⌐', '10101010': '¬', '10101011': '½',
        '10101100': '¼', '10101101': '¡', '10101110': '«', '10101111': '»',
        '10110000': '░', '10110001': '▒', '10110010': '▓', '10110011': '│',
        '10110100': '┤', '10110101': '╡', '10110110': '╢', '10110111': '╖',
        '10111000': '╕', '10111001': '╣', '10111010': '║', '10111011': '╗',
        '10111100': '╝', '10111101': '╜', '10111110': '╛', '10111111': '┐',
        '11000000': '└', '11000001': '┴', '11000010': '┬', '11000011': '├',
        '11000100': '─', '11000101': '┼', '11000110': '╞', '11000111': '╟',
        '11001000': '╚', '11001001': '╔', '11001010': '╩', '11001011': '╦',
        '11001100': '╠', '11001101': '═', '11001110': '╬', '11001111': '╧',
        '11010000': '╨', '11010001': '╤', '11010010': '╥', '11010011': '╙',
        '11010100': '╘', '11010101': '╒', '11010110': '╓', '11010111': '╫',
        '11011000': '╪', '11011001': '┘', '11011010': '┌', '11011011': '█',
        '11011100': '▄', '11011101': '▌', '11011110': '▐', '11011111': '▀',
        '11100000': 'α', '11100001': 'ß', '11100010': 'Γ', '11100011': 'π',
        '11100100': 'Σ', '11100101': 'σ', '11100110': 'µ', '11100111': 'τ',
        '11101000': 'Φ', '11101001': 'Θ', '11101010': 'Ω', '11101011': 'δ',
        '11101100': '∞', '11101101': 'φ', '11101110': 'ε', '11101111': '∩',
        '11110000': '≡', '11110001': '±', '11110010': '≥', '11110011': '≤',
        '11110100': '⌠', '11110101': '⌡', '11110110': '÷', '11110111': '≈',
        '11111000': '°', '11111001': '∙', '11111010': '·', '11111011': '√',
        '11111100': 'ⁿ', '11111101': '²', '11111110': '■', '11111111': '\xa0',
        }

    sentence = []

    for i in text:
        sentence.append(decoding_scheme[i])

    return "".join(sentence)

def intitial_permutation(plaintext):
    intitial_permutation = [58, 50, 42, 34, 26, 18, 10, 2,
                            60, 52, 44, 36, 28, 20, 12, 4,
                            62, 54, 46, 38, 30, 22, 14, 6,
                            64, 56, 48, 40, 32, 24, 16, 8,
                            57, 49, 41, 33, 25, 17, 9, 1,
                            59, 51, 43, 35, 27, 19, 11, 3,
                            61, 53, 45, 37, 29, 21, 13, 5,
                            63, 55, 47, 39, 31, 23, 15, 7]
    
    result = []
    # This for loop iterates through plaintext list
        # and initiial permutation list to 
    for i in range(len(intitial_permutation)):
        result.append(plaintext[intitial_permutation[i]-1])

    return result

def inverse_IP(ciphertext):
    """
        Description: 
            This function creates a new list from 2 lists. The inverse of IP
            and the ciphertext (A 64 bit binary)
            It uses elements from PC1 as position/index numbers to search for
            bits in the key list. Then appendeds that bit into a new list position
        
        Args:
            ciphertext: list
    """
    final_perm = [40, 8, 48, 16, 56, 24, 64, 32,
                39, 7, 47, 15, 55, 23, 63, 31,
                38, 6, 46, 14, 54, 22, 62, 30,
                37, 5, 45, 13, 53, 21, 61, 29,
                36, 4, 44, 12, 52, 20, 60, 28,
                35, 3, 43, 11, 51, 19, 59, 27,
                34, 2, 42, 10, 50, 18, 58, 26,
                33, 1, 41, 9, 49, 17, 57, 25]
    result = []
    for i in range(len(final_perm)):
        result.append(ciphertext[final_perm[i]-1])

    return result

# Create a List of bytes (8-bits)
def byte_grouping(ciphertext):
    """
        Description:
            This function groups the list of bits into 8-bits each element.
    """
    temp_list = []

    sentence = []

    for i in range(0, len(ciphertext), 8):
        for j in ciphertext[i:8+i]:
            temp_list.append(j)
        store_byte = "".join(temp_list)
        sentence.append(store_byte)
        temp_list.clear()

    return sentence

# KEY SCHEDULING
"""
    Description: You generate a master key and the subkeys created by it are 
    derived from that master key.

    DECRYPTION: TO DECRYPT JUST REVERSE THE LIST OF KEYS FROM 1 -> 16 TO 16 -> 1
"""

def permuted_choice1(key:list) -> list:
    """
        Description: 
            This function creates a new list from 2 lists. (A 56 bit binary) 
            It uses elements from PC1 as position/index numbers to search for
            bits in the key list. Then appendeds that bit into a new list position
        
        Args:
            key: list
    """
    # Compresses and generates a 56 bit binary list
    PC1 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]

    effective_key = []

    # For loop that iterations from 0 -> 55
    for i in range(len(PC1)):
        # Creates a new list by moving the position
            # of bits with the elements from PC1
            # Then Append the new element to a new list
        effective_key.append(key[PC1[i] - 1])

    return effective_key

# This function generates a list of subkeys
def generate_subkeys(key:list) -> list:
    """
        Description:
            This function takes in a list (56-bit binary)
            and splits it in half (28-bits each) to create 
            lists C and D. Both C and D will perform circular 
            shift where either the first bit or first two bits 
            will move to the end of the list.
        Args:
            shift_number: gives the number of bits shifted
            key: list of bits

        Returns:
            shifted_c: list
            shifted_d: list
    """
    # Split the list with slicing
    # C gets the first 28-bits
    # D gets the last 28-bits
    length = len(key)//2
    c = key[:length]
    d = key[length:]

    shift_schedule = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

    subkey_list = []
    # Shift the bits by slicing the first bit or the first 2 bits
        # then adding the first or 2 bits at the end
    for shift_number in shift_schedule:
        c = c[shift_number:] + c[:shift_number]
        d = d[shift_number:] + d[:shift_number]
        # Generate a 48-bit subkey
        subkey = permuted_choice2(c+d)

        subkey_list.append(subkey)
    return subkey_list

def permuted_choice2(key:list) -> list:
    """
        Description: 
            This function creates a new list from 2 lists. (A 48 bit binary)
            It uses elements from PC1 as position/index numbers to search for
            bits in the key list. Then appendeds that bit into a new list position
        
        Args:
            key: list

        Returns:
            subkey: list
    """
    # Compreses and generates a 48 bit binary list
    PC2 = [14, 17, 11, 24, 1, 5,
       3, 28, 15, 6, 21, 10,
       23, 19, 12, 4, 26, 8,
       16, 7, 27, 20, 13, 2,
       41, 52, 31, 37, 47, 55,
       30, 40, 51, 45, 33, 48,
       44, 49, 39, 56, 34, 53,
       46, 42, 50, 36, 29, 32]

    # The subkey result is stored here.
    subkey = []

    for i in range(len(PC2)):
        # Creates a new list by moving the position
            # of bits with the elements from PC1
            # Then Append the new element to a new list
        subkey.append(key[PC2[i]-1])

    return subkey

# EXPANSION TABLE
def expansion_table(plaintext):
	exp_d = [32, 1, 2, 3, 4, 5, 4, 5,
			6, 7, 8, 9, 8, 9, 10, 11,
			12, 13, 12, 13, 14, 15, 16, 17,
			16, 17, 18, 19, 20, 21, 20, 21,
			22, 23, 24, 25, 24, 25, 26, 27,
			28, 29, 28, 29, 30, 31, 32, 1]
	result = []
	for i in range(len(exp_d)):
		result.append(plaintext[exp_d[i]-1])
	return result

# S-BOX
def four_bit_number_decoding(binary:str)-> int:
    four_bit_decode_scheme = {
    '0000': 0,'0001': 1,'0010': 2,'0011': 3,
    '0100': 4,'0101': 5,'0110': 6,'0111': 7,
    '1000': 8,'1001': 9,'1010': 10,'1011': 11,
    '1100': 12,'1101': 13,'1110': 14,'1111': 15,
    }
    return four_bit_decode_scheme[binary]

def two_bit_decoding(binary:str) -> int:
    two_bit_scheme = {
        '00':0,
        '01':1,
        '10':2,
        '11':3
    }
    return two_bit_scheme[binary]

def four_bit_number_encoding(number:int) -> str:
    four_bit_scheme = {
    0: '0000',1: '0001',2: '0010',3: '0011',4: '0100',
    5: '0101',6: '0110',7: '0111',8: '1000',9: '1001',
    10: '1010',11: '1011',12: '1100',13: '1101',14: '1110',
    15: '1111',
    }
    
    return four_bit_scheme[number]

def s_box_function(plaintext):
    sbox = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

        [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

        [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

        [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

        [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

        [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

        [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

        [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]

    list_of_six_bits = []
    # The job is to take a 48-bit list and
        # divide it into 8 list of 6 bits
    for i in range(0, len(plaintext), 6): # Jump every 6 elements
        six_bits = []
        # Wherever the outter loop is we iterate and append 6 elements
            # Then append that list into the list_of_six_bits
        for j in range(i, 6+i):
            six_bits.append(plaintext[j])
        list_of_six_bits.append(six_bits)

    four_bit_list = []
    for i in range(len(list_of_six_bits)):
        row = two_bit_decoding("".join(list_of_six_bits[i][:1]+list_of_six_bits[i][5:]))
        column = four_bit_number_decoding("".join(list_of_six_bits[i][1:5]))

        four_bit_value = four_bit_number_encoding(sbox[i][row][column])
        four_bit_list.append(four_bit_value)

        four_bit_list = list("".join(four_bit_list))
    return four_bit_list

# P-PERMUATION TABLE

def p_permutation(plaintext):
    permutation = [16, 7, 20, 21,
        29, 12, 28, 17,
        1, 15, 23, 26,
        5, 18, 31, 10,
        2, 8, 24, 14,
        32, 27, 3, 9,
        19, 13, 30, 6,
        22, 11, 4, 25]

    result = []

    for i in range(len(permutation)):
        result.append(plaintext[permutation[i]-1])
    return result

# FEISTEL CIPHER ROUNDS
def xor(bit1:str, bit_key:str) -> str:
    """
        Description:
            XOR function that takes two lists of bits as arguments and
            XOR them, returning either a '0' if two bits form the list 
            are the same or '1' if thw two bits are different.
    """
    if bit1 == bit_key:
        return '0'
    else:
        return '1'
        
def encrypt_fiestel_rounds(plaintext:list, masterkey:list) -> list:
    """
        Description:
            First it splits the 64-bit list into 2 list of 32-bit numbers
            This is a fiestel function that performs 16 rounds of
            bit swapping and XOR bits with subkeys
    """
    plaintext_ip = intitial_permutation(plaintext)
    # Key Generation Functions
    effecive_key = permuted_choice1(masterkey)
    subkeys_list = generate_subkeys(effecive_key)

    # Split 64-bits into 2 lists of 32 bits. Left and Right
    length = len(plaintext_ip)//2
    left = plaintext_ip[:length]
    right = plaintext_ip[length:]

    for r in range(16):
        old_left = left
        # Right is only 32-bits so we need to expand it to 48-bits
            # Each round
        old_right = right
        expended = expansion_table(right)

        # f(right, subkey): XOR previous Right bits with the subkey
            # XOR each bit and append the resulting bit to the f_out list
        expanded_right = []
        for c in range(48):
            expanded_right.append(xor(expended[c], subkeys_list[r][c]))

        compress_right = s_box_function(expanded_right)

        permuted_right = p_permutation(compress_right)
        # new_right = old_left XOR f_out
        new_right = []
        for c in range(32):

            new_right.append(xor(old_left[c], permuted_right[c]))

        left = old_right
        right = new_right
    # After feistel encryption swap left and right.
    right, left = left, right

    # Send the finished feistel encrypted bits to
        # be rearranged by the inverse IP table
    feistel_inverse_perm = inverse_IP(left+right)

    # Return encrypted bits
    return feistel_inverse_perm


def decrypt_fiestel_rounds(ciphertext:list, masterkey:list) -> list:
    plaintext_ip = intitial_permutation(ciphertext)
    # Key Generation Functions
    effecive_key = permuted_choice1(masterkey)
    subkeys_list = generate_subkeys(effecive_key)

    # Split 64-bits into 2 lists of 32 bits. Left and Right
    length = len(plaintext_ip)//2
    left = plaintext_ip[:length]
    right = plaintext_ip[length:]

    for r in range(15,-1,-1):
        old_left = left
        # Right is only 32-bits so we need to expand it to 48-bits
            # Each round
        old_right = right
        expended = expansion_table(right)

        # f(right, subkey): XOR previous Right bits with the subkey
            # XOR each bit and append the resulting bit to the f_out list
        expanded_right = []
        for c in range(48):
            expanded_right.append(xor(expended[c], subkeys_list[r][c]))

        compress_right = s_box_function(expanded_right)

        permuted_right = p_permutation(compress_right)
        # new_right = old_left XOR f_out
        new_right = []
        for c in range(32):

            new_right.append(xor(old_left[c], permuted_right[c]))

        left = old_right
        right = new_right
    # After feistel encryption swap left and right.
    right, left = left, right

    # Send the finished feistel encrypted bits to
        # be rearranged by the inverse IP table
    decrypted_f_inverse_perm = inverse_IP(left+right)

    # Return encrypted bits
    return decrypted_f_inverse_perm

def mode_of_operation(message:str, secret_key:str):
    """
        Description: This function will handle everything
        - The encoding, 
        - The decoding, 
        - Partitioning the message
        - Return the ciphertext
    """

    # Padding the plaintext so the character number
        # is a multiple of 8
    padding = len(message)%8
    if padding > 0:
        padding = 8 - padding
    message = message+("!"*padding)

    list_of_DES_blocks = []

    warning = "\n**THE SOFTWARE ONLY SUPPORTS A NUMBER OF CHARACTERS THATS A MULTIPLE OF 8**\n " \
                "**So the system will pad every message with '!' if needed**"
    new_message = f"Message after padding applied: {message}"
    encoded_plaintext = ascii_encoding(message)
    encoded_secret_key = ascii_encoding(secret_key)

    for i in range(0, len(encoded_plaintext), 64):
        block = []
        for j in range(i, 64+i):
            block.append(encoded_plaintext[j])
        list_of_DES_blocks.append(block)

    list_of_ciphertext = []
    list_of_ciphertext_bits = []
    # TEST DES ENCRYPTION BY FEEDING THE BITS TO THE FEISTEL ROUNDS FUNCTION
    for i in range(len(list_of_DES_blocks)):
        encrypted_text = encrypt_fiestel_rounds(list_of_DES_blocks[i], encoded_secret_key)
        list_of_ciphertext_bits.append(encrypted_text)
    
        # Decode each block of ciphertext then append eack block to a list
        group_ciphertext = byte_grouping(encrypted_text)
        decoded_ciphertext_block = ascii_decoding(group_ciphertext)
        list_of_ciphertext.append(decoded_ciphertext_block)

    # CONCATENATE CIPHERTEXT
    ciphertext = "".join(list_of_ciphertext)

    list_of_decryptions = []
    # TEST DECRYPTION AND DECODING
    for i in range(len(list_of_ciphertext_bits)):
        decrypted_encryption = decrypt_fiestel_rounds(list_of_ciphertext_bits[i], encoded_secret_key)
        group_decryptedtext = byte_grouping(decrypted_encryption)
        decoded_decrypted_block = ascii_decoding(group_decryptedtext)
        list_of_decryptions.append(decoded_decrypted_block)
    decrypted_ciphertext = "".join(list_of_decryptions)

    return ciphertext, decrypted_ciphertext, new_message, warning


def main():
    secret_key = input("Please enter a secret key (must be 8 characters long): ")
    if len(secret_key)!=8:
        print("Sorry the secret key size can only be 8 characters in length, try again.")
    else:
        message = input("Please enter a message you wish to encrypt: ")

        ciphertext, decrypted_ciphertext, new_message, warning = mode_of_operation(message, secret_key)

        print("\n",warning)
        print("/////////////////////////////////////////////////////////////////////////////////////////")
        print(new_message,"\n")
        print(f"Your message after encryption: {ciphertext}")
        print("/////////////////////////////////////////////////////////////////////////////////////////")
        print(f"Your message after decryption {decrypted_ciphertext}\n")

if __name__ == "__main__":
    main()