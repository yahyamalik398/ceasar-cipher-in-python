from ascii import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', \
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']  
list=['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i',\
       'h','g','f','e','d','c','b','a']
direction= input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text=input("Type your message:\n").lower()
shift= int(input("Type the shift number:\n"))
def encryption(plain_text, shift_number):
  cipher_text=""
  for letter in plain_text:
    position= alphabet.index(letter)
    new_position= position+shift_number
    if (new_position>26):
      extra= new_position-26
      new_letter= alphabet[extra]
    else:
     new_letter= alphabet[new_position]
    cipher_text+=new_letter
  print(f"The encoded text is {cipher_text}")
def decrypt(cipher_text, shift_number):
 decrypted_text=""
 for letter in cipher_text:
   position= alphabet.index(letter)
   new_position=position-shift_number
   extra= -(new_position)
   if new_position<1:
     new_letter= list[extra-1]
   else:
     new_letter=alphabet[new_position]
   decrypted_text+=new_letter
 print(f"the decoded text is {decrypted_text}")

def ceasar(type, shifting, message):
 if direction=="encode":
  encryption(plain_text=message, shift_number=shifting)
 elif direction=="decode":
  decrypt(cipher_text=message, shift_number=shifting)
ceasar(type=direction, shifting=shift, message=text )


