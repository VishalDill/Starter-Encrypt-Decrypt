import os
import random

# Created by Vishal Dillibabu, Shyan Vilvarajah, Rabten Tsering

main_key = "potato"
def encrypt_algorithm(lst):

    lst.pop()

    # encrypt_algorithm process with algortihim
    s_is = []
    s_i = 0
    l_is = []
    l_i = len(lst) - 1

    for i in range(len(lst)):
        if s_i == l_i:
            break

        elif l_i not in s_is and s_i not in l_is and l_i > s_i and s_i < l_i:
            lst[s_i], lst[l_i] = lst[l_i], lst[s_i]
            s_is.append(s_i)
            l_is.append(l_i)

        else:
            break
        s_i += 2
        l_i -= 2

    lst.reverse()
    lst.append(10)


def decrypt_algorithm(lst):

    # decrypt_algorithm process with same algorithm
    lst.pop()
    lst.reverse()
    s_is = []
    s_i = 0
    l_is = []
    l_i = len(lst) - 1

    for i in range(len(lst)):

        if s_i == l_i:
            break

        elif l_i not in s_is and s_i not in l_is and l_i > s_i and s_i < l_i:
            lst[s_i], lst[l_i] = lst[l_i], lst[s_i]
            s_is.append(s_i)
            l_is.append(l_i)

        else:
            break
        s_i += 2
        l_i -= 2

    lst.append(10)


def encrypt(given_file):
    original_file = open(given_file,"rb")
    # CREATING A NEW ENCRYPTED FILE
    encrypted_file = open("encrypt_algorithm_Initialization.txt", "wb+")

    for line in original_file:
        lst = []
        for b in line:
            # append each byte in the line to list.
            lst.append(b)

            # print(bytes(lst))  # will look like [100, 145, 133, 200, 10] .
        # with each integer representing a byte.

        # this will pop 10 which is a byte that represents new line.
        encrypt_algorithm(lst)

        encrypted_file.write(bytes(lst))

    original_file.close()
    encrypted_file.close()

    # APPLYING encrypt_algorithm TO ORIGINAL FILE
    original_file = open(given_file, "wb+")
    encrypted_file = open("encrypt_algorithm_Initialization.txt", "rb")

    for line in encrypted_file:
        original_file.write(line)

    original_file.close()
    os.unlink("encrypt_algorithm_Initialization.txt")



def decrypt(file):
    encrypted_file = open(file, "rb")
    # CREATING A NEW DECRYPTED FILE
    dec_file = open("Decrypted_file.txt", "wb+")

    for new_line in encrypted_file:
        lst = []
        for b in new_line:
            # append each byte in the line to list.
            lst.append(b)

            # print(bytes(lst))  # will look like [100, 145, 133, 200, 10] .
            # with each integer representing a byte.

            # this will pop 10 which is a byte that represents new line.


        decrypt_algorithm(lst)
        dec_file.write(bytes(lst))

    encrypted_file.close()
    dec_file.close()
    encrypted_file = open(file, "wb+")
    dec_file = open("Decrypted_file.txt", "rb")

    for line in dec_file:
        encrypted_file.write(line)

    encrypted_file.close()
    dec_file.close()
    os.unlink("Decrypted_file.txt")

if __name__ == "__main__":
    option = input("Enter E to encrypt or D to decrypt: ")
    while option != "D" and option != "E":
        option = input("Please enter a valid input E for encryption or D for decryption: ")

    if option == "E":
        while True:
            try:
                file = input("Please enter file: ")
                break
            except FileNotFoundError:
                print("ERROR File not found")

        #Open the file to be encrypted
        encrypt(file)

    else:
        while True:
            try:
                file = input("Please enter file: ")
                break
            except FileNotFoundError:
                print("ERROR File not found")

        decrypt(file)
