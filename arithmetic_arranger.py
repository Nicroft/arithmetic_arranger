def arithmetic_arranger(problems,show_results=False):
    # Verificar si hay demasiados problemas
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = []
    for problem in problems:
        # Dividir el problema en operandos y operador
        operand1, operator, operand2 = problem.split()

        # Verificar que los operandos sean números
        if not operand1.isnumeric() or not operand2.isnumeric():
            return "Error: Numbers must only contain digits."

        # Verificar que el operador sea + o -
        if operator not in ("+", "-"):
            return "Error: Operator must be '+' or '-'."

        # Longitud máxima de los operandos
        max_len = max(len(operand1), len(operand2))

        # Crear la línea superior con el primer operando
        line1 = operand1.rjust(max_len + 2)

        # Crear la línea central con el operador y el segundo operando
        line2 = operator + " " + operand2.rjust(max_len)

        # Crear la línea inferior con guiones
        line3 = "-" * (max_len + 2)

        # Calcular el resultado si es necesario
        if show_results:
            if operator == "+":
                result = str(int(operand1) + int(operand2))
            else:
                result = str(int(operand1) - int(operand2))
            line4 = result.rjust(max_len + 2)
            arranged_problems.append(f"{line1}\n{line2}\n{line3}\n{line4}")
        else:
            arranged_problems.append(f"{line1}\n{line2}\n{line3}")

    return "\n".join(arranged_problems)
