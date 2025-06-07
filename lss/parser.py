import ply.yacc as yacc
from lss.lexer import tokens

def p_program(p):
    '''program : statement_list'''
    p[0] = p[1]

def p_statement_list(p):
    '''statement_list : statement
                      | statement_list statement'''
    p[0] = p[1] + [p[2]] if len(p) == 3 else [p[1]]

def p_statement_agendar(p):
    'statement : AGENDAR COLON field_block'
    p[0] = ('agendar', dict(p[3]))

def p_statement_consulta(p):
    'statement : CONSULTA COLON field_block'
    p[0] = ('consulta', dict(p[3]))

def p_statement_indisponibilidade(p):
    'statement : INDISPONIBILIDADE COLON field_block'
    p[0] = ('indisponibilidade', dict(p[3]))

def p_statement_ferias(p):
    'statement : FERIAS COLON field_block'
    p[0] = ('ferias', dict(p[3]))

def p_statement_batch(p):
    'statement : BATCH COLON statement_list'
    p[0] = ('batch', p[3])

def p_statement_def(p):
    'statement : DEF IDENTIFIER LPAREN RPAREN COLON field_block'
    p[0] = ('def', p[2], dict(p[6]))

def p_statement_call(p):
    'statement : call_expr'
    p[0] = p[1]

def p_call_expr(p):
    'call_expr : IDENTIFIER LPAREN RPAREN'
    p[0] = ('call', p[1])

def p_statement_if_else(p):
    'statement : IF expression COLON block ELSE COLON block'
    p[0] = ('if', p[2], p[4], p[7])

def p_statement_assign(p):
    'statement : IDENTIFIER EQUALS value'
    p[0] = ('assign', p[1], p[3])

def p_block(p):
    '''block : statement_list
             | field_block'''
    p[0] = p[1]

def p_field_block(p):
    '''field_block : field_line
                   | field_block field_line'''
    p[0] = p[1] + [p[2]] if len(p) == 3 else [p[1]]

def p_field_line(p):
    'field_line : IDENTIFIER COLON value'
    p[0] = (p[1], p[3])

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

def p_value_list(p):
    'value : LBRACKET list_items RBRACKET'
    p[0] = p[2]

def p_list_items(p):
    '''list_items : value
                  | list_items COMMA value'''
    p[0] = p[1] + [p[3]] if len(p) == 4 else [p[1]]

def p_value_block(p):
    'value : field_block'
    p[0] = dict(p[1])

def p_value_expression(p):
    'value : expression'
    p[0] = p[1]

def p_value_call(p):
    'value : call_expr'
    p[0] = p[1]

def p_expression_binop(p):
    '''expression : value EQ value
                  | value NE value
                  | value LT value
                  | value GT value
                  | expression AND expression
                  | expression OR expression'''
    p[0] = (p[2], p[1], p[3])

def p_expression_not(p):
    'expression : NOT expression'
    p[0] = ('not', p[2])

def p_error(p):
    if p:
        print(f"[Parser] Syntax error in {p.value!r} - line {p.lineno}")
    else:
        print("[Parser] Error: Unexpected end of input")

parser = yacc.yacc()
