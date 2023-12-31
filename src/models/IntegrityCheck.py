from pathlib import Path
from ConnectDB import ConnectDB
from Digest import digest
import colorama

colorama.init(autoreset=True)

def integrityCheck():
    '''
    Função que verifica a integridade de cadeia de Blocks no banco de dados

    Returns:
        bool: Retorna um bool que nos informa se a cadeia de Blocks é integra ou não

    Examples:
        >>> from IntegrityCheck import integrityCheck
        >>> integrityCheck()
        True
    
    See Also:
        - :ref:`models-block-label`
        - :ref:`models-connectdb-label`
    
    '''
    condb = ConnectDB()

    chain = condb.getAllAdded("Blocks")

    previousHash = chain[0][2]

    chain = chain[1:]

    eidToStudentsId = {}

    try:
        with open(str(Path(__file__).parent)+"/"+"studentsId_Mapping","r") as f:
            for line in f.read().splitlines():
                dkey, dvalue = line.split("=")
                eidToStudentsId.update({int(dkey): dvalue})
    
    except FileNotFoundError:
        print(colorama.Back.RED+"arquivo 'studentsId_Mapping' não existe!!")

    for block in chain:
        eid, vote, currentHash, time = block
        if currentHash == digest(vote+eidToStudentsId[eid]+time+previousHash):
            previousHash = currentHash
        else:
            return False
    
    return True

if __name__ == "__main__":
    print(integrityCheck())