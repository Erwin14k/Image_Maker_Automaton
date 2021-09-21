import os
from Token_DAO import Token_DAO
from tkinter import *
from tkinter.ttk import Combobox
from Lexical_Analyzer import Lexical_Analyzer
from tkinter.filedialog import askopenfilename
from Token import Token
from tkinter import messagebox
from Lexical_Analyzer import token_handler,error_handler
from Image_DAO  import Image_DAO
import re
import webbrowser as wb
lexical_analyzer_handler=Lexical_Analyzer()
image_dao_handler=Image_DAO()
current_image=""
current_filter=""
jpg_route="C:/Users/Erwin14k/Documents/Image_Maker_Automaton/jpg/"
#============================================================================================================
#Creación de la raíz aplicando algunos atributos
root=Tk()
root.title("Image Maker v1.0")
root.resizable(False,False)
root.iconbitmap("img/cobra_kai.ico")
root.config(cursor="hand2")
root.geometry("1200x600")
root.config(bg="Gold")
root.config(relief="groove")
root.config(bd="30")
#============================================================================================================




#============================================================================================================
#Creación del frame principal aplicando algunos atributos y elementos
main_frame=Frame(root,width="650",height="430")
main_frame.pack()
main_frame.config(bg="black")
main_frame.config(bd="20")
main_frame.config(relief="groove")
main_frame.config(cursor="hand2")
#Label del titulo del frame principal
Label(main_frame,text="IMAGE MAKER",fg="gold",font=("Comic Sans MS",30),bg="black").place(x=170,y=20)
#Label que contendrá una imagen del logo principal y el botón de inicio
logo_image=PhotoImage(file="img/cobra.png")
Label(main_frame,image=logo_image,bg="black").place(x=170,y=80)
#Botón para iniciar la aplicación
principal_Button=Button()
principal_Button.config(text="Iniciar", width="25",height="1",bg="black",fg="gold",font=("Comic Sans MS",20))
principal_Button.pack()
#============================================================================================================




#============================================================================================================
#Creación del frame con todas las funciones 
master_frame=Frame(root,width="650",height="100")
master_frame.config(bg="red")
master_frame.config(bd="20")
master_frame.config(relief="groove")
master_frame.config(cursor="hand2")
upload_Button=Button(master_frame,text="Cargar Archivo",font=("Comic Sans MS",10),bg="black",fg="yellow")
upload_Button.grid(row=0,column=0,padx=10)
analyze_Button=Button(master_frame,text="Analizar Archivo",font=("Comic Sans MS",10),bg="black",fg="yellow")
analyze_Button.grid(row=0,column=1,padx=10)
reports_Button=Button(master_frame,text="Reportes",font=("Comic Sans MS",10),bg="black",fg="yellow")
reports_Button.grid(row=0,column=2,padx=10)
images_Button=Button(master_frame,text="Generar Imágenes",font=("Comic Sans MS",10),bg="black",fg="yellow")
images_Button.grid(row=0,column=3,padx=10)
exit_Button=Button(master_frame,text=" Salir",font=("Comic Sans MS",10),bg="black",fg="yellow")
exit_Button.grid(row=0,column=4,padx=10)
#============================================================================================================




#============================================================================================================
#Creación del frame donde se muestran todos los filtros
filter_frame=Frame(root,width="650",height="430")
filter_frame.config(bg="gold")
original_Button=Button(filter_frame,text="Original",font=("Comic Sans MS",20),bg="black",fg="yellow")
original_Button.grid(row=0,column=0,pady=10)
original_Button.config(width=20)
mirrorx_Button=Button(filter_frame,text="Mirror X",font=("Comic Sans MS",20),bg="black",fg="yellow")
mirrorx_Button.grid(row=1,column=0,pady=10)
mirrorx_Button.config(width=20)
mirrory_Button=Button(filter_frame,text="Mirror Y",font=("Comic Sans MS",20),bg="black",fg="yellow")
mirrory_Button.grid(row=2,column=0,pady=10)
mirrory_Button.config(width=20)
double_mirror_Button=Button(filter_frame,text="Double Mirror",font=("Comic Sans MS",20),bg="black",fg="yellow")
double_mirror_Button.grid(row=3,column=0,pady=10)
double_mirror_Button.config(width=20)
#Variable que almacenará los valores del combobox
options_list=[]
#Creación del combobox para elegir la imagen
images_combobox=Combobox(filter_frame,width="50",state="readonly")
#Botón para seleccionar la imagen del combobox
image_selected_button=Button(filter_frame,text="Buscar Imagen",font=("Comic Sans MS",20),bg="black",fg="yellow")
#============================================================================================================




