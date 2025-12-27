def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return 'El número clave debe ser un número entero.'

    if shift < 1 or shift > 25:
        return 'El número debe ser entre 1 y 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text

def encrypt(text, shift):
    return caesar(text, shift)
    
    
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)

entrada=input ("Hola, para cifrar un texto pulse c, para descifrar pulse d :")

if entrada == "c":
    text = input ("Ingresa el texto a cifrar :").lower()
    shift = int (input("Ingresa el número clave para cifrar :"))
    print (encrypt(text, shift))
    
    
elif entrada == "d":
    text = input ("Ingresa el texto a descifrar :").lower()
    shift = int (input("Ingresa el número clave para descifrar :"))
    print (decrypt (text, shift))
else:
    print("Elige solo entre la opcion 'c' o 'd' :")

