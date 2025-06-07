import ply.lex as lex

reserved = {
    'agendar'            : 'AGENDAR',
    'consulta'           : 'CONSULTA',
    'indisponibilidade'  : 'INDISPONIBILIDADE',
    'ferias'             : 'FERIAS',
    'batch'              : 'BATCH',
    'def'                : 'DEF',
    'if'                 : 'IF',
    'else'               : 'ELSE',
    'and'                : 'AND',
    'or'                 : 'OR',
    'not'                : 'NOT'
}

tokens = [
    'IDENTIFIER', 'STRING', 'NUMBER', 'DATE',
    'COLON', 'EQUALS', 'LPAREN', 'RPAREN',
    'LBRACKET', 'RBRACKET', 'COMMA',
    'EQ', 'NE', 'LT', 'GT'
] + list(reserved.values())

t_COLON    = r':'
t_EQUALS   = r'='
t_LPAREN   = r'\('
t_RPAREN   = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA    = r','
t_EQ       = r'=='
t_NE       = r'!='
t_LT       = r'<'
t_GT       = r'>'
t_ignore   = ' \n\t'

def t_DATE(t):
    r'(0[1-9]|[1-2][0-9]|3[0-1])-(0[1-9]|1[0-2])-(202[5-8])'
    return t

def t_IDENTIFIER(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print(f"[Lexer] Illegal character '{t.value[0]}' - line {t.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()
