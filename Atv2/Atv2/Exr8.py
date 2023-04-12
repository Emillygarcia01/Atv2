nome = input("Digite o nome: ")
sexo = input("Digite o sexo (M ou F): ")
idade = int(input("Digite a idade: "))

if sexo == "F" and idade < 25:
    print(nome, "ACEITA")
else:
    print("NÃO ACEITA")
