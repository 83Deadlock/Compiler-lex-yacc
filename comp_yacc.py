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


def p_Decl(p):
    "Decl : int ID"
    "Decl : int ID ATRIB "


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




#Parser
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
