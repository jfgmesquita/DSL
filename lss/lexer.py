import ply.lex as lex

reserved = {
    'agendar'       : 'AGENDAR',
    'consulta'      : 'CONSULTA',
    # 'indisponibilidade': 'INDISPONIBILIDADE',
    # 'batch'         : 'BATCH',
    # 'def'           : 'DEF',
}

tokens = [
    'IDENTIFIER', 'STRING', 'NUMBER', 'DATE', 'COLON'
] + list(reserved.values())

t_COLON   = r':'
t_ignore  = ' \n\t'

def t_DATE(t):
    r'(0[1-9]|[1-2][0-9]|3[0-1])-(0[1-9]|1[0-2])-(202[5-8])' # DD-MM-YYYY
    return t

def t_IDENTIFIER(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

def t_STRING(t):
    r'"[A-Za-z0-9_\- ]*"'
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
