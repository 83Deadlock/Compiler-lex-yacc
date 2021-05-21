# Comp_lex.py
#
# Trabalho Prático PL
#
# Programa -> Main funcoes
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
#        | int id = Exp ;
# 
# Instrucoes -> inst { Insts }
#
# Insts -> Insts Inst
#        | £
#
# Inst -> print ( Exp ) ;
#       | read ( id ) ;
#       | id = Exp ;
#       | if ( cond ) { Insts } ;
#       | if ( cond ) { Insts } else { Insts } ;
#       | repeat { Insts } until ( cond ) ;
#
# Exp -> Exp '+' Termo
#     |  Exp '-' Termo
#     |  Termo
#
# Termo -> Termo '*' Factor
#       |  Termo '/' Factor
#       |  Termo '%' Factor
#       |  Factor
#
# Factor -> '(' Exp ')'
#         | num
#         | id
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
          'PRINT','READ']

literals = ['(',')','{','}',';']

t_ADD = r'\+'
t_SUB = r'-'
t_MUL = r'\*'
t_DIV = r'/'
t_MOD = r'%'
t_EQ = r'=='
t_ATRIB = r'='
t_AND = r'&'
t_OR = r'#'
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

t_ignore = " \t\n"

def t_error(t):
    print("Caracter ilegal: ",t.value[0])
    t.lexer.skip

lexer = lex.lex()