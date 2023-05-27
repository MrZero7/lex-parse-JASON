import Lexer_final

new_lex = Lexer_final.lexer

#input
input_code = '''
begin
declare int x;
while (x=1) do read y; endwhile
write y;
end
'''

#program begin
def parse_begin(lexer):
    x=match("begin", lexer)
    print("\n\nProgram Begin\n")
    parse_statements_block(lexer)

def get_token(lexer):
    token = get_next_token(lexer)
    return token

def get_next_token(lexer):
    token = lexer.token()
    if token is None:
        return ""
    else:
        return token.type

#this code compare and match a given token
def match(expected_token, lexer):
    token = get_next_token(lexer)
    if token == expected_token:
        return token
    else:
        raise SyntaxError(
            f"Expected token {expected_token}, but found {token}")

def parse_statements_block(lexer):
    while (lexer):
        parse_statement(lexer)
    
#finds the right statment that should be used
def parse_statement(lexer):
    x = get_token(lexer)

    if x == "function":
        parse_function(lexer)
    elif x == "declare":
        parse_declare_statement(lexer)
    elif x == "read":
        parse_read_statement(lexer)
    elif x == "write":
        parse_write_statement(lexer)
    elif x == "assign":
        parse_assign_statement(lexer)
    elif x == "if":
        parse_if(lexer)
    elif x == "while":
        parse_while_loop(lexer)
    elif x== "end" :
        print("\nProgram End")
        exit(1)
    else:
        return

#parses function-------------------------------------------------------
def parse_function(lexer):
    
    match("ID", lexer)
    match("LPAREN", lexer)
    new_dec=parse_func_dec(lexer)
    match("RPAREN", lexer)
    print(f"Function: ID {new_dec}")
    print ("{")
    match("LCURL",lexer)
    parse_statement(lexer)
    match("RCURL",lexer)
    print ("}")

def parse_func_dec(lexer):
    datatype1 = match("Datatype", lexer)
    identifier1 = match("ID", lexer)
    match("COMMA", lexer)
    datatype2 = match("Datatype", lexer)
    identifier2 = match("ID", lexer)
    return (datatype1 ,identifier1,datatype2 ,identifier2)
#end parses function------------------------------------------------------

#parses the declare statement
def parse_declare_statement(lexer):
    
    match("Datatype", lexer)
    match("ID", lexer)
    match("SEMICOLON", lexer)
    print("Declare statement: Datatype ID semicolon\n")


#parses read statement
def parse_read_statement(lexer):

    match("ID", lexer)
    match("SEMICOLON", lexer)
    print("Read statement: read ID semicolon")
    

#parses write statement
def parse_write_statement(lexer):

    match("ID", lexer)
    match("SEMICOLON", lexer)
    print("Write statement: write ID semicolon")

#parses the assign statement
def parse_assign_statement(lexer):
    
    match("ID", lexer)
    match("RELATIONAL_OP", lexer)
    match("NUMBER",lexer)
    match("SEMICOLON", lexer)
    print("Assign statement: ID = NUMBER semicolon")

#parses if statement
def parse_if(lexer):

    print("If statement : IF condition THEN stmt else stmt")
    print("condition: ", end = " ")
    parse_expression(lexer)
    match("THEN", lexer)
    print("\nexpression: ", end = " ")
    parse_statement(lexer)
    match("else", lexer)
    print("expression: ", end = " ")
    parse_statement(lexer)
    match("endif", lexer)
    print("ENDIF\n")
    
#parses while loop
def parse_while_loop(lexer):

    print("While statement: While exp DO exp")
    print("expression: ", end = " ")
    parse_expression(lexer)
    match("do", lexer)
    print("\nexpression: ", end =" ")
    parse_statement(lexer)
    match("endwhile", lexer)
    print("ENDWHILE\n")
    

#parses expression-----------------------------------------
def parse_expression(lexer):
    return parse_arithmetic_expression(lexer)


def parse_arithmetic_expression(lexer):
        parse_term(lexer)

def parse_term(lexer):
    x=get_token(lexer)
    if x == 'LPAREN':

        expression = parse_expression(lexer)
        return expression
    elif x == 'ID':

        identifier = 'ID'
        print(x, end =" ")
        expression = parse_expression(lexer)
        return identifier
    elif x == 'NUMBER':

        number = 'NUMBER'
        print(x, end =" ")
        expression = parse_expression(lexer)
        return number
    elif x == 'RELATIONAL_OP':

        print(x, end =" ")
        expression =parse_arithmetic_expression(lexer)
    elif x == 'ARITHMETIC_OP':

        print(x, end =" ")
        expression =parse_arithmetic_expression(lexer)
    elif x == 'RPAREN':

        return 
    else:
        raise SyntaxError("Invalid factor")
#end parse expression---------------------------------------------------------------


#generate the output
new_lex.input(input_code)
parse_begin(new_lex)