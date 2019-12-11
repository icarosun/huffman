from codigo import Codigo
from tree import Tree

def compressao(tree, mensagem):
    compressao= ""
    for letra in mensagem:
        if letra in tree.codigo.letra:
            newTree=tree
            chave=""
            while(letra != newTree.codigo.letra):
                esquerda=newTree.left
                direita=newTree.right
                if(letra == esquerda.codigo.letra):
                    chave+="0"
                    newTree=esquerda
                elif(letra in esquerda.codigo.letra):
                    chave+="0"
                    newTree=esquerda
                elif(letra == direita.codigo.letra):
                    chave+="1"
                    newTree=direita
                else:
                    chave+="1"
                    newTree=direita
            del(direita)                
            del(esquerda)
            del(newTree)
            compressao+=chave
        else:
            return -1
    return compressao

def decodificacao(tree, codigo):
    decodificado=""
    newTree=tree
    for bit in codigo:
        if(newTree.left == None and newTree.right == None):
            decodificado+=newTree.codigo.letra
            newTree=tree
        else:
            if bit == "0":
                newTree=newTree.left
                if(newTree.left == None and newTree.right == None):
                    decodificado+=newTree.codigo.letra
                    newTree=tree
            else:
                newTree=newTree.right
                if(newTree.left == None and newTree.right == None):
                    decodificado+=newTree.codigo.letra
                    newTree=tree
    return decodificado

def newTabelaTxt(texto):
    alfabeto=[0]*128
    tabela = []
    for i in texto:
        alfabeto[ord(i)] +=1
    soma=0
    for i,x in enumerate(alfabeto):
        if x != 0:
            frequencia=Codigo(chr(i), x)
            tree=Tree(frequencia)
            tabela.append(tree)
            del(frequencia)
            del(tree)
            soma+=x
    for tree in tabela:
        tree.codigo.peso=tree.codigo.peso/soma
    return treeHuffman(tabela)

def treeHuffman(tabela):
    tabela = sorted(tabela, key = lambda x: x.codigo.peso)
    while(len(tabela)>1):
        tree0=tabela[0].codigo
        tree1=tabela[1].codigo
        novaLetra= "(" + tree0.letra +  "," +  tree1.letra +  ")"
        novoPeso=tree0.peso+tree1.peso
        root= Tree(Codigo(novaLetra, novoPeso), tabela[0], tabela[1])
        for i in range(2): tabela.pop(0)
        tabela.append(root)
        del(tree0)
        del(tree1)
        del(novaLetra)
        del(novoPeso)
        del(root)
        tabela = sorted(tabela, key = lambda x: x.codigo.peso)
    return tabela[0]

def newTabela(palavra):
    lista=palavra.split(",")
    tabela=[]
    soma=0
    while(len(lista)>0):
        soma+=int(lista[1])
        frequencia=Codigo(lista[0], int(lista[1]))
        tree=Tree(frequencia)
        tabela.append(tree)
        del(frequencia)
        del(tree)
        for i in range(2): lista.pop(0)
    for tree in tabela:
        tree.codigo.peso = tree.codigo.peso/soma
    return treeHuffman(tabela)

def printarHuffman(tree, lista, top, vector):
    if(tree.left != None):
        lista[top]= "0"
        printarHuffman(tree.left, lista, top+1, vector)

    if(tree.right != None):
        lista[top]="1"
        printarHuffman(tree.right, lista, top+1, vector)
    
    if(tree.left == None and tree.right == None):
        printArr(tree.codigo.letra,lista, top, vector)

def printArr(codigo, lista, top, vetor):
    binario=""
    for i in range(top):
        binario+=lista[i]
    tupla=codigo + " " + binario
    vetor.append(tupla)

def tabelaCodigo():
    huffmanComp=dict()
    huffmanDesc=dict()
    tam=int(input("Insira o tamanho da tabela: "))
    for i in range(0, tam):
        letra=input("Insira a letra: ")
        codigo=input("Insira o respectivo codigo: ")
        huffmanComp[letra]= codigo
        huffmanDesc[codigo]=letra
    opcao=-1
    while(opcao!=0):
        print("""
            1-comprimir
            2-descomprimir

            0-Sair
         """)
        opcao=int(input("Escolha uma opcao: "))
        if opcao == 1:
            saida=[]
            texto=input("Entre com a mensagem: ")
            for i in texto:
                saida.append(huffmanComp[i])
            saida = "".join(saida)
            print(saida)
            arquivo=open("comprimir.txt", "w")
            arquivo.write(saida)
            arquivo.close()
        elif(opcao == 2):
            saida=[]
            texto=leitura ()
            palavra=""
            print(texto)
            indice=0
            while(indice < len(texto)):
                palavra+=texto[indice]
                if palavra in huffmanDesc:
                    saida.append(huffmanDesc[palavra])
                    palavra=""
                indice+=1
            saida= "".join(saida)
            print(saida)
            arquivo=open("descomprimir.txt", "w")
            arquivo.write(saida)
            arquivo.close()
        else:
            print("Saindo")

def leitura():
    nomeTxt = input("Insira o nome do arquivo em txt: ")
    arquivo=open(nomeTxt)
    l=arquivo.readlines()
    print(l)
    arquivo.close()
    l="".join(l)
    return l

def ler():
    huffmanComp=dict()
    huffmanDesc=dict()
    nomeTxt="entrada_top.txt"
    arquivo= open(nomeTxt)
    for i,x in enumerate(arquivo.readlines()):
        if(i == 0):
            texto=x.split()
        else:
            l=x.split()
            if(len(l)>1):
                letra=l[1]
                codigo=l[0]
                huffmanComp[letra]= codigo
                huffmanDesc[codigo]=letra
            else:
                codigo=l[0]
                huffmanComp[" "]= codigo
                huffmanDesc[codigo]=" "
    texto="".join(texto)
    opcao=-1
    while(opcao!=0):
        print("""
            1-comprimir
            2-descomprimir

            0-Sair
         """)
        opcao=int(input("Escolha uma opcao: "))
        if opcao == 1:
            saida=[]
            for i in texto:
                saida.append(huffmanComp[i])
            saida = "".join(saida)
            print(saida)
            arquivo=open("comprimir.txt", "w")
            arquivo.write(saida)
            arquivo.close()
        elif(opcao == 2):
            saida=[]
            palavra=""
            indice=0
            while(indice < len(texto)):
                palavra+=texto[indice]
                if palavra in huffmanDesc:
                    saida.append(huffmanDesc[palavra])
                    palavra=""
                indice+=1
            saida= "".join(saida)
            print(saida)
            arquivo=open("descomprimir.txt", "w")
            arquivo.write(saida)
            arquivo.close()
        else:
            print("Saindo")