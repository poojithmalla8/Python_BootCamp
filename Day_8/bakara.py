alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 


#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
def caesar(text,shift,direction):
    if direction == 'encode':
        cipher_text=""
        for letter in text:
            updated_shifter=alphabet.index(letter)+shift
            if updated_shifter<len(alphabet):
                cipher_text+=alphabet[updated_shifter]
            if updated_shifter>len(alphabet):
                updated_shifter_2=updated_shifter-len(alphabet)
                cipher_text+=alphabet[updated_shifter_2]
        print(cipher_text)
        
    elif  direction=='decode':
        original_text=""
        for letter in text:
            new_shifter=alphabet.index(letter)-shift
            original_text=original_text+alphabet[new_shifter]
        print(original_text)
      

caesar(text=text,shift=shift,direction=direction)