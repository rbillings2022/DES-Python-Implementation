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
