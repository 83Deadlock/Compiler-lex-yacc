import ply.yacc as yacc
import sys

from comp_lex import tokens,literals

# Rules
def p_Programa(p):
    "Programa : Main Funcoes"
    p.parser.fileOut.write(p[1] + p[2])

def p_Main(p):
    "Main : FUNC MAIN '{' Declaracoes Instrucoes '}'"
    p[0] = p[4] + "\nstart" + p[5] + "stop"

def p_Funcoes(p):
    "Funcoes : Funcoes Funcao"
    p[0] = p[1] + p[2]

def p_Funcoes_Null(p):
    "Funcoes : "
    p[0] = ""

def p_Funcao(p):
    "Funcao : FUNC NAME '{' Instrucoes '}'"
    p[0] = p[4]

def p_Declaracoes(p):
    "Declaracoes : DECL '{' Decls '}'"
    p[0] = p[3]

def p_Decls(p):
    "Decls : Decls Decl"
    p[0] = p[1] + p[2]

def p_DeclsNull(p):
    "Decls : "
    p[0] = ""

def p_Decl_ID(p):
    "Decl : INT ID ';'"
    p.parser.var_int[p[2]] = p.parser.gp
    p.parser.gp += 1
    p[0] = "pushi 0 \n"

def p_Decl_ATRIB(p):
    "Decl : INT ID ATRIB ExpCond ';'"
    p.parser.register[p[4]] = p.paser.gp
    p.parser.gp += 1
    p[0] = p[4]

def p_Instrucoes(p):
    "Instrucoes : INST '{' Insts '}'"
    p[0] = p[3]

def p_Insts(p):
    "Insts : Insts Inst"
    p[0] = p[1] + p[2]


def p_InstsNull(p):
    "Insts : "
    p[0] = ""


def p_InstPrint(p):
    "Inst : PRINT '(' Log ')' ';'"
    p[0] = p[3] + "writei\n"


def p_InstRead(p):
    "Inst : READ '(' ID ')' ';'"
    p[0] = "read\natoi\n" + "storeg " + p.parser.var_int[p[3]] + "\n"


def p_InstAtrib(p):
    "Inst : ID ATRIB ExpCond ';'"
    p[0] = "pushi " + p[3] + "storeg " + p.parser.var_int[p[1]] + "\n"


# def p_InstIf(p):
#     "Inst : if '(' cond ')' '{' Insts '}'"
#     #p[0] = 

# No or -> a # b = (a*b) - (a+b)

def p_Log_not(p):
    "Log : NOT Log"
    p[0] = p[2] + "not\n"

def p_Log_and(p):
    "Log : Log AND FactCond"
    p[0] = p[1] + p[3] + "mul\n"

def p_Log_or(p):
    "Log : Log OR FactCond"
    p[0] = p[1] + p[3] + "add\n" + p[1] + p[3] + "mul\nsub\n"

def p_Log_factcond(p):
    "Log : FactCond"
    p[0] = p[1]

def p_FactCond_leq(p):
    "FactCond : FactCond LEQ ExpCond"
    p[0] = p[1] + p[3] + "infeq\n"

def p_FactCond_les(p):
    "FactCond : FactCond LES ExpCond"
    p[0] = p[1] + p[3] + "inf\n"

def p_FactCond_geq(p):
    "FactCond : FactCond GEQ ExpCond"
    p[0] = p[1] + p[3] + "supeq\n"

def p_FactCond_gre(p):
    "FactCond : FactCond GRE ExpCond"
    p[0] = p[1] + p[3] + "sup\n"

def p_FactCond_eq(p):
    "FactCond : FactCond EQ ExpCond"
    p[0] = p[1] + p[3] + "equal\n"

def p_FactCond_dif(p):
    "FactCond : FactCond DIF ExpCond"
    p[0] = p[1] + p[3] + "equal\nnot\n"

def p_FactCond_expcond(p):
    "FactCond : ExpCond"
    p[0] = p[1]

def p_ExpCond_add(p):
    "ExpCond : ExpCond ADD TermoCond"
    p[0] = p[1] + p[3] + "add\n"

def p_ExpCond_sub(p):
    "ExpCond : ExpCond SUB TermoCond"
    p[0] = p[1] - p[3] + "sub\n"

def p_ExpCond_termo(p):
    "ExpCond : TermoCond"
    p[0] = p[1]

def p_TermoCond_mult(p):
    "TermoCond : TermoCond MUL FactorCond"
    p[0] = p[1] + p[3] + "mul\n"

def p_TermoCond_div(p):
    "TermoCond : TermoCond DIV FactorCond"
    if p[3] != 0:
        p[0] = p[1] + p[3] + "div\n"
    else:
        p[0] = "pushi 0\n"

def p_TermoCond_mod(p):
    "TermoCond : TermoCond MOD FactorCond"
    if p[3] != 0:
        p[0] = p[1] + p[3] + "mod\n"
    else:
        p[0] = "pushi -1\n"

def p_TermoCond_fator(p):
    "TermoCond : FactorCond"
    p[0] = p[1]

def p_FactorCond_par(p):
    "FactorCond : '(' Log ')'"
    p[0] = p[2]

def p_FactorCond_num(p):
    "FactorCond : NUM"
    p[0] = "pushi " + p[1] + "\n"

def p_FactorCond_id(p):
    "FactorCond : ID"
    p[0] = "pushg " + p.parser.var_int[p[1]] + "\n"

def p_error(p):
    print("Syntax Error in input: ", p)

q = 0
while q == 0:
    fileInName = input("Input File Path >> ")
    try:
        fileIn = open(fileInName,"r")
        q = 1
    except (FileNotFoundError, NotADirectoryError):
        print("Wrong File Path\n")

q = 0
while q == 0:
    fileOutName = input("Output File Path >> ")
    try:
        fileOut = open(fileOutName,"w")
        q = 1
    except NotADirectoryError:
        print("Wrong File Path\n")

#Parser Dicktionary
parser = yacc.yacc()

parser.registers = {}
parser.var_int ={}
parser.gp = 0
parser.ifCount = 0      #conta os ifs para qnd criar concatenar com "if"
parser.cycleCount = 0   #igual aos ifs
parser.fileOut = fileOut

dataIn = fileIn.read()
parser.parse(dataIn)

fileIn.close()
fileOut.close()