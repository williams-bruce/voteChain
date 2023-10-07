from ConnectDB import ConnectDB

def generateTables():
    '''
    Função que cria as tabelas do Banco de dados.
    
    See Also:
        - :ref:`models-connectdb-label`
    '''
    condb = ConnectDB()

    blocksTable = "CREATE TABLE `Blocks` (\
        `id` int(11) NOT NULL AUTO_INCREMENT,\
        `vote` varchar(8) NOT NULL,\
        `currentHash` varchar(255) NOT NULL,\
        `time` varchar(100) NOT NULL,\
        PRIMARY KEY (`id`)\
        ) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;"
    
    candidatosTable = "CREATE TABLE `candidatos` (\
        `codigo` varchar(10) NOT NULL,\
        `nome` varchar(255) NOT NULL,\
        `partido` varchar(255) NOT NULL,\
        `time` timestamp NOT NULL DEFAULT current_timestamp(),\
        PRIMARY KEY (`codigo`)\
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;"
    
    eleitoresTable = "CREATE TABLE `eleitores` (\
        `codigo` varchar(10) NOT NULL,\
        `nome` varchar(255) NOT NULL,\
        `time` timestamp NOT NULL DEFAULT current_timestamp(),\
        PRIMARY KEY (`codigo`)\
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;"
    
    condb.queryRaw(blocksTable)
    condb.queryRaw(candidatosTable)
    condb.queryRaw(eleitoresTable)

if __name__ == "__main__":
    generateTables()