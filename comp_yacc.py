import ply.yacc as yacc
import sys

from comp_lex import tokens,literals

parser = yacc.yacc()

parser.registers = {}

q = 0
while q == 0:
    fileInName = input("InputFile>>")
    try:
        fileIn = open(fileInName,"r")
        lines = fileIn.readlines()
        q = 1
    except OSError:
        print("Nome de ficheiro inválido")

fileOutName = input("OutputFile>>")
fileOut = open(fileOutName,"w")

for linha in lines:
    result = parser.parse(linha)
    fileOut.write(result)