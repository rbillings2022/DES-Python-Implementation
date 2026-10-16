from des import modes

def main():
    # secret_key = input("Please enter a secret key (must be 8 characters long): ")
    secret_key = "Tghsdgsh"
    if len(secret_key)!=8:
        print("Sorry the secret key size can only be 8 characters in length, try again.")
    else:
        # message = input("Please enter a message you wish to encrypt: ")
        message = "Hi there I am bob and bob is "

        ciphertext, decrypted_ciphertext, new_message, warning = modes.electronic_codebook(message, secret_key)

        print("\n",warning)
        print("/////////////////////////////////////////////////////////////////////////////////////////")
        print(f"Your message: {message}\n")
        print(new_message,"\n")
        print(f"Your message after encryption: {ciphertext}")
        print("/////////////////////////////////////////////////////////////////////////////////////////")
        print(f"Your message after decryption {decrypted_ciphertext}\n")

if __name__ == "__main__":
    main()
