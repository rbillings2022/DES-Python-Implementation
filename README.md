# DES-Python-Implementation
## Description
This is a toy simulation of DES. It has it's own encoding scheme that covers 256 symbols. The encoding scheme map letters and symbols to an 8-bit binary code flatten as a string. The bits/bytes each will be programmically manipulated as a list data structure to perform operations such as XOR and permutations. Creating an encoding scheme will help visually understand what's going on under the hood when bits are rearranged during DES permutations.

### Warning
Since this a toy implementation, the 8 bits removed during permuted choice 2 are not stored or used anywhere, they're just discarded. 
## DES encryption Architecture
<img width="2301" height="3099" alt="Cryptography Cipher architecture" src="https://github.com/user-attachments/assets/7480d65f-df08-4044-a25f-47241702dc76" />
