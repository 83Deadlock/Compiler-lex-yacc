# Comp_lex.py
#
# Trabalho Prático PL
#
# Programa -> Main Funcoes
#
# Funcoes -> Funcoes Funcao
#          | £
#
# Funcao -> func nome { Declaracoes Instrucoes }
#
# Main -> func main { Declaracoes Instrucoes }
#
# Declaracoes -> decl { Decls }
# 
# Decls -> Decls Decl
#        | £
# 
# Decl -> int id ;
#        | int id = ExpCond ;
# 
# Instrucoes -> inst { Insts }
#
# Insts -> Insts Inst
#        | £
#
# Inst -> print '(' Log ')' ;
#       | print '(' string ')'
#       | read '(' id ')' ;
#       | exec nome '(' ')' ';'
#       | id = ExpCond ;
#       | if '(' Log ')' '{' Insts '}'
#       | if '(' Log ')' '{' Insts '}' else '{' Insts '}'
#       | repeat '{' Insts '}' until '(' Log ')'
#
# Log -> ! Log
#      | Log '&' FactCond
#      | Log '#' FactCond
#      | FactCond
#
# FactCond -> FactCond '<=' ExpCond
#          |  FactCond '<' ExpCond
#          |  FactCond '>=' ExpCond
#          |  FactCond '>' ExpCond
#          |  FactCond '==' ExpCond
#          |  FactCond '!=' ExpCond
#          |  ExpCond
# 
# ExpCond -> ExpCond '+' TermoCond
#         |  ExpCond '-' TermoCond
#         |  TermoCond
#
# TermoCond -> TermoCond '*' FactorCond
#            | TermoCond '/' FactorCond
#            | TermoCond '%' FactorCond
#            | FactorCond
#
# FactorCond -> '(' Log ')'
#            | num
#            | id

import ply.lex as lex

tokens = ['ADD','SUB','MUL','DIV','MOD','ATRIB',
          'AND','OR','NOT','EQ','DIF','LES','LEQ','GRE','GEQ',
          'FUNC','DECL','INST','IF','ELSE','REPEAT','UNTIL',
          'PRINT','READ', 'ID', 'NUM', "INT","NAME","MAIN",
          'LPAR','RPAR','STRING','EXEC']

literals = ['{','}',';']

def t_EXEC(t):
    r'\?'
    return t

def t_LPAR(t):
    r'\('
    return t

def t_RPAR(t):
    r'\)'
    return t

def t_ADD(t):
    r'\+'
    return t

def t_SUB(t):    
    r'-'
    return t

def t_MUL(t):
    r'\*'
    return t

def t_DIV(t):
    r'/'
    return t

def t_MOD(t):
    r'%'
    return t

def t_EQ(t):
    r'=='
    return t

def t_ATRIB(t):
    r'='
    return t

def t_AND(t):
    r'&'
    return t

def t_OR(t):
    r'\#'
    return t

def t_DIF(t):
    r'!='
    return t

def t_NOT(t):
    r'\!'
    return t

def t_LES(t):
    r'<'
    return t

def t_LEQ(t):
    r'<='
    return t

def t_GRE(t):
    r'>'
    return t

def t_GEQ(t):
    r'>='
    return t

def t_FUNC(t):
    r'func'
    return t

def t_DECL(t):
    r'decl'
    return t

def t_INST(t):
    r'inst'
    return t

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_REPEAT(t):
    r'repeat'
    return t

def t_UNTIL(t):
    r'until'
    return t

def t_PRINT(t):
    r'print'
    return t

def t_READ(t):
    r'read'
    return t

def t_INT(t):
    r'int'
    return t

def t_NUM(t):
    r'\-?\d+'
    return t

def t_MAIN(t):
    r'main'
    return t

def t_NAME(t):
    r'[A-Z][a-zA-Z0-9_]*'
    return t

def t_STRING(t):
    r'\"[^"]*\"'
    return t

def t_ID(t):
    r'[a-z][a-zA-Z0-9_]*'
    return t

t_ignore = " \t\n"

def t_error(t):
    print("Caracter ilegal: ",t.value[0])
    t.lexer.skip

lexer = lex.lex()