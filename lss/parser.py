import ply.yacc as yacc
from lss.lexer import tokens

# Bloco principal: lista de statements
def p_program(p):
    '''program : statement_list'''
    p[0] = p[1]

def p_statement_list(p):
    '''statement_list : statement
                      | statement_list statement'''
    p[0] = p[1] + [p[2]] if len(p) == 3 else [p[1]]

# Exemplos de statements
def p_statement_agendar(p):
    '''statement : AGENDAR COLON agendar_body'''
    p[0] = ('agendar', dict(p[3]))

def p_agendar_body(p):
    '''agendar_body : field_list'''
    p[0] = p[1]

def p_statement_consulta(p):
    '''statement : CONSULTA COLON field_list'''
    p[0] = ('consulta', dict(p[3]))

# Campos genéricos: IDENTIFIER : valor
def p_field_list(p):
    '''field_list : field
                  | field_list field'''
    p[0] = p[1] + [p[2]] if len(p) == 3 else [p[1]]

def p_field(p):
    '''field : IDENTIFIER COLON value'''
    p[0] = (p[1], p[3])

# Valores possíveis
def p_value_string(p):
    'value : STRING'
    p[0] = p[1]

def p_value_number(p):
    'value : NUMBER'
    p[0] = p[1]

def p_value_date(p):
    'value : DATE'
    p[0] = p[1]

def p_value_identifier(p):
    'value : IDENTIFIER'
    p[0] = p[1]

# Erro de sintaxe
def p_error(p):
    if p:
        print(f"[Parser] Syntax error in {p.value!r} - line {p.lineno}")
    else:
        print("[Parser] Error: Unexpected end of input")

parser = yacc.yacc()
