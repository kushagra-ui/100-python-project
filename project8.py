logo = ''' ██████╗ █████╗ ███████╗███████╗ █████╗ ██████╗      ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗ 
██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗    ██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗
██║     ███████║█████╗  ███████╗███████║██████╔╝    ██║     ██║██████╔╝███████║█████╗  ██████╔╝
██║     ██╔══██║██╔══╝  ╚════██║██╔══██║██╔══██╗    ██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗
╚██████╗██║  ██║███████╗███████║██║  ██║██║  ██║    ╚██████╗██║██║     ██║  ██║███████╗██║  ██║
 ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝     ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                               '''
 
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encode and 'decode' to decrypt : \n ").lower()
text= input("type your meassage : \n ").lower()
shift= int(input("type the shift number: \n "))


def caesar(original_text, shift_amount, encode_or_decode):
    output_text=""
    if encode_or_decode== "decode":
             shift_amount *= -1 

    for  letter in original_text:
       if letter not in alphabet:
           output_text += letter
       else:   
        
        shifted_position= alphabet.index(letter) + shift_amount
        shifted_position%= len(alphabet)
        output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result : {output_text}")

caesar(original_text= text, shift_amount= shift , encode_or_decode= direction)
should_continue = False
while should_continue:
    direction = input("Type 'encode' to encode and 'decode' to decrypt : \n ").lower()
    text= input("type your meassage : \n ").lower()
    shift= int(input("type the shift number: \n "))


restart = input(" Type 'yes'if you want to go again otherwise type 'no' \n ").lower() 
if restart == "no":
    should_continue = False
    print("GoodBye!")
   
   
   
    

