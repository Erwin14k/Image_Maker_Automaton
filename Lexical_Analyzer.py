from Token_DAO import Token_DAO
from os import error
from Token import Token
from Error import Error
from Error_DAO import Error_DAO
import re

error_handler=Error_DAO()
token_handler=Token_DAO()

class Lexical_Analyzer:
    def __init__(self):
        self.tokens_list = []
        self.errors_list = []
        
    def analyze2(self, original_text):
        self.tokens_list = []
        self.errors_list = []

        #inicializar atributos
        line = 1
        column = 1
        buffer = ''
        sentinel = '$'
        state = 0
        original_text += sentinel

        #automata
        i = 0
        while i< len(original_text):
            c = original_text[i]
            #=======================================================================================
            #Estado 0, donde dependiendo lo recolectado ira cambiando de estado
            if state == 0:
                #Si encuentra una letra, se irá al estado 1
                if re.search('[a-z]', c) or re.search('[A-Z]', c):
                    buffer += c
                    column += 1
                    state = 1
                elif c == '=':
                    buffer += c
                    token_handler.new_token(buffer, 'equals', line, column)
                    buffer = ''
                    column += 1
                    #state=3
                elif c == '"':
                    buffer += c
                    token_handler.new_token(buffer, 'quotation_mark', line, column)
                    buffer = ''
                    column += 1
                    state=4
                elif c == '}':
                    buffer += c
                    token_handler.new_token(buffer, 'closed_key', line, column)
                    buffer = ''
                    column += 1
                    #state=3
                elif c == '{':
                    buffer += c
                    token_handler.new_token(buffer, 'open_key', line, column)
                    buffer = ''
                    column += 1
                    #state=3
                elif c == ';':
                    buffer += c
                    token_handler.new_token(buffer, 'semicolon', line, column)
                    buffer = ''
                    column += 1
                    #state=3
                elif c == ',':
                    buffer += c
                    token_handler.new_token(buffer, 'comma', line, column)
                    buffer = ''
                    column += 1
                    #state=3
                elif c == '[':
                    buffer += c
                    token_handler.new_token(buffer, 'open_square_bracket', line, column)
                    buffer = ''
                    column += 1
                    #state=3
                elif c == ']':
                    buffer += c
                    token_handler.new_token(buffer, 'closed_square_bracket', line, column)
                    buffer = ''
                    column += 1
                    #state=3
                elif c == '#':
                    buffer += c
                    column += 1
                    state = 5
                elif c.isdigit():
                    buffer += c
                    column += 1
                    state = 2
                elif c=="@":
                    buffer += c
                    column += 1
                    state = 11
                elif c == '\n':
                    line += 1
                    column = 1
                elif c == '\t':
                    column += 1
                elif c == ' ':
                    column += 1
                elif c == '\r':
                    pass
                elif c == sentinel:
                    print('Se aceptó la cadena!')
                    break
                else:
                    buffer += c
                    error_handler.new_error('Caracter ' + buffer + ' no reconocido en el lenguaje.'
                    , 'Léxico', line, column)
                    buffer = ''
                    column += 1
            #=======================================================================================
            
            
            
            
            #=======================================================================================
            #Estado 1, donde solo acepta letras, por lo tanto si es diferente regresa a estado 0
            elif state == 1:
                if re.search('[a-z]', c) or re.search('[A-Z]', c):
                    buffer += c
                    column += 1
                else:
                    if buffer == 'TITULO':
                        token_handler.new_token(buffer, 'TITULO', line, column)
                    elif buffer == 'ANCHO':
                        token_handler.new_token(buffer, 'ANCHO', line, column)
                    elif buffer == 'ALTO':
                        token_handler.new_token(buffer, 'ALTO', line, column)
                    elif buffer == 'COLUMNAS':
                        token_handler.new_token(buffer, 'COLUMNAS', line, column)
                    elif buffer == 'FILAS':
                        token_handler.new_token(buffer, 'FILAS', line, column)
                    elif buffer == 'CELDAS':
                        token_handler.new_token(buffer, 'CELDAS', line, column)
                    else:
                        token_handler.new_token(buffer, 'string_value', line, column)
                    buffer = ''
                    i -= 1
                    state = 0
            #=======================================================================================




            #=======================================================================================
            #Estado 2, donde solo acepta números, por lo tanto si es diferente regresa a estado 0
            elif state == 2:
                if c.isdigit():
                    buffer += c
                    column += 1
                else:
                    token_handler.new_token(buffer, 'int_value', line, column)
                    buffer = ''
                    i -= 1
                    state = 0
            #=======================================================================================




            #=======================================================================================
            #Estado 4, viene de recibir " en el estado 0
            elif state==4:
                if re.search('[a-z]', c):
                    buffer += c
                    buffer = ''
                    column += 1
                elif c=='"':
                    buffer += c
                    buffer = ''
                    column += 1
                    state=0
            #=======================================================================================




            #=======================================================================================
            #Estado 5, viene de recibir # en el estado 0
            elif state==5:
                if re.search('[a-z]', c) or c.isdigit() or re.search('[A-Z]', c):
                    column+=1
                    buffer=""
                    state=6
                else:
                    buffer += c
                    error_handler.new_error('Caracter ' + buffer + ' no reconocido en el lenguaje.'
                    , 'Léxico', line, column)
                    buffer = ''
                    column += 1
            #=======================================================================================




            #=======================================================================================
            #Estado 6, viene de recibir Letra|número en el estado 5
            elif state==6:
                if re.search('[a-z]', c) or c.isdigit() or re.search('[A-Z]', c):
                    column+=1
                    buffer=""
                    state=7
                else:
                    buffer += c
                    error_handler.new_error('Caracter ' + buffer + ' no reconocido en el lenguaje.'
                    , 'Léxico', line, column)
                    buffer = ''
                    column += 1
            #=======================================================================================




            #=======================================================================================
            #Estado 7, viene de recibir Letra|número en el estado 6
            elif state==7:
                if re.search('[a-z]', c) or c.isdigit() or re.search('[A-Z]', c):
                    column+=1
                    buffer=""
                    state=8
                else:
                    buffer += c
                    error_handler.new_error('Caracter ' + buffer + ' no reconocido en el lenguaje.'
                    , 'Léxico', line, column)
                    buffer = ''
                    column += 1
            #=======================================================================================




            #=======================================================================================
            #Estado 8, viene de recibir Letra|número en el estado 7
            elif state==8:
                if re.search('[a-z]', c) or c.isdigit() or re.search('[A-Z]', c):
                    column+=1
                    buffer=""
                    state=9
                else:
                    buffer += c
                    error_handler.new_error('Caracter ' + buffer + ' no reconocido en el lenguaje.'
                    , 'Léxico', line, column)
                    buffer = ''
                    column += 1
            #=======================================================================================




            #=======================================================================================
            #Estado 9, viene de recibir Letra|número en el estado 8
            elif state==9:
                if re.search('[a-z]', c) or c.isdigit() or re.search('[A-Z]', c):
                    column+=1
                    buffer=""
                    state=10
                else:
                    buffer += c
                    error_handler.new_error('Caracter ' + buffer + ' no reconocido en el lenguaje.'
                    , 'Léxico', line, column)
                    buffer = ''
                    column += 1
            #=======================================================================================




            #=======================================================================================
            #Estado 10, viene de recibir Letra|número en el estado 9
            elif state==10:
                if re.search('[a-z]', c) or c.isdigit() or re.search('[A-Z]', c):
                    column+=1
                    buffer=""
                    state=0
                else:
                    buffer += c
                    error_handler.new_error('Caracter ' + buffer + ' no reconocido en el lenguaje.'
                    , 'Léxico', line, column)
                    buffer = ''
                    column += 1
        
            #=======================================================================================




            #=======================================================================================
            #Estado 11, viene de recibir @ en el estado 0
            elif state==11:
                if c=="@":
                    column+=1
                    buffer=""
                    state=12
                else:
                    buffer += c
                    error_handler.new_error('Caracter ' + buffer + ' no reconocido en el lenguaje.'
                    , 'Léxico', line, column)
                    buffer = ''
                    column += 1
            #=======================================================================================




            #=======================================================================================
            #Estado 12, viene de recibir @ en el estado 11
            elif state==12:
                if c=="@":
                    column+=1
                    buffer=""
                    state=13
                else:
                    buffer += c
                    error_handler.new_error('Caracter ' + buffer + ' no reconocido en el lenguaje.'
                    , 'Léxico', line, column)
                    buffer = ''
                    column += 1
            #=======================================================================================




            #=======================================================================================
            #Estado 13, viene de recibir @ en el estado 12
            elif state==13:
                if c=="@":
                    column+=1
                    buffer=""
                    state=0
                else:
                    buffer += c
                    error_handler.new_error('Caracter ' + buffer + ' no reconocido en el lenguaje.'
                    , 'Léxico', line, column)
                    buffer = ''
                    column += 1
            #=======================================================================================
            i += 1

    def print_tokens(self):
        token_handler.print_token()

    def print_errors(self):
        if len(error_handler.errors_list) == 0:
            print('No hubo errores')
        else:
            error_handler.print_error()