#============================================================================================================
#Creación de un frame que servirá como division
division_frame=Frame(root,width="100",height="100",bg="gold")
#============================================================================================================




#============================================================================================================
#Creación del botón donde se muestra la imagen
image_frame=Frame(root,width="650",height="470")
image_frame.grid_propagate(FALSE)
image_frame.config(relief="groove")
image_frame.config(cursor="hand2")
img=PhotoImage(file="")
image_label=Label(image_frame,bg="red")
image_label.grid(row=2,column=2)
size_label=Label(bg="gold",text="Tamaño de la imagen :",font=("Comic Sans MS",30))





#============================================================================================================




#============================================================================================================
#Función encargada de iniciar la aplicación
def master_mind_window():
    main_frame.destroy()
    principal_Button.destroy()
    root.geometry("1400x600")
    master_frame.grid(row=0,column=0)
    filter_frame.grid(row=1,column=0)
    division_frame.grid(row=1,column=1)
    image_frame.grid(row=1,column=2)
    size_label.grid(row=0,column=2)
#Con este botón inicializamos esta función
principal_Button.config(command=master_mind_window)
#============================================================================================================    



#============================================================================================================
#Función que termina con la ejecución de la aplicación
def exit_application():
    messagebox.showinfo(title="Image Maker V1.0",message="Vuelve pronto Crack!!")
    exit()
exit_Button.config(command=exit_application)
#============================================================================================================




#============================================================================================================
#Función para cargar el archivo con extensión "pxla" a memoria.
route=""
original_text=""
images_counter=0
temp_text=""
images_data=[]
def upload_file():
    global route,original_text,images_counter,options_list,images_combobox,image_selected_button,temp_text
    route = askopenfilename()
    if route.endswith("pxla"):
        archive = open(route,"r")
        original_text=archive.read()
        archive.close()
        temp_text=original_text
        messagebox.showinfo(title="Image Maker V1.0",message="El archivo fue cargado con éxito al sistema!!")
    else:
        messagebox.showerror(title="Image Maker V1.0",message="No es un archivo con extensión 'pxla', intenta de nuevo!!")
        upload_file()
upload_Button.config(command=upload_file)
#============================================================================================================





