from . import permutation_tables
from formatting import binary_format

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
        subkey = permutation_tables.permuted_choice2(c+d)

        subkey_list.append(subkey)
    return subkey_list

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
        row = binary_format.two_bit_decoding("".join(list_of_six_bits[i][:1]+list_of_six_bits[i][5:]))
        column = binary_format.four_bit_number_decoding("".join(list_of_six_bits[i][1:5]))

        four_bit_value = binary_format.four_bit_number_encoding(sbox[i][row][column])
        four_bit_list.append(four_bit_value)

        four_bit_list = list("".join(four_bit_list))
    return four_bit_list

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
    plaintext_ip = permutation_tables.intitial_permutation(plaintext)
    # Key Generation Functions
    effecive_key = permutation_tables.permuted_choice1(masterkey)
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
        expended = permutation_tables.expansion_table(right)

        # f(right, subkey): XOR previous Right bits with the subkey
            # XOR each bit and append the resulting bit to the f_out list
        expanded_right = []
        for c in range(48):
            expanded_right.append(xor(expended[c], subkeys_list[r][c]))

        compress_right = s_box_function(expanded_right)

        permuted_right = permutation_tables.p_permutation(compress_right)
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
    feistel_inverse_perm = permutation_tables.inverse_IP(left+right)

    # Return encrypted bits
    return feistel_inverse_perm


def decrypt_fiestel_rounds(ciphertext:list, masterkey:list) -> list:
    plaintext_ip = permutation_tables.intitial_permutation(ciphertext)
    # Key Generation Functions
    effecive_key = permutation_tables.permuted_choice1(masterkey)
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
        expended = permutation_tables.expansion_table(right)

        # f(right, subkey): XOR previous Right bits with the subkey
            # XOR each bit and append the resulting bit to the f_out list
        expanded_right = []
        for c in range(48):
            expanded_right.append(xor(expended[c], subkeys_list[r][c]))

        compress_right = s_box_function(expanded_right)

        permuted_right = permutation_tables.p_permutation(compress_right)
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
    decrypted_f_inverse_perm = permutation_tables.inverse_IP(left+right)

    # Return encrypted bits
    return decrypted_f_inverse_perm
