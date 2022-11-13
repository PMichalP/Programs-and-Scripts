ALPHABET_TABLE = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                  "m", "n", "o", "p", "r", "s", "t", "u", "w", "v", "x", "y", "z"]

print("This is Script to cipher text using Cesar cipher")
text_to_cipher = input("Provide text to cipher: ")
cipher_value = int(input("Provide cipher value: "))
ciphered_text = ""

for character_to_cipher in text_to_cipher:
    if (character_to_cipher != " "):
        index_of_character_in_dictionary = 0

        for character_from_alphabet_table in ALPHABET_TABLE:
            if (character_to_cipher == character_from_alphabet_table):
                new_character_index = index_of_character_in_dictionary + cipher_value

                if (new_character_index >= 25):
                    new_character_index = new_character_index - 25
                ciphered_text = ciphered_text + \
                    ALPHABET_TABLE[new_character_index]

            index_of_character_in_dictionary = index_of_character_in_dictionary + 1
    else:
        ciphered_text = ciphered_text + " "

print(text_to_cipher)
print(ciphered_text)
