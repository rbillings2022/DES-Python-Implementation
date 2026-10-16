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
