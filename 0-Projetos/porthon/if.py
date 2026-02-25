idade = int(input("Digite sua idade: "))
while idade>0 and idade<=120:
    if idade >= 18:
        print("Você é maior de idade.")
    else:
        print("Você é menor de idade.")
    int(input("Digite uma idade válida: "))
