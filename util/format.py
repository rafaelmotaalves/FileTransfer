def byte_to_string(bytes):
    """
    Retorna uma formatação adequada para leitura do tamanho do arquivo
    """
    if(bytes >= 10**9):
        return '{} Gbytes'.format(bytes/10**9)
    elif(bytes >= 10**6):
        return '{} Mbytes'.format(bytes/10**6)
    elif(bytes >= 10**3):
        return '{} Kbytes'.format(bytes/10**3)
    return '{} bytes'.format(bytes)