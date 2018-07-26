from Crypto.Cipher import AES

KEY = b'86bd8a144720b6b0650cbde99a0db485'  # 16-ти байтный ключ.

class CryptAes:
    """
    Класс для шифрования сообщений по алгоритму AES.
    """
    def encrypt(self, message):
        obj = AES.new('KEY', AES.MODE_CBC, '666')
        ciphertext = obj.encrypt(message)
        return ciphertext

    def decrypt(self, raw_string_crypt):
        obj2 = AES.new('KEY', AES.MODE_CBC, '666')
        raw_string = obj2.decrypt(raw_string_crypt)
        return raw_string
