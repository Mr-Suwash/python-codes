alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction=input("Type encode to encrypt and decode to decrypt ")
inputs=input("enter the text ").lower()

Shift_value=int(input("Enter the position to be shifted "))

def caeser(start_text, shift_positions, cipher_direction):
    end_text=""
    for letter in start_text:
       position=alphabets.index(letter) 
       if(direction=="decode"):
           shift_positions*=-1
       new_position=position+shift_positions
       new_letter=alphabets[new_position]
       end_text+=new_letter
    print(f"The {cipher_direction}d text is {end_text}")

caeser(start_text=inputs, shift_positions=Shift_value, cipher_direction=direction)

