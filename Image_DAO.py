from Image import Image
import imgkit
class Image_DAO:
    def __init__(self):
        self.images_list = []
        self.name_images_list=[]
#============================================================================================================
    def new_image(self,name,width,height,rows,cols,filters,colors):
        #================================================================
        rows=int(rows)
        cols=int(cols)
        #================================================================


        #================================================================
        name=name.replace('"',"")
        #================================================================


        #================================================================
        filters=filters.replace(" ","")
        filters=filters.replace("=","")
        filters=filters.split(",")
        #================================================================


        #================================================================
        colors=colors.replace("\n","")
        colors=colors.replace("[","")
        colors=colors.replace("\t","")
        colors=colors.replace("{","")
        colors=colors.split("],")
        for c in range(len(colors)):
            colors[c]=colors[c].split(",")
        #================================================================


        #================================================================
        temp_grid=[]
        for a in range(rows):
            temp_grid.append([])
            for b in range(cols):
                temp_grid[a].append(0)
        #================================================================


        #================================================================
        k=0
        for c in range(len(colors)):
            if colors[k][2]=="TRUE":
                x=colors[k][1]
                y=colors[k][0]
                colors[k][1]=y
                colors[k][0]=x
                temp_grid[int(colors[k][0])][int(colors[k][1])]=colors[k][3]
                
            k+=1
            
        #================================================================


        #================================================================
        new = Image(name,width,height,rows,cols,filters,colors,temp_grid)
        self.images_list.append(new)
        self.images_report(name,temp_grid,rows,cols,width,height,filters)
        print("se creo con exito!!!!")
        #print(reversed(temp_grid))
        return True
        #================================================================