#============================================================================================================
def image_attributes(data):
    #print(data)
    j=0
    buffer=""
    name2=""
    rows2=""
    cols2=""
    width2=""
    height2=""
    filters2=""
    colors2=""
    jiu=0
    state=0
    sentinel="$"
    for x in range(len(data)):
        i=0
        temp=data[j]
        temp+=sentinel
        for c in temp:
            if state==0:
                if re.search('[A-Z]', c) or c=="="  :
                    buffer += c
                    state=1
                elif c == '"':
                    buffer += c
                    buffer = ""
                    state=2
                elif c == '\n':
                    jiu=0
                elif c=="{":
                    buffer+=c
                    buffer=""
                    state=8
                elif c == '\t':
                    jiu=0
                elif c == ' ':
                    jiu=0
                elif c == '\r':
                    jiu=0
                    pass
                elif c==sentinel:
                    image_dao_handler.new_image(name2,width2,height2,rows2,cols2,filters2,colors2)
                    j+=1
                    break
                else:
                    buffer += c
                    buffer = ''
            #===============================================================================
            elif state ==1:
                if re.search('[A-Z]', c)  or c=='=':
                    buffer += c
                else:
                    if c=='"':
                        buffer +=c
                        buffer=""
                        state=2
                    elif buffer=="ANCHO=":
                        buffer=""
                        state=3
                    elif buffer=="ALTO=":
                        buffer=""
                        state=4
                    elif buffer=="FILAS=":
                        buffer=""
                        state=5
                    elif buffer=="COLUMNAS=":
                        buffer=""
                        state=6
                    elif buffer=="FILTROS":
                        print("filtros",name2)
                        buffer=""
                        state=7
                    elif buffer=="FILTROS=":
                        print("filtros",name2)
                        buffer=""
                        state=7
                    else:
                        buffer =""
                        state=0
            #===============================================================================
            if state==2: 
                if re.search('[a-z]', c) or re.search('[A-Z]', c) or c=='"':
                        buffer += c

                else: 
                    name2=buffer
                    name2.replace('"',"") 
                    buffer+=c
                    buffer = ''
                    state=0
            #===============================================================================
            elif state==3:
                if c.isdigit() :
                    buffer+=c
                else:
                    width2=buffer
                    buffer=""
                    state=0
            #===============================================================================
            elif state==4:
                if c.isdigit() :
                    buffer+=c
                else:
                    height2=buffer
                    buffer=""
                    state=0
            #===============================================================================
            elif state==5:
                if c.isdigit() :
                    buffer+=c
                else:
                    rows2=buffer
                    buffer=""
                    state=0
            #===============================================================================
            elif state==6:
                if c.isdigit() :
                    buffer+=c
                else:
                    cols2=buffer
                    buffer=""
                    state=0
            #===============================================================================
            elif state==7:
                if c==" "  or c=="=" or re.search('[A-Z]', c) or c=="," or c=="\t":
                    buffer+=c
                    print(c)
                else:
                    print(buffer,"=0000000000000000000000000000000000000000000000000000000000")
                    filters2=buffer
                    buffer=""
                    state=0
            #===============================================================================
            elif state==8:
                if c=="["  or c.isdigit() or re.search('[A-Z]', c) or c=="," or c=="#" or c=="]" or c=="\n" or c=="{" or c=="\t" or c==" ":
                    buffer+=c
                else:
                    colors2=buffer
                    buffer=""
                    state=0
            #===============================================================================        
    #image_dao_handler.print_image()
    print("")

#============================================================================================================



#============================================================================================================
#Función para generar las imagenes en formato html
def images_generator():
    global temp_text,images_counter,options_list,images_data,images_combobox,image_selected_button
    counter=0
    temp_text.replace("\t","")
    images_counter=(temp_text.count("@@@@"))+1
    for x in range(images_counter):
        if temp_text.count("@@@@")>=1:
            temp=temp_text[counter:temp_text.find("@@@@")+4]
            images_data.append(temp)
            temp_text=temp_text[temp_text.find("@@@@")+4:len(temp_text)]
        else:
            temp=temp_text
            images_data.append(temp)
    image_attributes(images_data)
    image_dao_handler.images_name_collector()
    options_list+=image_dao_handler.name_images_list
    images_combobox.grid(row=4,column=0)
    image_selected_button.grid(row=5,column=0,pady=10)
    images_combobox.config(values=options_list)
    
    messagebox.showinfo(title="Image Maker V1.0",message="Archivos Html de las imágenes Generados!!")
images_Button.config(command=images_generator)

#============================================================================================================




#============================================================================================================
#Función para analizar el texto recolectado.
def analyze_file():
    global original_text
    try:
        lexical_analyzer_handler.analyze_file(original_text)
        print("\n\n\n\n\n\n\n")
        lexical_analyzer_handler.print_errors()
        print("\n\n\n\n\n\n\n")
        lexical_analyzer_handler.print_tokens()
        messagebox.showinfo(title="Image Maker V1.0",message="El archivo se analizó con éxito!!")
    
    except:
        messagebox.showerror(title="Image Maker V1.0",message="El archivo No pudo analizarse, intenta de nuevo!!")
        analyze_file()
    
