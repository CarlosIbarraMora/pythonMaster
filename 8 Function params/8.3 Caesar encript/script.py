letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    else:
        print("Invalid option")
    for char in start_text:
        if char in letters:
            position = letters.index(char)
            new_position = position + shift_amount
            if new_position > 25:
                new_position -= 26
            end_text += letters[new_position]
        else:
            end_text += char
    print(f"The text is {end_text}")
    


text = input("Type your message:\n").upper()
shift = int(input("Type the shift number:\n"))
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
caesar(text,shift,direction)