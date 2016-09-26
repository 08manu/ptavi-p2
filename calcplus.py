#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija


fich = open(sys.argv[1] , 'r')
lineas = fich.readlines()


calculadora = calcoohija.CalculadoraHija()


for linea in lineas:
	element = linea[:-1].split(',')


	if element[0] == "suma":
		resultado = calculadora.suma(int(element[1]), int(element[2]))
		for operacion in element[3:]:
			resultado = calculadora.suma(resultado, int(operacion))
	elif element[0] == "resta":
		resultado = calculadora.resta(int(element[1]), int(element[2]))
		for operacion in element[3:]:
			resultado = calculadora.resta(resultado, int(operacion))
	elif element[0] == "multiplica":
			resultado = calculadora.mult(int(element[1]), int(element[2])
		for operacion in element[3:]:
			resultado = calculadora.mult(resultado, int(operacion))
	elif element[0] == "divide":
			resultado = calculadora.div(int(element[1]), int(element[2]))
		for operacion in element[3:]:
			resultado = calculadora.div(resultado, int(operacion))
	print(resultado)

		
        
        
   
