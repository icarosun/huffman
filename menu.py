import huffman

armazenamento=[]
lista=[0]*128
opcao=-1
while(opcao != 0):
    print(""" 
    GERAR ARVORE HUFFMAN

TESTE - 5
LER ARQUIVO - 4
TABELA CODIGO - 3
TEXTO - 2
TABELA - 1
-------------------
SAIR - 0
""")
    opcao=int(input("Escolha: "))
    if(opcao > 5 or opcao < 0):
        print("Escolha invalida, digite um valor entre 0 e 2")            
    else:
        menu=1
        if opcao == 2:
            texto=huffman.leitura()
            print(texto)
            root=huffman.newTabelaTxt(texto)
            print("Arvore gerada")
            print(root.codigo.letra)
            print("Compressao do texto: ")
            print(huffman.compressao(root, texto))
        elif opcao == 1:
            print("Insira a tabela: ")
            print("a,3,b,4,")
            tabela=input("Tabela: ")
            root=huffman.newTabela(tabela)
            print("Arvore gerada")
            print(root.codigo.letra)
        elif opcao == 0:
            print("Tchau mundo!")
            menu=-1
        elif opcao == 3:
            huffman.tabelaCodigo()
        elif opcao == 4:
            huffman.leitura()
        elif opcao == 5:
            huffman.ler()
        else:
            print("Error")
            menu=-1       
        
        while(menu != -1):  
            print("""
    MENU

PRINTAR ARVORE - 4
GERAR NOVA ARVORE - 3
CODIFICAR - 2
DECODIFICAR - 1
SAIR - 0
                """)
            menu = int(input("Escolha: "))
            if menu == 3:
                print("Voltando")
                menu=-1
            elif menu == 2:
                texto=input("Insira o texto: ")
                codigo=huffman.compressao(root, texto)
                print(codigo)
            elif menu == 1:
                codigo = input("Insira: ")
                print(huffman.decodificacao(root, codigo))
            elif menu == 4:
                huffman.printarHuffman(root,lista, 0, armazenamento)
                for x in armazenamento:
                    print(x)
            else:
                print("Tchau mundo!")
                opcao=0
                menu=-1
