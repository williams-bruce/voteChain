from pathlib import Path
from ConnectDB import ConnectDB
from datetime import datetime
from Digest import digest
import colorama

colorama.init(autoreset=True)

class Block:
    '''
    Classe que representa o Bloco em uma blockchain e cada voto.
    Toda vez que um objeto bloco é instanciado, é feito um registro no banco de dados com os dados da transação.
    No construtor é usado todos os métodos da classe Block.
    Instancia o Block e adiciona no banco de dados usando o currentHash anterior.
    Se não há Block anterior, então é usado Initial_Block_Config para gerar o primeiro Block do banco de dados.
    
    Args:
        vote (str): String do voto para gerar o Block.
        studentId (str): Identificador do aluno que votou.
    
    Attributes:
        vote (str): A String do voto, representa em quem foi votado.
        time (str): String que mostra quando o objeto foi instanciado.
        currentHash (str): String que representa o hash da transação.

    Examples:
        >>> from Block import Block
        >>> block = Block("example_vote","example_studentId")

    '''

    BlockDBManipulator = ConnectDB()
    '''
    BlockDBManipulator (models.ConnectDB): Parâmetro estático que gerencia os acessos ao banco de dados.
        
    See Also:
        - :ref:`models-connectdb-label`
    '''

    currentStudentId = None
    '''
    currentStudentId (None): Tem valor de inicialização None mas recebe a str studentId durante a execução do construtor e é usado para gerar o currentHash, no final do construtor recebe o valor None novamente.
    '''
    
    def remove(**kwargs):
        '''
        Método estático que remove um bloco do banco de dados.

        Args:
            **kwargs: é passado para Block.BlockDBManipulator.remove().

        See Also:
            - :ref:`models-connectdb-label`
        '''
        Block.BlockDBManipulator.remove("Blocks",**kwargs)
    
    def getLastCurrentHash():
        '''
        Método estático que pega o último currentHash no banco de dados. usa Block.BlockDBManipulator.getMostlyRecentAdded().

        See Also:
            - :ref:`models-connectdb-label`
        '''
        lastTuple = Block.BlockDBManipulator.getMostlyRecentAdded("Blocks")
        if lastTuple == None:
            return None
        else:
            return lastTuple[2]
    
    def insert(self):
        '''
        Método que insere o bloco no banco de dados. Usado automaticamente no construtor.
        '''
        Block.BlockDBManipulator.insert("Blocks",**self.__dict__)
        id = Block.BlockDBManipulator.getMostlyRecentAdded("Blocks")[0]
        with open("studentsId_Mapping", "a") as f:
            f.write(f"{id}={Block.currentStudentId}\n")

    def __init__(self, vote: str, studentId: str) -> None:    
        previousHash = Block.getLastCurrentHash()
        if previousHash == None:
        
            try:
                with open(str(Path(__file__).parent)+"/"+"Initial_Block_Config","r") as f:
                    initialBlockConfig = {}
                    lines = f.read().splitlines()
                    for line in lines:
                        dkey, dvalue = line.split("=")
                        initialBlockConfig.update({dkey: dvalue})
                    Block.BlockDBManipulator.insert("Blocks",**initialBlockConfig)


                    previousHash = initialBlockConfig['currentHash']
            
            except FileNotFoundError:
                print(colorama.Back.RED+"arquivo 'Initial_Block_Config' não existe!!")
        
        Block.currentStudentId = studentId #Não inserido no BD

        self.vote        = vote
        self.time        = datetime.now().__str__()
        self.currentHash = digest(vote+studentId+self.time+previousHash)

        self.insert()

        self.currentStudentId = None
