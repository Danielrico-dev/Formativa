def calcular(num1, num2, operacao):
    if operacao == "+":
        return num1 + num2
    elif operacao == "-":
        return num1 - num2
    elif operacao == "*":
        return num1 * num2
    elif operacao == "/":
        if num2 == 0:
            return "Erro: divisão por zero"
        return num1 / num2
    else:
        return "Operação inválida"


if __name__ == "__main__":
    print("Calculadora em Python")

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Escolha a operação (+ - * /): ")

    resultado = calcular(num1, num2, operacao)
    print("Resultado:", resultado)