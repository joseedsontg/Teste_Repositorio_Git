#input() = a function that prompts the user to enter data
#          returns the entered data as a string

nome = input("Qual eh o seu nome: ")
print(f"Ola {nome}!")
idade = int(input("Qauntos anos voce tem?: "))
idade = idade + 1
print(f"Voce tem {idade} anos")