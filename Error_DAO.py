from Error import  Error
class Error_DAO:
    def __init__(self):
        self.errors_list = []
        
    
    #Función para crear nuevos Errores
    def new_error(self,description, type, line, column):
        new = Error(description, type, line, column)
        self.errors_list.append(new)
        return True

    def print_error(self):
        for error in self.errors_list:
            print(error.description,error.type,str(error.line),str(error.column))

    def errors_html_report(self):
        f = open('Reportes/ERRORS.html','w')
        error_html ="""<html>
        <head></head>
        <body>
        <center>
        <h1>REPORTE DE ERRORES</h1>
        </center>
        <style type="text/css" media="all">
        h1, h2 {display: inline;}
        </style>
        <hr />
        <center>
        <table width="500" border="2" cellpadding="5" >
        <tr>
        <th>DESCRIPCIÓN</th>
        <th>TIPO</th>
        <th>FILA</th>
        <th>COLUMNA</th>
        </tr>"""
        for error in self.errors_list:
            error_html+="""
            <tr>
            <td bgcolor= "#FF0F0F">"""+error.description+"""</td>
            <td bgcolor= "#FF0F0F">"""+error.type+"""</td>
            <td bgcolor= "#FF0F0F">"""+str(error.line)+"""</td>
            <td bgcolor= "#FF0F0F">"""+str(error.column)+"""</td>
            </tr>"""
        error_html+="""
        </table>
        </body>
        </html>"""
        f.write(error_html)
        f.close()