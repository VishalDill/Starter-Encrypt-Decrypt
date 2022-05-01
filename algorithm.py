import os
import random
#import Tkinter

# Created by Vishal Dillibabu, Shyan Vilvarajah and Rabten Tsering.

def encrypt_algorithm(lst):

    lst.pop()

    # encrypt_algorithm process with algorithm
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
    encrypted_file.close()
    os.unlink("encrypt_algorithm_Initialization.txt")

    # ADDING NEW KEYS AND VALS TO PASSWORD FILE

    if given_file != "Passwords.txt":
        key_dict = decrypt_checker()
        decrypt("Passwords.txt")
        append_file = open("Passwords.txt", "a")

        password = ""
        for i in range(10):
            password += str(random.randrange(0, 10))

        while password in key_dict.values():
            password = ""
            for i in range(10):
                password += str(random.randrange(0, 10))

        entry = f"{given_file}:{password}\n"
        append_file.write(entry)

        append_file.close()
        encrypt("Passwords.txt")
        return password
    else:
        return None

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

    # REMOVE THE DECRYPTED FILE FROM PASSWORDS FILE
    if file != "Passwords.txt":
        decrypt("Passwords.txt")
        in_file = open("Passwords.txt", "r")
        place_holder = open("Place holder.txt", "w")

        # IF THE CURRENT LINE IS THE FILE WE ARE DECRYPTING, IT DOESN'T GET COPIED TO THE   NEW PASSWORDS MASTER LIST
        for line in in_file:
            if line[0 : line.find(":")] != file:
                place_holder.write(line)

        in_file.close()
        place_holder.close()
        place_holder = open("Place holder.txt", "r")
        in_file = open("Passwords.txt", "w")

        for line in place_holder:
            in_file.write(line)

        in_file.close()
        place_holder.close()
        os.unlink("Place holder.txt")
        encrypt("Passwords.txt")


def encrypt_checker(given_file):
    key_dict = decrypt_checker()
    if given_file not in key_dict:
        return True
    else:
        return False


def decrypt_checker():
    decrypt("Passwords.txt")
    key_file = open("Passwords.txt", "r")
    key_dict = {}
    for line in key_file:
        dict_key = ""
        dict_value = ""
        colon_flag = False
        for char in line:
            if char == ":":
                colon_flag = True
            elif colon_flag is False:
                dict_key += char
            elif char == "\n":
                break
            else:
                dict_value += char
        key_dict[dict_key] = dict_value
    key_file.close()
    encrypt("Passwords.txt")
    return key_dict
