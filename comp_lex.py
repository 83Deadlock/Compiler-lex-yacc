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
# Inst -> print ( ExpCond ) ;
#       | read ( id ) ;
#       | id = ExpCond ;
#       | if ( Log ) { Insts }
#       | if ( Log ) { Insts } else { Insts }
#       | repeat { Insts } until ( Log )
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
          'PRINT','READ', 'ID', 'NUM', "INT","NAME","MAIN"]

literals = ['(',')','{','}',';']

t_ADD = r'\+'
t_SUB = r'-'
t_MUL = r'\*'
t_DIV = r'/'
t_MOD = r'%'
t_EQ = r'=='
t_ATRIB = r'='
t_AND = r'&'
t_OR = r'\#'
t_NOT = r'\!'
t_DIF = r'!='
t_LES = r'<'
t_LEQ = r'<='
t_GRE = r'>'
t_GEQ = r'>='
t_FUNC = r'func'
t_DECL = r'decl'
t_INST = r'inst'
t_IF = r'if'
t_ELSE = r'else'
t_REPEAT = r'repeat'
t_UNTIL = r'until'
t_PRINT = r'print'
t_READ = r'read'
t_INT = r'int'
t_ID = r'\w+'
t_NUM = r'\-?\d+'
t_MAIN = r'main'
t_NAME = r'name'

t_ignore = " \t\n"

def t_error(t):
    print("Caracter ilegal: ",t.value[0])
    t.lexer.skip

lexer = lex.lex()