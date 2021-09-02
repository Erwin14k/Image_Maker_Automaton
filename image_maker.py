from Token_DAO import Token_DAO
from os import system
from tkinter import *
from Lexical_Analyzer import Lexical_Analyzer
from tkinter.filedialog import askopenfilename
from Token import Token
from Lexical_Analyzer import token_handler,error_handler
lexical_analyzer_handler=Lexical_Analyzer()


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
exit_Button=Button(master_frame,text=" Salir",font=("Comic Sans MS",10),bg="black",fg="yellow")
exit_Button.grid(row=0,column=3,padx=10)
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
#============================================================================================================




#============================================================================================================
#Creación de un frame que servirá como division
division_frame=Frame(root,width="100",height="100",bg="gold")
#============================================================================================================




#============================================================================================================
#Creación del frame donde se muestra la imagen
image_frame=Frame(root,width="650",height="430",padx=50)
image_frame.config(bg="yellow")
image_frame.config(bd="20")
image_frame.config(relief="groove")
image_frame.config(cursor="hand2")
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
#Con este botón inicializamos esta función
principal_Button.config(command=master_mind_window)
#============================================================================================================    



#============================================================================================================
#Función que termina con la ejecución de la aplicación
def exit_application():
    exit()
exit_Button.config(command=exit_application)
#============================================================================================================




#============================================================================================================
#Función para cargar el archivo con extensión "pxla" a memoria.
route=""
original_text=""
def upload_file():
    global route,original_text
    route = askopenfilename()
    archive = open(route,"r")
    original_text=archive.read()
    archive.close()
    print(original_text)
    lexical_analyzer_handler.analyze2(original_text)
    print("\n\n\n\n\n\n\n")
    lexical_analyzer_handler.print_errors()
    print("\n\n\n\n\n\n\n")
    lexical_analyzer_handler.print_tokens()
    token_handler.tokens_html_report()
    error_handler.errors_html_report()
upload_Button.config(command=upload_file)
#============================================================================================================




#============================================================================================================
#La útlima instrucción de la raíz, ejecutará todo lo que esté arriba de este método
root.mainloop()
#============================================================================================================

