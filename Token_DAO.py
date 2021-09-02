from Token import  Token
class Token_DAO:
    def __init__(self):
        self.tokens_list = []
        self.color=""
        
    
    #Función para crear nuevos Errores
    def new_token(self,lexem, type,  line, column):
        new = Token(lexem, type,  line, column)
        self.tokens_list.append(new)
        return True
    
    def print_token(self):
        for token in self.tokens_list:
            if token.type == 'TITULO' or token.type == 'ANCHO' or token.type == 'ALTO' or token.type == 'FILAS' or token.type == 'COLUMNAS'or token.type == 'CELDAS':
                self.color = '\033[4;34m' #azul
            elif token.type == 'open_key' or token.type == 'closed_key' or token.type == 'two_points' or token.type == 'semicolon' or token.type == 'comma'or token.type == 'equals'or token.type == 'quotation_mark' or token.type=='open_square_bracket'or token.type=='closed_square_bracket' or token.type=='hashtag':
                self.color = '\033[4;35m' #rosado
            elif token.type == 'string_value':
                self.color = '\033[4;32m' #verde
            elif token.type == 'int_value':
                self.color = '\x1b[1;33m' #amarillo
            print(self.color+" ",token.lexem,token.type,str(token.line),str(token.column))
    
    def tokens_html_report(self):
        f = open('TOKENS.html','w')
        token_html ="""<html>
        <head></head>
        <body>
        <center>
        <h1>REPORTE DE TOKENS</h1>
        </center>
        <style type="text/css" media="all">
        h1, h2 {display: inline;}
        </style>
        <hr />
        <center>
        <table width="500" border="2" cellpadding="5" >
        <tr>
        <th>TOKEN</th>
        <th>LEXEMA</th>
        <th>FILA</th>
        <th>COLUMNA</th>
        </tr>"""
        for token in self.tokens_list:
            if token.type == 'TITULO' or token.type == 'ANCHO' or token.type == 'ALTO' or token.type == 'FILAS' or token.type == 'COLUMNAS'or token.type == 'CELDAS':
                token_html+="""
                <tr>
                <td bgcolor= "#39BBC4">"""+token.type+"""</td>
                <td bgcolor= "#39BBC4">"""+token.lexem+"""</td>
                <td bgcolor= "#39BBC4">"""+str(token.line)+"""</td>
                <td bgcolor= "#39BBC4">"""+str(token.column)+"""</td>
                </tr>"""
        for token in self.tokens_list:
            if token.type == 'open_key' or token.type == 'closed_key' or token.type == 'two_points' or token.type == 'semicolon' or token.type == 'comma'or token.type == 'equals'or token.type == 'quotation_mark' or token.type=='open_square_bracket'or token.type=='closed_square_bracket' or token.type=='hashtag':
                token_html+="""
                <tr>
                <td bgcolor= "#1DEA38">"""+token.type+"""</td>
                <td bgcolor= "#1DEA38">"""+token.lexem+"""</td>
                <td bgcolor= "#1DEA38">"""+str(token.line)+"""</td>
                <td bgcolor= "#1DEA38">"""+str(token.column)+"""</td>
                </tr>"""
        for token in self.tokens_list:
            if token.type == 'string_value':
                token_html+="""
                <tr>
                <td bgcolor= "#A276B6">"""+token.type+"""</td>
                <td bgcolor= "#A276B6">"""+token.lexem+"""</td>
                <td bgcolor= "#A276B6">"""+str(token.line)+"""</td>
                <td bgcolor= "#A276B6">"""+str(token.column)+"""</td>
                </tr>"""
        for token in self.tokens_list:
            if token.type == 'string_value':
                token_html+="""
                <tr>
                <td bgcolor= "#A276B6">"""+token.type+"""</td>
                <td bgcolor= "#A276B6">"""+token.lexem+"""</td>
                <td bgcolor= "#A276B6">"""+str(token.line)+"""</td>
                <td bgcolor= "#A276B6">"""+str(token.column)+"""</td>
                </tr>"""
        for token in self.tokens_list:
            if token.type == 'int_value':
                token_html+="""
                <tr>
                <td bgcolor= "#E9AC17">"""+token.type+"""</td>
                <td bgcolor= "#E9AC17">"""+token.lexem+"""</td>
                <td bgcolor= "#E9AC17">"""+str(token.line)+"""</td>
                <td bgcolor= "#E9AC17">"""+str(token.column)+"""</td>
                </tr>"""
        token_html+="""
        </table>
        </body>
        </html>"""
        f.write(token_html)
        f.close()