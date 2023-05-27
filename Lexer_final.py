import ply.lex as lex

reserved = {

    'read':'read',                'READ':'READ',
    'write':'write',              'WRITE':'WRITE',
    'set':'set',                  'SET':'SET',
    'if':'if',                    'IF':'IF',
    'then':'then',                'THEN':'THEN',
    'else':'else',                'ELSE':'ELSE',
    'endif':'endif',              'ENDIF':'ENDIF',
    'while':'while',              'WHILE':'WHILE',
    'do':'do',                    'DO':'DO',
    'endwhile':'endwhile',        'ENDWHILE':'ENDWHILE',
    'until':'until',              'UNTIL':'UNTIL',
    'enduntil':'enduntil',        'ENDUNTIL':'ENDUNTIL',
    'call':'call',                'CALL':'CALL',
    'integer':'Datatype',         'INTEGER':'Datatype',
    'boolean':'Datatype',         'BOOLEAN':'Datatype',
    'float':'Datatype',           'FLOAT':'Datatype',
    'double':'Datatype',          'DOUBLE':'Datatype',
    'character':'Datatype',       'CHARACTER':'Datatype',
    'string':'Datatype',          'STRING':'Datatype',
    'real': 'Datatype',           'REAL': 'Datatype',
    'int': 'Datatype',            'INT': 'Datatype',
    'str': 'Datatype',            'STR': 'Datatype',
    'char': 'Datatype',           'CHAR': 'Datatype',
    'begin':'begin',              'BEGIN':'BEGIN',
    'end':'end',                  'END':'END',
    'parameters': 'parameters',   'PARAMETERS': 'PARAMETERS',
    'declare': 'declare',         'DECLARE': 'DECLARE',
    'assign' : 'assign',          'ASSIGN' : 'ASSIGN',
    'function' :'function',       'fUNCTION' :'fUNCTION',

}

tokens = [
    'ID',
    'FLOAT',
    'NUMBER',
    'SEMICOLON',
    'LPAREN',
    'RPAREN',
    'string',
    'COMMA',
    'ARITHMETIC_OP',
    'RELATIONAL_OP',
    'Datatype',
    'LCURL',
    'RCURL',
] + list(reserved.values())

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCURL = r'\{'
t_RCURL = r'\}'

t_SEMICOLON = r';'
t_COMMA = r','
t_ARITHMETIC_OP = r'(\+|-|\*|/)'
t_RELATIONAL_OP = r'(<|>|=|!)'
t_ignore = r" [ \t \n]" # A string containing ignored characters (spaces and tabs)
t_Datatype=r'[int float integer INT]'

def t_FLOAT(t):
    r"\d+\.\d+"
    t.value = float(t.value)
    return t


def t_NUMBER(t):
    r'\d+\.\d+|\d+'
    t.value = (t.value)
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_string(t):
    r'\".*\"'
    t.value = (t.value)
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Create the lexer
lexer = lex.lex()