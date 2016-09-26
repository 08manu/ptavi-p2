#!/usr/bin/python3
# -*- coding: utf -8-*-

import sys
import calcoo


class CalculadoraHija(calcoo.Calculadora):

    def mult(self, op1, op2):
        return op1 * op2

    def div(self, op1, op2):
        try:
            return op1 / op2
        except ZeroDivisionError:
            sys.exit("Error: Division by zero")

calculadora = CalculadoraHija()

operaciones = {'suma': calculadora.suma, 'resta': calculadora.resta, 
               'multiplica': calculadora.mult, 'divide': calculadora.div}


if __name__ == "__main__":

    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parametres")

    resultado = operaciones[sys.argv[2]](operando1, operando2)

    print(resultado)
