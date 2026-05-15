def dividir_lista(lista, n):

    k, m = divmod(len(lista), n)

    return [lista[i*k + min(i,m):(i+1)*k + min(i+1,m)] for i in range(n)]