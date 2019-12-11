from codigo import Codigo
from tree import Tree

class Huffman:
    def __init__(self):
        self.compressao=dict()
        self.descompressao=dict()
        self.tabela=[]
        self.texto=""

    def analisarFrequencia(self, nomeArquivo):
        alfabeto=[0]*128
        arquivo=open(nomeArquivo)
        linha=arquivo.readlines()
        arquivo.close()
        tabelaPeso = []
        self.texto = "".join(linha)
        for i in self.texto:
            alfabeto[ord(i)] +=1
        soma=0
        for i,x in enumerate(alfabeto):
            if x != 0:
                frequencia=Codigo(chr(i), x)
                tree=Tree(frequencia)
                tabelaPeso.append(tree)
                del(frequencia)
                del(tree)
                soma+=x
        for tree in tabelaPeso:
            tree.codigo.peso=tree.codigo.peso/soma
        root=self.geraArvore(tabelaPeso)
        huffman=Huffman()
        array=[0]*128
        self.gerarTabela(root, array, 0, self.tabela)
        self.gerarEstruturas()

    def geraArvore(self,pesos):
        pesos = sorted(pesos, key = lambda x: x.codigo.peso)
        esquerdaMaior=True
        while(len(pesos)>1):
            tree0=pesos[0].codigo
            tree1=pesos[1].codigo
            if esquerdaMaior:
                novaLetra= "(" + tree1.letra +  "," +  tree0.letra +  ")"
                novoPeso=tree0.peso+tree1.peso
                root= Tree(Codigo(novaLetra, novoPeso), pesos[1], pesos[0])
                esquerdaMaior=False
            else:
                novaLetra= "(" + tree0.letra +  "," +  tree1.letra +  ")"
                novoPeso=tree0.peso+tree1.peso
                root= Tree(Codigo(novaLetra, novoPeso), pesos[0], pesos[1])
                esquerdaMaior=True
            for i in range(2): pesos.pop(0)
            pesos.append(root)
            del(tree0)
            del(tree1)
            del(novaLetra)
            del(novoPeso)
            del(root)
            pesos = sorted(pesos, key = lambda x: x.codigo.peso)
        return pesos[0]

    def gerarTabela(self, tree, lista, top, vector):
        if(tree.left != None):
            lista[top]= "0"
            self.gerarTabela(tree.left, lista, top+1, vector)

        if(tree.right != None):
            lista[top]="1"
            self.gerarTabela(tree.right, lista, top+1, vector)
        
        if(tree.left == None and tree.right == None):
            self.gerarTupla(tree.codigo.letra,lista, top, vector)

    def gerarTupla(self,codigo, caminho, tamanho, vetor):
        binario=""
        for i in range(tamanho):
            binario+=caminho[i]
        tupla=codigo + " " + binario
        vetor.append(tupla)

    def printaTabela(self):
        for tupla in self.tabela:
            print(tupla)
    
    def gerarEstruturas(self):
        for tupla in self.tabela:
            self.compressao[tupla[0]]=tupla[2:]
            self.descompressao[tupla[2:]]= tupla[0]

    def comprimir(self, nomeArquivo):
        self.analisarFrequencia(nomeArquivo)
        arquivo=open("Saida/comprimido.txt", "w")
        saida=""
        for letra in self.texto:
            saida+=self.compressao[letra]
        for tupla in self.tabela:
            saida += "\n" + tupla
        arquivo.write(saida)
        arquivo.close()

    def descomprimir(self, nomeArquivo):
        arquivo=open(nomeArquivo)
        for i,x in enumerate(arquivo.readlines()):
            if(i == 0):
                binario=x.split()
            else:
                linha=x.split()
                if(len(linha)>1):
                    letra=linha[0]
                    codigo=linha[1]
                    self.descompressao[codigo]=letra
                else:
                    codigo=linha[0]
                    self.descompressao[codigo]=" "
        binario="".join(binario)
        arquivo.close()
        palavra=""
        saida=[]
        indice=0
        while(indice < len(binario)):
            palavra+=binario[indice]
            if palavra in self.descompressao:
                saida.append(self.descompressao[palavra])
                palavra=""
            indice+=1
        saida= "".join(saida)
        arquivo=open("Saida/descomprimido.txt", "w")
        arquivo.write(saida)
        arquivo.close()