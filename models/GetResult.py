from ConnectDB import ConnectDB

def getResult():
    '''
    Função que retorna um dicionário com o resultado da eleição.

    Returns:
        (dict): retorna dicionário que representa o resultado. a chave é o número do candidato e o valor a quantidade de votos.
    '''
    
    condb = ConnectDB()

    alldata = condb.getAllAdded("Blocks")

    votes = {}

    for data in alldata:
        if data[1] in votes:
            votes[data[1]] += 1
        else:
            votes.update({data[1]:1})

    return votes

if __name__ == "__main__":
    votes = getResult()
    print("Cand.       Votos")
    for keyName in votes:
        print(f"{keyName: >5} --- {votes[keyName]: >7}") if keyName != 0 else None