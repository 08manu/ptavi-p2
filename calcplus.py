#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija


fich = open(sys.argv[1], 'r')
lineas = fich.readlines()

calculadora = calcoohija.CalculadoraHija()

operaciones = {'suma': calculadora.suma, 'resta': calculadora.resta,
               'multiplica': calculadora.mult, 'divide': calculadora.div}

for linea in lineas:

    element = linea[:-1].split(',')

    resultado = operaciones[element[0]](int(element[1]), int(element[2]))
    for operacion in element[3:]:
        resultado = operaciones[element[0]](resultado, int(operacion))

    print(resultado)
