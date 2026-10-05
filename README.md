# DES Python Cryptographic Implementation
## Description
This is a toy simulation of DES. It has it's own encoding scheme that covers 256 symbols. The encoding scheme map letters and symbols to an 8-bit binary code flatten as a string. The bits/bytes each will be programmically manipulated as a list data structure to perform operations such as XOR and permutations. Creating an encoding scheme will help visually understand what's going on under the hood when bits are rearranged during DES permutations.

### Warning
Since this a toy implementation, the 8 bits removed during permuted choice 1 are not stored or used anywhere, they're just discarded. 

## Purpose
This is an Educational implementation of DES using ECB mode and a custom encoding scheme.

## Design
- ECG partition messages into 64-bit block size
- 56-bit effective key
- Using 16 Feistel rounds for each block
- Initial and Inverse permutation 8x8
- Key scheduling and 48-bit subkey generation
- Expansion premutation
- Sub-Box

## Security limitations of this implementation
- Vulnerable to side channel attacks due to if-else statements
- Effective key is only 56-bits, it can easily be brute force guessed
- Vulnerable to leaking encryption patterns, if certain words or letters repeat in the ciphertext, that pattern is obvious. This can lead to the plaintext being predicted

## High-level Architecture
- Message is encoded, each character represent 8-bits
- ECB partition message into 64-bit block
- Each block feeds 64-bit block into DES function
- Key schedule function generates 16, 48-bit subkeys
- Feistel function  splits 64-bits into Left and Right
- Next Left stores the previous Right bits
- Right executes a layer of functions
  1. Previous Right is expanded to 48-bits
  2. Then XORed by the subkey
  3. Compressed by the Sub-boxes
  4. Permutation applied
  5. XORed by previous left
- Feistel Repeats for 16 rounds
- Finally Inverse permutation is applied.
## Tests
- TO BE DECIDED
## DES encryption Architecture
<img width="2301" height="3099" alt="Cryptography Cipher architecture" src="https://github.com/user-attachments/assets/844dcd34-f4c3-4b6a-b627-6007be4b704b" />

## DES ECB Mode Architecture
<img width="1920" height="1080" alt="ECB Mode" src="https://github.com/user-attachments/assets/ee6e9999-720c-4ec5-b220-66f07e06e8d5" />



