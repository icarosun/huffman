import huffman

opcao=-1
while(opcao != 0):
    print(""" 
    GERAR ARVORE HUFFMAN

TEXTO - 2
TABELA - 1
-------------------
SAIR - 0
""")
    opcao=int(input("Escolha: "))
    if(opcao > 2 or opcao < 0):
        print("Escolha invalida, digite um valor entre 0 e 2")            
    else:
        menu=1
        if opcao == 2:
            texto=input("Ensira o texto: ")
            root=huffman.newTabelaTxt(texto)
            print("Arvore gerada")
            print(root.codigo.letra)
            print("Compressao do texto: ")
            print(huffman.compressao(root, texto))
        elif opcao == 1:
            print("Ensira a tabela: ")
            print("a,3,b,4,")
            tabela=input("Tabela: ")
            root=huffman.newTabela(tabela)
            print("Arvore gerada")
            print(root.codigo.letra)
        elif opcao == 0:
            print("Tchau mundo!")
            menu=-1
        else:
            print("Error")
            menu=-1       
        
        while(menu != -1):
            print("""
    MENU

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
                texto=input("Ensira o texto: ")
                print(huffman.compressao(root, texto))
            elif menu == 1:
                codigo = input("Ensira: ")
                print(huffman.decodificacao(root, codigo))
            else:
                print("Tchau mundo!")
                opcao=0
                menu=-1