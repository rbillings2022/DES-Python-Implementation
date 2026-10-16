from . import des_cipher
from formatting import binary_format
from formatting import list_construct
import re

def electronic_codebook(message:str, secret_key:str):
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
    encoded_plaintext = binary_format.encoding(message)
    encoded_secret_key = binary_format.encoding(secret_key)

    for i in range(0, len(encoded_plaintext), 64):
        block = []
        for j in range(i, 64+i):
            block.append(encoded_plaintext[j])
        list_of_DES_blocks.append(block)

    list_of_ciphertext = []
    list_of_ciphertext_bits = []
    # TEST DES ENCRYPTION BY FEEDING THE BITS TO THE FEISTEL ROUNDS FUNCTION
    for i in range(len(list_of_DES_blocks)):
        encrypted_text = des_cipher.encrypt_fiestel_rounds(list_of_DES_blocks[i], encoded_secret_key)
        list_of_ciphertext_bits.append(encrypted_text)

        # Decode each block of ciphertext then append eack block to a list
        group_ciphertext = list_construct.byte_grouping(encrypted_text)
        decoded_ciphertext_block = binary_format.decoding(group_ciphertext)
        list_of_ciphertext.append(decoded_ciphertext_block)

    # CONCATENATE CIPHERTEXT
    ciphertext = "".join(list_of_ciphertext)

    list_of_decryptions = []

    # TEST DECRYPTION AND DECODING
    for i in range(len(list_of_ciphertext_bits)):
        decrypted_encryption = des_cipher.decrypt_fiestel_rounds(list_of_ciphertext_bits[i], encoded_secret_key)
        group_decryptedtext = list_construct.byte_grouping(decrypted_encryption)
        decoded_decrypted_block = binary_format.decoding(group_decryptedtext)
        list_of_decryptions.append(decoded_decrypted_block)
    decrypted_ciphertext = "".join(list_of_decryptions)

    decrypted_ciphertext = re.sub(r"[^a-zA-Z ]","", decrypted_ciphertext)

    return ciphertext, decrypted_ciphertext, new_message, warning
