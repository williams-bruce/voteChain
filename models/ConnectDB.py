from pathlib import Path
import mysql.connector
import colorama

colorama.init(autoreset=True)

class ConnectDB:
    '''
    Classe que faz os acessos, inserção e remoção no banco de dados. Precisa do arquivo Credentials do usuário para acessar o banco de dados.

    Attributes:
        connection (mysql.connector.connection_cext.CMySQLConnection): Conexão com o banco de dados.
        cursor (mysql.connector.connection_cext.CMySQLCursor): Cursor da conexão com o banco de dados.
    '''
    def __init__(self) -> None:
        credentials = {}

        try:
            with open(str(Path(__file__).parent)+"/"+"Credentials","r") as f:
                lines = f.read().splitlines()
                for line in lines:
                    dkey, dvalue = line.split("=")
                    credentials.update({dkey: dvalue})
        except FileNotFoundError:
            print(colorama.Back.RED+"arquivo 'Credentials' não existe!!")

        self.connection = mysql.connector.connect(**credentials)

        self.cursor = self.connection.cursor()

    def queryRaw(self, query: str, dataTuple=None):
        '''
        Método que passa uma query diretamente, sem tratamentos.

        Args:
            query (str): Uma String que reprensenta a query.
            dataTuple (None, tuple): A informção complementar para query se necessário. Nesse método é usado self.cursor.execute().
        '''
        self.cursor.execute(query, dataTuple)
        self.connection.commit()

    def insert(self, table, **kwargs):
        '''
        Método que adiciona dados em uma tabela. *Informação importante* ao passar os kwargs, deve-se passar como chave todas as colunas nas quais os dados podem ser inseridos, e os valores é o que será adicionado.

        Args:
            table (str): String que represta a tabela nos quais os dados vão ser adicionados.
            **kwargs: chaves reprensentam colunas e os valores dessas chaves os valores adicionados.
        
        Examples:
            >>> from ConnectDB import ConnectDB
            >>> condb = ConnectDB()
            >>> condb.insert("Blocks",vote="example1",currentHash="example2",time="example3")
            ### Não pode-se esquecer de adicionar todas as colunas que podem ser modificadas.
        '''
        if kwargs.__len__() > 0:
            query = f"INSERT INTO {table} ("
            for keyName in kwargs:
                query += keyName+","
            query = query[:-1] + ") VALUES ("
            
            for i in range(kwargs.__len__()):
                query += "%s,"
            query = query[:-1] + ");"
        else:
            print("Precisa de kwargs para fucionar")

        self.cursor.execute(query,tuple(kwargs.values()))
        self.connection.commit()

    def remove(self, table, **kwargs):
        '''
        Método que remove dados em uma tabela. *Informação importante* Não é igual ao insert(), basta passar algumas colunas.

        Args:
            table (str): String que represta a tabela nos quais os dados vão ser retirados.
            **kwargs: chaves reprensentam colunas e os valores dessas chaves os valores adicionados.
        
        Examples:
            >>> from ConnectDB import ConnectDB
            >>> condb = ConnectDB()
            >>> condb.remove("Blocks",vote="example1",currentHash="example2",time="example3")
            ### Assim remove o(s) Block(s) que tem vote="example1" AND currentHash="example2" AND time="example3"
            >>> condb.remove("Blocks",vote="example1",currentHash="example2")
            ### Assim remove o(s) Block(s) que tem vote="example1" AND currentHash="example2"
            >>> condb.remove("Blocks",vote="example1",currentHash="example2",time="example3")
            ### Assim remove o(s) Block(s) que tem vote="example1"
        '''
        if kwargs.__len__() > 0:
            query = f"DELETE FROM {table} WHERE "
            for keyName in kwargs:
                query += f"{keyName}=%s AND "
            query = query[:-5] + ";"
            
            self.cursor.execute(query,tuple(kwargs.values()))
            self.connection.commit()

        else:
            print("Precisa de kwargs para fucionar")

    def search(self, table, **kwargs):
        '''
        Método que busca dados em uma tabela. *Informação importante* Não é igual ao insert(), basta passar algumas colunas.

        Args:
            table (str): String que represta a tabela nos quais os dados vão ser retirados.
            **kwargs: chaves reprensentam colunas e os valores dessas chaves os valores adicionados.
        
        Returns:
            (list): Retorna uma lista de tupla com os resultados.

        Examples:
            >>> from ConnectDB import ConnectDB
            >>> condb = ConnectDB()
            >>> condb.search("Blocks",vote="example1",currentHash="example2",time="example3")
            ### Assim retorna o(s) Block(s) que tem vote="example1" AND currentHash="example2" AND time="example3"
            >>> condb.search("Blocks",vote="example1",currentHash="example2")
            ### Assim retorna o(s) Block(s) que tem vote="example1" AND currentHash="example2"
            >>> condb.search("Blocks",vote="example1",currentHash="example2",time="example3")
            ### Assim retorna o(s) Block(s) que tem vote="example1"
        '''
        if kwargs.__len__() > 0:
            query = f"SELECT * FROM {table} WHERE "
            for keyName in kwargs:
                query += f"{keyName}=%s AND "
            query = query[:-5] + ";"
            
            self.cursor.execute(query,tuple(kwargs.values()))
            #self.connection.commit()

            return self.cursor.fetchall()

        else:
            print("Precisa de kwargs para fucionar")
            return False

    def getAllAdded(self,table):
        '''
        Método que retorna uma lista de todas as tuplas adicionadas ordenadas pela coluna time. A tabela deve ter coluna 'time'.

        Args:
            table (str): String que representa a tabela da qual as tuplas vão ser retiradas.

        Returns:
            (list): Lista de todas as tuplas adicionadas. Usada para verificar integridade.
        '''
        query = f"SELECT * FROM {table} ORDER BY time"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def getMostlyRecentAdded(self, table):
        '''
        Método que retorna uma lista de todas as tuplas adicionadas ordenadas pela coluna time. A tabela deve ter coluna 'time'.

        Args:
            table (str): String que representa a tabela da qual a tupla vai ser retirada.

        Returns:
            (tuple, None): Retorna a ultima tupla adicionada. Usada para criar novos blocos. Se não há dados na tabela retorna None.
        '''
        query = f"SELECT * FROM {table} ORDER BY time DESC LIMIT 1;"
        self.cursor.execute(query)
        return self.cursor.fetchone()
    
    def __del__(self) -> None:
        if hasattr(self,'connection'):
            self.connection.close()