analyze_Button.config(command=analyze_file)
#============================================================================================================




#============================================================================================================
#Función para recolectar información de la imagen solicitada
def search_information():
    global images_combobox,image_selected_button,current_image,size_label
    temp_dimensions=""
    if images_combobox.get()!="":
        current_image=images_combobox.get()
        temp_dimensions=image_dao_handler.dimensions_by_name(current_image)
        image_dao_handler.validate_image(current_image)
        messagebox.showinfo(title="Image Maker V1.0", message="La información de la imagen: "+images_combobox.get()
        +"\nHa sido procesada!!\nPuedes continuar seleccionando los filtros!!")
        size_label.config(text=temp_dimensions)

    else:
        messagebox.showerror(title="Image Maker V1.0", message="No has seleccionado ninguna imagen!!")
image_selected_button.config(command=search_information)
#============================================================================================================




#============================================================================================================
#Función para recolectar información de la imagen solicitada
def reports_view():
    token_handler.tokens_html_report()
    error_handler.errors_html_report()
    messagebox.showinfo(title="Image Maker V1.0", message="Se Abrirán Los siguientes Reportes:\n-Reporte De Tokens\n"
    "-Reporte De errores")
    os.system("C:/Users/Erwin14k/Documents/Image_Maker_Automaton/Reportes/TOKENS.html")
    os.system("C:/Users/Erwin14k/Documents/Image_Maker_Automaton/Reportes/ERRORS.html")
reports_Button.config(command=reports_view)
#============================================================================================================




#============================================================================================================
#Función para visualizar la imagen de manera original.
def original_view():
    global current_image,original_Button,img,image_label,image_frame
    print(current_image)
    img.config(file="jpg/"+current_image+"ORIGINAL.png")
    image_label.config(image=img)
    image_frame.grid_propagate(TRUE)
original_Button.config(command=original_view)
#============================================================================================================




#============================================================================================================
#Función para visualizar la imagen de manera MIRRORY.
def mirrory_view():
    global current_image,mirrory_Button,img,image_label,image_frame
    temp_filt=""
    temp_filt=image_dao_handler.filters_by_name(current_image)
    if temp_filt.count("MIRRORY") >=1:
        print(current_image)
        img.config(file="jpg/"+current_image+"MIRRORY.png")
        image_label.config(image=img)
        image_frame.grid_propagate(TRUE)
    else:
        messagebox.showerror(title="Image Maker V1.0", message="Filtro no disponible para esta imagen!!")
mirrory_Button.config(command=mirrory_view)
#============================================================================================================





#============================================================================================================
#Función para visualizar la imagen de manera MIRRORX.
def mirrorx_view():
    global current_image,mirrorx_Button,img,image_label,image_frame
    temp_filt=""
    temp_filt=image_dao_handler.filters_by_name(current_image)
    if temp_filt.count("MIRRORX") >=1:
        print(current_image)
        img.config(file="jpg/"+current_image+"MIRRORX.png")
        image_label.config(image=img)
        image_frame.grid_propagate(TRUE)
    else:
        messagebox.showerror(title="Image Maker V1.0", message="Filtro no disponible para esta imagen!!")
mirrorx_Button.config(command=mirrorx_view)
#============================================================================================================





#============================================================================================================
#Función para visualizar la imagen de manera MIRRORX.
def double_view():
    global current_image,double_mirror_Button,img,image_label,image_frame
    temp_filt=""
    temp_filt=image_dao_handler.filters_by_name(current_image)
    if temp_filt.count("DOUBLEMIRROR") >=1:
        print(current_image)
        img.config(file="jpg/"+current_image+"DOUBLE.png")
        image_label.config(image=img)
        image_frame.grid_propagate(TRUE)
    else:
        messagebox.showerror(title="Image Maker V1.0", message="Filtro no disponible para esta imagen!!")
double_mirror_Button.config(command=double_view)
#============================================================================================================





#============================================================================================================
#La útlima instrucción de la raíz, ejecutará todo lo que esté arriba de este método
root.mainloop()
#============================================================================================================

