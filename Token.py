class Token:
    def __init__(self, lexem, type,  line, column):
        self.lexem = lexem
        self.type = type
        self.line = line 
        self.column = column 
        if self.type == 'TITULO' or self.type == 'ANCHO' or self.type == 'ALTO' or self.type == 'FILAS' or self.type == 'COLUMNAS'or self.type == 'CELDAS' or self.type=='SEPARATOR':
            self.color = '\033[4;34m' #azul
        elif self.type == 'open_key' or self.type == 'closed_key' or self.type == 'two_points' or self.type == 'semicolon' or self.type == 'comma'or self.type == 'equals'or self.type == 'quotation_mark' or self.type=='open_square_bracket'or self.type=='closed_square_bracket' or self.type=='hashtag':
            self.color = '\033[4;35m' #rosado
        elif self.type == 'FILTROS' or self.type =="boolean_value":
            self.color = '\033[4;32m' #verde
        elif self.type == 'int_value':
            self.color = '\x1b[1;33m' #amarillo
        elif self.type == 'error_value':
            self.color = '\033[4;31m' #rojo

    def print_token(self):
        print(self.color+" ",self.lexem, self.type, self.line, self.column)
        