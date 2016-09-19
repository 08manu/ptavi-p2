#!/usr/bin/python3
#-*- coding: utf-8-*-

import sys
import calcoohija

fich = open('/tmp/git/fichero' , 'r')
lineas = fich.readlines()


for linea in lineas:
    calculadora = calcoohija.CalculadoraHija()
    element = linea[:-1].split(',') 
    print(linea[0])
    if linea[0] == "suma":
        resultado = calculadora.suma(element[1], element[2]) 
    
        #resultado = calculadora.suma(resultado, element[3]) 
        #resultado = calculadora.suma(resultado, element[4]) 
        #resultado = calculadora.suma(resultado, element[5]) 
        #resultado = calculadora.suma(resultado, element[6])
         
        for elemento in linea[3:]:
            resultado = calculadora.suma(resultado, elemento) 
           
        print(resultado)

    #if linea[0] == "resta":
        
        
   
