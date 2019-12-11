from huffman import Huffman

huffman=Huffman()

print("\t\t2 - COMPRIMIR")
print("\t\t1 - DESCOMPRIMIR")
opcao=int(input("Escolha: "))

if opcao == 2:
    huffman.comprimir("Entrada/comprimir.txt")
elif opcao == 1:
    huffman.descomprimir("Entrada/descomprimir.txt")
else:
    print("Tchau!")