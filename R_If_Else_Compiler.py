'''
CFG FOR IF-ELSE LOOP IN R LANGUAGE ->
S->if A
A->CNS | CNSE | CS | CSE
C->(condition)
S->{Nstatements;N} | {NstatementsN}
N->'\n'(next line)
E->elseNS | elseS
'''


import ply.lex as lex 
import ply.yacc as yacc
tokens=['if','else','condition','statements','next','normalopenbracket','normalclosebracket','curlyopenbracket','curlyclosebracket','semicolon','PLUS','MINUS','TIMES','DIVIDE','letter',];
t_ignore = ' \t';
t_next = ' \\n';
t_curlyopenbracket = r'\{';
t_curlyclosebracket = r'\}';
t_normalopenbracket = r'\(';
t_normalclosebracket = r'\)';
t_semicolon = r';';
t_if=r'if';
t_else=r'else';
t_condition=r'condition';
t_statements=r'statements';
t_PLUS    = r'\+';
t_MINUS   = r'-';
t_TIMES   = r'\*';
t_DIVIDE  = r'/';
t_letter = r'[^\n\r\\/:*?\"<> |0-9]';

def p_if(p):
    '''assign : if expr'''
    print("Syntax is correct .");

def p_expr(p):
    '''expr : conditionsub next statementsub
            | conditionsub next statementsub elsesub
            | conditionsub statementsub
            | conditionsub statementsub elsesub
            '''

def p_conditionsub(p):
    '''conditionsub : normalopenbracket comparisonsub normalclosebracket'''

def p_statementsub(p):
    '''statementsub : curlyopenbracket next statements semicolon next curlyclosebracket
                    | curlyopenbracket next statements next curlyclosebracket
                    '''

def p_elsesub(p):
    '''elsesub : else next statementsub
               pipp| else statementsub 
               '''    

def p_comparisonsub(p):s
    '''comparisonsub : letter PLUS letter  
                     | letter MINUS letter
                     | letter DIVIDE letter
                     | letter TIMES letter
                     '''  

def p_error(p):
  print("Syntax error .");

lex.lex();
yacc.yacc();

data='''if(a>b)
{
    statements
} else
{
    statements
}''';

yacc.parse(data)