def Crypto(*args):
    """La funcion Crypto recibe una cadena de texto y mediante el encriptado Cesar, le otorga
    un desplazamiento dado para devolver un mensaje encriptado"""
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    mov = 5
    text = input("Introduce texto a encriptar: ")
    text = text.lower()
    text_crypt = ""

    for i in text:
        place = alphabet.index(i)
        if place+mov > 26:
            text_crypt = text_crypt+alphabet[place+mov-26]
        else:
            text_crypt = text_crypt+alphabet[place+mov]
    print(text_crypt)
    return text_crypt

def Decrypt(*args):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z' ]
    mov = 5
    text = input("Introduce texto a desencriptar: ")
    text = text.lower()
    text_decrypt = ""

    for i in text:
        place = alphabet.index(i)
        if place+mov > 26:
            text_decrypt = text_decrypt+alphabet[place-mov-26]
        else:
            text_decrypt = text_decrypt+alphabet[place-mov]
    print(text_decrypt)
    return text_decrypt
