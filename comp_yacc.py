import ply.yacc as yacc
import sys
import os

from comp_lex import tokens,literals

# Rules
def p_Programa(p):
    "Programa : Main Funcoes"
    p.parser.fileOut.write("main:\n" + p[1] + p[2])

def p_Main(p):
    "Main : FUNC MAIN '{' Declaracoes Instrucoes '}'"
    p[0] = p[4] + "start\n" + p[5] + "stop\n"

def p_Funcoes(p):
    "Funcoes : Funcoes Funcao"
    p[0] = p[1] + p[2]

def p_Funcoes_Null(p):
    "Funcoes : "
    p[0] = ""

def p_Funcao(p):
    "Funcao : FUNC NAME '{' Declaracoes Instrucoes '}'"
    p.parser.functionsDefined.append(p[2])
    p[0] = f"{p[2]}:\n{p[4]}{p[5]}return\n"

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
    p.parser.var_int[p[2]] = p.parser.gp
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

def p_Inst_Print_str(p):
    "Inst : PRINT LPAR STRING RPAR ';'"
    p[0] = "pushs " + p[3] + "\n" + "writes\n"

def p_Inst_Print_log(p):
    "Inst : PRINT LPAR Log RPAR ';'"
    p[0] = p[3] + "writei\npushs \"\\n\" \nwrites\n"

def p_Inst_Read(p):
    "Inst : READ LPAR ID RPAR ';'"
    if p[3] in p.parser.var_int:
        p[0] = "read\natoi\n" + "storeg " + str(p.parser.var_int[p[3]]) + "\n"
    else:
        print("Unused variable " + p[3]+"\n")

def p_Inst_Exec(p):
    "Inst : EXEC NAME LPAR RPAR ';'"
    p[0] = f"pusha {p[2]}\ncall\n"

def p_Inst_Atrib(p):
    "Inst : ID ATRIB ExpCond ';'"
    p[0] = p[3] + "storeg " + str(p.parser.var_int[p[1]]) + "\n"

def p_Inst_If(p):
    "Inst : IF LPAR Log RPAR '{' Insts '}'"
    p[0] = p[3] + f"jz fimif{p.parser.ifCount}\n" + p[6] + f"fimif{p.parser.ifCount}:\n"
    p.parser.ifCount = p.parser.ifCount + 1 

def p_Inst_ifelse(p):
    "Inst : IF LPAR Log RPAR '{' Insts '}' ELSE '{' Insts '}'"
    p[0] = p[3] + f"jz else{p.parser.ifCount}\n" + p[6] + f"jump fimif{p.parser.ifCount}\n" + f"else{p.parser.ifCount}:\n" + p[10] + f"fimif{p.parser.ifCount}:\n"
    p.parser.ifCount = p.parser.ifCount + 1

def p_Inst_repeat(p):
    "Inst : REPEAT '{' Insts '}' UNTIL LPAR Log RPAR"
    p[0] = f"repeat{p.parser.ifCount}:\n" + p[3] + p[7] + f"jz repeat{p.parser.ifCount}\n"
    p.parser.ifCount = p.parser.ifCount + 1

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
    p[0] = p[1] + p[3] + "sub\n"

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
        print("Invalid operation:\n\tCan't divide " + p[1] + "by zero.")
        p[0] = ""
        parser.errorCount = parser.errorCount + 1
        parser.success = False

def p_TermoCond_mod(p):
    "TermoCond : TermoCond MOD FactorCond"
    if p[3] != 0:
        p[0] = p[1] + p[3] + "mod\n"
    else:
        print("Invalid operation:\n\tCan't divide " + p[1] + "by zero.")
        p[0] = ""
        parser.errorCount = parser.errorCount + 1
        parser.success = False

def p_TermoCond_fator(p):
    "TermoCond : FactorCond"
    p[0] = p[1]

def p_FactorCond_par(p):
    "FactorCond : LPAR Log RPAR"
    p[0] = p[2]

def p_FactorCond_num(p):
    "FactorCond : NUM"
    p[0] = "pushi " + p[1] + "\n"

def p_FactorCond_id(p):
    "FactorCond : ID"
    if p[1] in p.parser.var_int:
        p[0] = "pushg " + str(p.parser.var_int[p[1]]) + "\n"
    else:
        print("'" + p[1] + "' variable undefined.")
        p[0] = ""
        parser.errorCount = parser.errorCount + 1
        parser.success = False

def p_error(p):
    print("Syntax Error in input: ", p)
    parser.errorCount = parser.errorCount + 1
    parser.success = False

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

parser = yacc.yacc()

parser.var_int = {}
parser.gp = 0
parser.ifCount = 0      #conta os ifs para qnd criar concatenar com "if"
parser.cycleCount = 0   #igual aos ifs
parser.success = True
parser.fileOut = fileOut
parser.errorCount = 0
parser.functionsDefined = []
parser.functionsCalled = []

dataIn = fileIn.read()
parser.parse(dataIn)

fileIn.close()
fileOut.close()

for func in parser.functionsCalled:
    if not func in parser.functionsDefined:
        print("Undefined function '" + func +"'.")
        parser.success = False
        parser.errorCount = parser.errorCount + 1

if not parser.success:
    print(f"Found {parser.errorCount} errors in " + fileInName +".")
    os.remove(fileOutName)