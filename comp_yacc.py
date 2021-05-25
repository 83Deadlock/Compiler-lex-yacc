import ply.yacc as yacc
import sys

from comp_lex import tokens,literals

# Rules
def p_Programa(p):
    "Programa : Main Funcoes"

def p_Main(p):
    "Main : func main '{' Declaracoes Instrucoes '}'"
    p[0] = p[4] + "\nstart" + p[5] + "stop"

def p_Funcoes(p):
    "Funcoes : Funcoes Funcao"


def pFuncoesNull(p):
    "Funcoes : "

def p_Funcao(p):
    "Funcao : func nome '{' Declaracoes Instrucoes '}'"


def p_Declaracoes(p):
    "Declaracoes : decl '{' Decls '}'"


def p_Decls(p):
    "Decls : Decls Decl"


def p_DeclsNull(p):
    "Decls : "


def p_Decl_ID(p):
    "Decl : int ID"
    p.parser.var_int[p[2]] = p.parser.gp
    p.parser.gp+= 1
    p[0] = "pushi" + p[2] +"\n"

def p_Decl_ATRIB(p):
    "Decl : int ATRIB  '=' ID"
    #not sure, prob é merda
    p.parser.register[p[3]] = p.parser.var_int[p[2]]
    p.parser.register[p[3]] = p.paser.gp
    p.parser.gp+= 1
    p[0] = "pushi" + p[3] +'\n'

def p_Instrucoes(p):
    "Intrucoes : INST '{' Insts '}'"


def p_Insts(p):
    "Insts : Insts Inst"
    p[0] = p[1] + p[2]


def p_InstsNull(p):
    "Insts : "


def p_InstPrint(p):
    "Inst : PRINT '(' Exp ')'"
    p[0] = p[3] + "writei\n"


def p_InstRead(p):
    "Inst : READ '(' ID ')'"
    p[0] = p[2] + "read\n"


def p_InstAtrib(p):
    "Inst : ID = Exp"
    p[0] = "pushi" + p[2] + "\n"


def p_InstIf(p):
    "Inst : if '(' cond ')' '{' Insts '}'"
    p[0] = 





#Parser Dicktionary
parser = yacc.yacc()

parser.registers = {}
parser.var_int ={}
parser.gp = 0

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
