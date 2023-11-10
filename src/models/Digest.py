from hashlib import sha256
import sys

def digest(stringToHash: str) -> str:
    
    """
    Função que gera o hash (SHA256) a partir de uma string.

    Args:
        stringToHash (str): String a partir da qual será gerado seu hash (SHA256).

    Returns:
        str: Retorna uma string de caracteres hexadecimal, o hash (SHA256).
   
    Examples:
        >>> from Digest import digest
        >>> print(digest("ola_mundo"))
        fb1d6b9f693828ea898bed8c7d955b0f1d8327bc2fd1c2920b5439ccdc76071f
    """

    hashBytes = sha256(stringToHash.encode())
    return hashBytes.hexdigest()

if __name__ == "__main__":
    for args in sys.argv[1:]:
        print(digest(args))