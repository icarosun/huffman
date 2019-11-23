from codigo import Codigo
from tree import Tree

def printTree(tree):
    if tree == None : return
    printTree(tree.left)
    printTree(tree.right)
    print(tree.codigo.letra)    

def printTreeIndented(tree, level=0) :
  if tree == None : return
  printTreeIndented(tree.right, level+1)
  print('  '*level + (tree.codigo.letra))
  printTreeIndented(tree.left, level+1)

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

alfabeto= [0]*128

tabela = []

#texto=input("Entre com o texto: ")

texto = "a"*20 + "b"*9 + "c"*15 + "d"*11 + "e"*40 + "f"*5 

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

#for tree in tabela:
#    print(tree.codigo.letra, " | ", tree.codigo.peso)

tabela = sorted(tabela, key = lambda x: x.codigo.peso)

#print("-"*10)
#for tree in tabela:
#    print(tree.codigo.letra, " | ", tree.codigo.peso)

maiorEsquerda = True
while(len(tabela)>1):
    tree0=tabela[0].codigo
    tree1=tabela[1].codigo
    if maiorEsquerda:
        novaLetra= "(" + tree1.letra +  "," +  tree0.letra +  ")"
        novoPeso=tree0.peso+tree1.peso
        root= Tree(Codigo(novaLetra, novoPeso), tabela[1], tabela[0])
        maiorEsquerda = False
    else:
        novaLetra= "(" + tree0.letra +  "," +  tree1.letra +  ")"
        novoPeso=tree0.peso+tree1.peso
        root= Tree(Codigo(novaLetra, novoPeso), tabela[0], tabela[1])
        maiorEsquerda = True
    for i in range(2): tabela.pop(0)
    tabela.append(root)
    del(tree0)
    del(tree1)
    del(novaLetra)
    del(novoPeso)
    del(root)
    tabela = sorted(tabela, key = lambda x: x.codigo.peso)

root=tabela[0]
print(root.codigo.letra)
print("Arvore gerada!")
codificar=input("Ensira o texto que deseja codificar: ")
comprimido=compressao(root, codificar)
if(comprimido == -1):
    print("Error")
else:
    print(comprimido)
decodificar=input("Ensira o codigo para ser decodificado: ")
decodificado=decodificacao(root, decodificar)
print(decodificado)
