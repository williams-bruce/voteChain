from hashlib import sha256
import sys

def digest(stringToHash: str) -> str:
    """
    Esta é uma descrição da função.
    
    Args:
        parametro (tipo): Descrição do parâmetro.
    
    Returns:
        tipo_de_retorno: Descrição do que a função retorna.
    """
    hashBytes = sha256(stringToHash.encode())
    return hashBytes.hexdigest()

if __name__ == "__main__":
    for args in sys.argv[1:]:
        print(digest(args))