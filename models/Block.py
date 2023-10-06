from ConnectDB import ConnectDB
from datetime import datetime
from Digest import digest
import colorama

colorama.init(autoreset=True)

class Block:
    BlockDBManipulator = ConnectDB()
    currentStudentId = None
    
    def remove(**kwargs):
        Block.BlockDBManipulator.remove("Blocks",**kwargs)
    
    def getLastCurrentHash():
        lastTuple = Block.BlockDBManipulator.getMostlyRecentAdded("Blocks")
        if lastTuple == None:
            return None
        else:
            return lastTuple[2]
    
    def __init__(self, vote: str, studentId: str) -> None:
        previousHash = Block.getLastCurrentHash()
        if previousHash == None:
        
            try:
                with open("Initial_Block_Config","r") as f:
                    initialBlockConfig = {}
                    lines = f.read().splitlines()
                    for line in lines:
                        dkey, dvalue = line.split("=")
                        initialBlockConfig.update({dkey: dvalue})
                    Block.BlockDBManipulator.insert("Blocks",**initialBlockConfig)


                    previousHash = initialBlockConfig['currentHash']
            
            except FileNotFoundError:
                exit(colorama.Back.RED+"arquivo 'Initial_Block_Config' não existe!!")
        
        Block.currentStudentId = studentId #Não inserido no BD

        self.vote        = vote
        self.time        = datetime.now().__str__()
        self.currentHash = digest(vote+studentId+self.time+previousHash)

    def insert(self):
        Block.BlockDBManipulator.insert("Blocks",**self.__dict__)
        id = Block.BlockDBManipulator.getMostlyRecentAdded("Blocks")[0]
        with open("studentsId_Mapping", "a") as f:
            f.write(f"{id}={Block.currentStudentId}\n")

a = Block("10","id001")
a.insert()
b = Block("20","id002")
b.insert()
c = Block("30","id003")
c.insert()
