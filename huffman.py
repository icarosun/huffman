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
    