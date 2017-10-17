import sys

def mochila(w,values,quantity,capacity):

    #inserindo valores e pesos, todos neutros
    w.insert(0,0)
    values.insert(0,0)

    #criando a tabela
    tab = [[0 for x in range(capacity+1)] for y in range(quantity+1)]

    #preenchendo a tabela de acordo com o arquivo de entrada
    for i in range(1, quantity+1): #i representado as linhas da tabela, e os indices dos produtos
        for j in range(1, capacity+1): #j = peso da mochila atual

            if w[i] <= j: #se o peso do item i cabe na mochila com o peso j
		
		#operaçoes para inserir o valor na tabela
                aux1 = j - w[i] 
                aux2 = values[i] + tab[i-1][aux1]

                if aux2 > tab[i-1][j]:

                    tab[i][j] = aux2
                else:

                    tab[i][j] = tab[i-1][j]

            else: #senão repito o valor da linha acima na tabela
                tab[i][j] = tab[i-1][j]

    #encontrando os produtos escolhidos
    i = quantity
    j = capacity

    valor_ideal = tab[i][j] #valor ideal para se levar na mochila
    itensQueSeraoLevados = []

    while i > 0 or j > 0:

        if tab[i][j] != tab[i-1][j]:

            #entra
            itensQueSeraoLevados.append(i)

            #proxima coluna
            j = j - w[i]
            i = i - 1

        else:

            i = i - 1
    
    return itensQueSeraoLevados, valor_ideal

#leitura do arquivo, neste caso: "input.txt"
with open(sys.argv[1],'r') as myfile:
    file = myfile.read().replace('\n',' ')
    
res = file.split()

quantity = int(res[0])
capacity = int(res[1])
w = []
values = []

i = 2

#salvando os pesos e os valores dos produtos
while i < len(res):

    w.append(int(res[i]))
    values.append(int(res[i+1]))

    i = i + 2

produtos, valor_final = mochila(w,values,quantity,capacity)

print("produtos selecionados: ")
print(produtos)
print("valor Total de: ")
print(valor_final)