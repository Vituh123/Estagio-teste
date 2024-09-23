palavra_invertida = ""
palavra = input("Digite uma palavra: ")

for i in range(len(palavra) - 1, -1, -1):
    palavra_invertida += palavra[i]

print("Palavra invertida:", palavra_invertida)