#============================================================================================================

    def print_image(self):
        for image in self.images_list:
            print(image.name,image.width, image.height, image.rows, image.cols,image.filters,"\n\n\n",image.grid)
    
    def images_name_collector(self):
        for image in self.images_list:
            print(image.name)
            self.name_images_list=[*self.name_images_list,image.name]
    
    def html_collecotr(self):
        for image in self.images_list:
            imgkit.from_file("ImagesReports/"+image.name+'.html',"jpg/"+image.name+'.jpg')
    
    def filters_by_name(self,name):
        for image in self.images_list:
            if image.name==name:
                return image.filters
    
    def dimensions_by_name(self,name):
        for image in self.images_list:
            if image.name==name:
                return image.width,"X",image.height



    def images_report(self,name,matrix,rows,cols,width,height,filters):
        mirrory=[]
        #mirrory+=reversed(matrix)
        mirrorx=[]
        doublemirror=[]
        #Para rotar 90 grados
        '''for m in range(len(matrix[0])):
            dm.append([])
            for n in range(len(matrix)):
                dm[m].append(matrix[len(matrix)-1-n][m])'''
        #MIRROR Y
        mirrory += list(matrix[::-1])
        mirrory.extend(matrix[1:])
        for j in range(len(matrix)):
            fila=matrix[j][::-1]
            mirrorx.append(fila)
        doublemirror+=list(mirrorx[::-1])
        doublemirror.extend(mirrorx[1:])
        f = open("ImagesReports/"+name+".html",'w')
        images_html ='''<html>
        <head></head>
        <body bgcolor="19D1C2">
        <center>
        <h1>'''+name+'''--ORIGINAL</h1>
        </center>
        <style type="text/css" media="all">
        h1, h2 {display: inline;}
        </style>
        <hr />
        <center>
        <table width="'''+width+'''" height="'''+height+'''" border="2" cellpadding="0"  bordercolor="#000000">'''
        for i in range(0,rows):
            images_html+="""<tr>"""
            for j in  range(0,cols):
                if matrix[i][j]!=0:
                    images_html+='''
                    <td bgcolor= "'''+matrix[i][j]+'''"></td>'''
                else:
                    images_html+='''
                    <td bgcolor=#FFFFFF ""></td>'''
            images_html+='''</tr>'''

        images_html+='''
        </table>'''
        #==========================================================================
        if filters.count("MIRRORY")>=1:
            images_html+='''
            <center>
            <h1>'''+name+'''---MIRRORY</h1>
            </center>
            <style type="text/css" media="all">
            h1, h2 {display: inline;}
            </style>
            <hr />
            <center>
            <table width="'''+width+'''" height="'''+height+'''" border="2" cellpadding="0" bordercolor="#000000">'''
            for i in range(0,rows):
                images_html+="""<tr>"""
                for j in  range(0,cols):
                    if mirrory[i][j]!=0:
                        images_html+='''
                        <td bgcolor= "'''+mirrory[i][j]+'''"></td>'''
                    else:
                        images_html+='''
                        <td bgcolor=#FFFFFF ""></td>'''
                images_html+='''</tr>'''

            images_html+='''
            </table>'''
        #==========================================================================
        if filters.count("MIRRORX")>=1:
            images_html+='''
            <center>
            <h1>'''+name+'''---MIRRORX</h1>
            </center>
            <style type="text/css" media="all">
            h1, h2 {display: inline;}
            </style>
            <hr />
            <center>
            <table width="'''+width+'''" height="'''+height+'''" border="2" cellpadding="0" bordercolor="#000000" >'''
            for i in range(0,rows):
                images_html+="""<tr>"""
                for j in  range(0,cols):
                    if mirrorx[i][j]!=0:
                        images_html+='''
                        <td bgcolor= "'''+mirrorx[i][j]+'''"></td>'''
                    else:
                        images_html+='''
                        <td bgcolor=#FFFFFF ""></td>'''
                images_html+='''</tr>'''

            images_html+='''
            </table>'''

        #==========================================================================
        if filters.count("DOUBLEMIRROR")>=1:
            images_html+='''
            <center>
            <h1>'''+name+'''---DOUBLE MIRROR</h1>
            </center>
            <style type="text/css" media="all">
            h1, h2 {display: inline;}
            </style>
            <hr />
            <center>
            <table width="'''+width+'''" height="'''+height+'''" border="2" cellpadding="0" bordercolor="#000000">'''
            for i in range(0,rows):
                images_html+="""<tr>"""
                for j in  range(0,cols):
                    if doublemirror[i][j]!=0:
                        images_html+='''
                        <td bgcolor= "'''+doublemirror[i][j]+'''"></td>'''
                    else:
                        images_html+='''
                        <td bgcolor=#FFFFFF ""></td>'''
                images_html+='''</tr>'''

            images_html+='''
            </table>'''
        images_html+='''
        </body>
        </html>'''
        f.write(images_html)
        f.close()
    def validate_image(self,name):
        filters_temp=""
        temp_gridd=[]
        width_temp=0
        height_temp=0
        rows_temp=0
        cols_temp=0
        for image in self.images_list:
            if image.name==name:
                filters_temp=image.filters
                temp_gridd+=image.grid
                width_temp=image.width
                height_temp=image.height
                rows_temp=image.rows
                cols_temp=image.cols
        self.original_image_maker(name,temp_gridd,width_temp,height_temp,rows_temp,cols_temp)
        mirrory_temp=[]
        mirrory_temp+=reversed(temp_gridd)
        mirrorx_temp=[]
        doublemirror_temp=[]
        for j in range(len(temp_gridd)):
            fi=temp_gridd[j][::-1]
            mirrorx_temp.append(fi)
        doublemirror_temp+=reversed(mirrorx_temp)
        if filters_temp.count("MIRRORX")>=1:
            self.mirrorx_image_maker(name,mirrorx_temp,width_temp,height_temp,rows_temp,cols_temp)
        if filters_temp.count("MIRRORY")>=1:
            self.mirrory_image_maker(name,mirrory_temp,width_temp,height_temp,rows_temp,cols_temp)
        if filters_temp.count("DOUBLEMIRROR")>=1:
            self.double_image_maker(name,doublemirror_temp,width_temp,height_temp,rows_temp,cols_temp)
            

        
    def original_image_maker(self,name,grid,width,height,rows,cols):
        print(width,height)
        f = open("temp.html",'w')
        temp_html ='''<html>
        <head></head>
        <body bgcolor="19D1C2">
        <table width="'''+width+'''" height="'''+height+'''" border="2" cellpadding="0"  bordercolor="#000000">'''
        for i in range(0,rows):
            temp_html+="""<tr>"""
            for j in  range(0,cols):
                if grid[i][j]!=0:
                    temp_html+='''
                    <td bgcolor= "'''+grid[i][j]+'''"></td>'''
                else:
                    temp_html+='''
                    <td bgcolor=#FFFFFF ""></td>'''
            temp_html+='''</tr>'''

        temp_html+='''
        </table>'''
        temp_html+='''
        </body>
        </html>'''
        f.write(temp_html)
        f.close()
        options = {
            'width':width,
            'height':height
        }
        imgkit.from_file("temp.html","jpg/"+name+'ORIGINAL.png',options=options)

    def mirrorx_image_maker(self,name,grid,width,height,rows,cols):
        f = open("temp.html",'w')
        temp_html ='''<html>
        <head></head>
        <body bgcolor="19D1C2">
        <table width="'''+width+'''" height="'''+height+'''" border="2" cellpadding="0"  bordercolor="#000000">'''
        for i in range(0,rows):
            temp_html+="""<tr>"""
            for j in  range(0,cols):
                if grid[i][j]!=0:
                    temp_html+='''
                    <td bgcolor= "'''+grid[i][j]+'''"></td>'''
                else:
                    temp_html+='''
                    <td bgcolor=#FFFFFF ""></td>'''
            temp_html+='''</tr>'''

        temp_html+='''
        </table>'''
        temp_html+='''
        </body>
        </html>'''
        f.write(temp_html)
        f.close()
        options = {
            'width':width,
            'height':height
        }
        imgkit.from_file("temp.html","jpg/"+name+'MIRRORX.png',options=options)
    def mirrory_image_maker(self,name,grid,width,height,rows,cols):
        f = open("temp.html",'w')
        temp_html ='''<html>
        <head></head>
        <body bgcolor="19D1C2">
        <table width="'''+width+'''" height="'''+height+'''" border="2" cellpadding="0"  bordercolor="#000000">'''
        for i in range(0,rows):
            temp_html+="""<tr>"""
            for j in  range(0,cols):
                if grid[i][j]!=0:
                    temp_html+='''
                    <td bgcolor= "'''+grid[i][j]+'''"></td>'''
                else:
                    temp_html+='''
                    <td bgcolor=#FFFFFF ""></td>'''
            temp_html+='''</tr>'''

        temp_html+='''
        </table>'''
        temp_html+='''
        </body>
        </html>'''
        f.write(temp_html)
        f.close()
        options = {
            'width':width,
            'height':height
        }
        imgkit.from_file("temp.html","jpg/"+name+'MIRRORY.png',options=options)
    def double_image_maker(self,name,grid,width,height,rows,cols):
        f = open("temp.html",'w')
        temp_html ='''<html>
        <head></head>
        <body bgcolor="19D1C2">
        <table width="'''+width+'''" height="'''+height+'''" border="2" cellpadding="0"  bordercolor="#000000">'''
        for i in range(0,rows):
            temp_html+="""<tr>"""
            for j in  range(0,cols):
                if grid[i][j]!=0:
                    temp_html+='''
                    <td bgcolor= "'''+grid[i][j]+'''"></td>'''
                else:
                    temp_html+='''
                    <td bgcolor=#FFFFFF ""></td>'''
            temp_html+='''</tr>'''

        temp_html+='''
        </table>'''
        temp_html+='''
        </body>
        </html>'''
        f.write(temp_html)
        f.close()
        options = {
            'width':width,
            'height':height
        }
        imgkit.from_file("temp.html","jpg/"+name+'DOUBLE.png',options=options)
        print("")
