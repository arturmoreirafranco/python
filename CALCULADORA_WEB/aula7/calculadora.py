import math
from flask import render_template, request

def calcular():
    try:
        num1 = float(request.form["num1"])
    except (KeyError, ValueError):
        return render_template("calculadora.html", etapas="Erro: Informe um primeiro número válido.", resultados="")

    operacao = request.form.get("operacao")

    if operacao == "sqrt":
        if num1 < 0:
            resultado = "Erro"
            etapas = f"Erro matemático: Não existe raiz real de número negativo ({num1})."
        else:
            resultado = math.sqrt(num1)
            etapas = f"√{num1} = {resultado}"

    elif operacao == "log":
        if num1 <= 0:
            resultado = "Erro"
            etapas = "Erro matemático: O logaritmo só existe para números maiores que zero."
        else:
            resultado = math.log10(num1)
            etapas = f"log10({num1}) = {resultado}"

    else:
        num2_valor = request.form.get("num2", "").strip()
        if not num2_valor:
            return render_template("calculadora.html", etapas="Informe o segundo número para esta operação.", resultados="")
        
        try:
            num2 = float(num2_valor)
        except ValueError:
            return render_template("calculadora.html", etapas="O segundo número informado é inválido.", resultados="")

        if operacao == "+":
            resultado = num1 + num2
            etapas = f"{num1} + {num2} = {resultado}"

        elif operacao == "-":
            resultado = num1 - num2
            etapas = f"{num1} - {num2} = {resultado}"

        elif operacao == "*":
            resultado = num1 * num2
            etapas = f"{num1} * {num2} = {resultado}"

        elif operacao == "/":
            if num2 == 0:
                resultado = "Erro"
                etapas = "Erro matemático: Divisão por zero não é permitida."
            else:
                resultado = num1 / num2
                etapas = f"{num1} / {num2} = {resultado}"

        elif operacao == "**":
            try:
                resultado = math.pow(num1, num2)
                etapas = f"{num1} ^ {num2} = {resultado}"
            except OverflowError:
                resultado = "Erro"
                etapas = "Erro: O resultado gerou um número grande demais (Overflow)."

        else:
            return render_template("calculadora.html", etapas="Operação inválida.", resultados="")

    return render_template("calculadora.html", etapas=etapas, resultados=resultado)
