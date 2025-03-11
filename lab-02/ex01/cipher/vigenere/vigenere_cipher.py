class VigenereCipher:
    def __init__(self):
        pass

    def vigenere_encrypt(self, plain_text: str, key: str) -> str:  # Sửa typo: encrpyt -> encrypt
        if not isinstance(plain_text, str) or not isinstance(key, str):
            raise TypeError("plain_text and key must be strings")
        if not key:
            raise ValueError("Key cannot be empty")
        
        encrypt_text = ""
        key_index = 0
        for char in plain_text:
            if char.isalpha():
                key_shift = ord(key[key_index % len(key)].upper()) - ord('A')
                if char.isupper():
                    encrypt_text += chr((ord(char) - ord('A') + key_shift) % 26 + ord('A'))
                else:
                    encrypt_text += chr((ord(char) - ord('a') + key_shift) % 26 + ord('a'))
                key_index += 1  # Tăng key_index cho ký tự chữ cái
            else:
                encrypt_text += char  # Giữ nguyên ký tự không phải chữ cái
        return encrypt_text

    def vigenere_decrypt(self, encrypt_text: str, key: str) -> str:
        if not isinstance(encrypt_text, str) or not isinstance(key, str):
            raise TypeError("encrypt_text and key must be strings")
        if not key:
            raise ValueError("Key cannot be empty")
        
        decrypt_text = ""
        key_index = 0
        for char in encrypt_text:
            if char.isalpha():
                key_shift = ord(key[key_index % len(key)].upper()) - ord('A')
                if char.isupper():
                    decrypt_text += chr((ord(char) - ord('A') - key_shift) % 26 + ord('A'))
                else:
                    decrypt_text += chr((ord(char) - ord('a') - key_shift) % 26 + ord('a'))
                key_index += 1  # Sửa lỗi thụt lề: tăng key_index ở đây
            else:
                decrypt_text += char  # Giữ nguyên ký tự không phải chữ cái
        return decrypt_text