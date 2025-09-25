operador = input("insira um operador aritmetico(+, -, /, *): ")

if operador == "+":
    a = float(input("Insira o primeiro numero pra soma: "))
    b = float(input("Insira o segundo numero para soama: "))
    soma = a + b
    print(f"Resultado = {soma:.2f}")
elif operador == "-":
    a = float(input("Insira o primeiro numero pra subtracao: "))
    b = float(input("Insira o segundo numero para subtacao: "))
    subtracao = a - b
    print(f"Resultado = {subtracao:.2f}")
elif operador == "/":
    a = float(input("Insira o primeiro numero para divisao: "))
    b = float(input("Insira o segundo numero para divisao: "))
    divisao = a / b
    print(f"Resultado = {divisao:.2f}")
elif operador == "*":
    a = float(input("Insira o primeiro numero para multiplicacao: "))
    b = float(input("Insira o segundo numero para multiplicacao: "))
    multiplicacao = a * b
    print(f"Resultado = {multiplicacao:.2f}")