import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import threading
import datetime
import shutil
import csv
import os

# CODIGO LOGICO EMPIEZA AQUI

class busqueda_init:

    def __init__(self):
        self.opcion = None
        self.texto_actualizado = ""
        self.comprobar = True
        self.text_widget2 = None
        self.nombre = None
        self.logs = ""
        self.c1 = 0
        self.c2 = 0
        self.total_filas = 0
        self.window_4 = None
        self.estado3 = False
        self.detener_proceso = False

    def abrir_archivo(self):
        nombre_csv.config(state="normal")
        self.ruta_archivo = filedialog.askopenfilename(
            filetypes=[("Archivos CSV", "*.csv")])
        if self.ruta_archivo:
            # Obtener solo el nombre del archivo con extensión
            nombre_archivo = self.ruta_archivo.split("/")[-1]
            # Borrar cualquier texto existente en el Entry
            nombre_csv.delete(0, "end")
            # Insertar el nombre del archivo en el Entry
            nombre_csv.insert(0, nombre_archivo)
            nombre_csv.config(relief=tk.SOLID, bd=2, disabledforeground="forest green", highlightbackground="#00FF00", highlightthickness=1)
            nombre_csv.config(state="disabled")  # Deshabilitar el Entry
        

    def valor_extension(self):
        self.ingresado = extension_guardada.get()  # Obtener el valor del Entry
        extension_ingresada.config(relief=tk.SOLID, bd=2, disabledforeground="forest green", highlightbackground="#00FF00", highlightthickness=0)
        if extension_ingresada['state'] == 'normal':
            extension_ingresada.config(state='disabled')  # Deshabilitar el Entry
        else:
            extension_ingresada.config(state='normal')  # Habilitar el Entry

    def ruta_ubicacion_(self):
        ruta_ubicacion.config(state="normal")
        self.ruta_busqueda = filedialog.askdirectory()
        # Obtener solo el nombre del archivo con extensión
        nombre_carpeta = self.ruta_busqueda.split("/")[-1]
        # Borrar cualquier texto existente en el Entry
        ruta_ubicacion.delete(0, "end")
        # Insertar el nombre del archivo en el Entry
        ruta_ubicacion.insert(0, nombre_carpeta)
        ruta_ubicacion.config(relief=tk.SOLID, bd=2, disabledforeground="forest green", highlightbackground="#00FF00", highlightthickness=1)
        ruta_ubicacion.config(state="disabled")  # Deshabilitar el Entry
    
    def ruta_destino_(self):
        ruta_destino.config(state="normal")
        self.ruta_destino2 = filedialog.askdirectory()
        # Obtener solo el nombre del archivo con extensión
        nombre_carpeta2 = self.ruta_destino2.split("/")[-1]
        # Borrar cualquier texto existente en el Entry
        ruta_destino.delete(0, "end")
        # Insertar el nombre del archivo en el Entry
        ruta_destino.insert(0, nombre_carpeta2)
        ruta_destino.config(relief=tk.SOLID, bd=2, disabledforeground="forest green", highlightbackground="black", highlightthickness=0)
        ruta_destino.config(state="disabled")  # Deshabilitar el Entry
    
    def opcion_disponible (self, opcion):

        self.opcion = opcion
        if opcion  == "Cortar":
            color_opcion = Cortar_1.cget("background")
            if Cortar_1["state"] == "normal" and color_opcion != "forest green":
                Copiar_2.config(state='disabled',bg="SystemButtonFace")  # Deshabilitar el Entry
                Borrar_3.config(state='disabled', bg="SystemButtonFace")
                Cortar_1.config(bg="forest green")
            else:
                Copiar_2.config(state='normal')  # Habilitar el Entry
                Borrar_3.config(state='normal')  # Habilitar el Entry
                Cortar_1.config(bg="SystemButtonFace")
        if opcion  == "Copiar":
            color_opcion = Copiar_2.cget("background")
            if Copiar_2["state"] == "normal" and color_opcion != "forest green":
                Borrar_3.config(state='disabled', bg="SystemButtonFace")
                Cortar_1.config(state='disabled',bg="SystemButtonFace")  # Deshabilitar el Entry
                Copiar_2.config(bg="forest green")
            else:
                Borrar_3.config(state='normal')  # Habilitar el Entry
                Cortar_1.config(state='normal')  # Habilitar el Entry
                Copiar_2.config(bg="SystemButtonFace")
        if opcion == "Borrar":
            color_opcion = Borrar_3.cget("background")
            if Copiar_2["state"] == "normal" and color_opcion != "forest green":
                Copiar_2.config(state='disabled',bg="SystemButtonFace")  # Deshabilitar el Entry
                Cortar_1.config(state='disabled', bg="SystemButtonFace")
                Borrar_3.config(bg="forest green")

            else:
                Copiar_2.config(state='normal')  # Habilitar el Entry
                Cortar_1.config(state='normal')  # Habilitar el Entry
                Borrar_3.config(bg="SystemButtonFace")

# ----------------------------------------------------------------
# Aqui empieza la logica y funcionamiento principal del programa
    
    def ejecucion_principal(self):
            
            self.c1 = 0
            self.c2 = 0
            self.detener_proceso = False
            if boton_inicio["text"] == "Detener":
                boton_inicio.configure(text="Iniciar")
                self.detener_proceso = True
                self.estado3 = True
                return
            try:    
                self.ruta_archivo.replace("/","\\")
                boton_inicio.configure(text="Detener")
            except:
                nombre_csv.config(highlightbackground="red", highlightthickness=2)
                return
        
            if self.window_4 is not None and self.estado3:
                    self.window_4.destroy()
            self.window_4 = tk.Toplevel()
            self.window_4.title("Registro de exploración")
            self.window_4.configure(bg="forest green")
            self.window_4.resizable(width=False, height=False)

            # marco secundario "Registro de exploración"
            self.frame_margen4 = tk.Frame(self.window_4, bd=2, relief=tk.SUNKEN)
            self.frame_margen4.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

            self.frame_contador = tk.Frame(self.frame_margen4, bd=2, highlightbackground="forest green", relief="sunken", highlightthickness=3)
            self.frame_contador.grid(row=0, column=0, padx=(5, 0), pady=(10, 10))

            # Label de conteo, busqueda y encontrados
            self.localizando = tk.Label(self.frame_contador, text=f"Localizando {self.c2} de {0}")
            self.localizando.grid(row=0, column=0)
            self.encontrados_l = tk.Label(self.frame_contador, text=f"/Archivos Encontrados {self.c1}")
            self.encontrados_l.grid(row=0, column=1)
            self.frame_registros = tk.Frame(self.frame_margen4, bd=2, height=349, width=309, relief="ridge")
            self.frame_registros.grid(row=1, column=0, padx=(4, 0), pady=2)
            text_widget2 = tk.Text(self.frame_registros, height=22, width=38)
            text_widget2.pack(fill="both", expand=True)
            self.registro_encontrado = ttk.Scrollbar(self.frame_registros, orient="vertical", command=text_widget2.yview)
            text_widget2.configure(yscrollcommand=self.registro_encontrado.set)
            self.registro_encontrado.pack(side="right", fill="y")

            # tamaño de la ventana secundaria
            window_width_4 = 330
            window_height_4 = 420

            # obtener la posición y tamaño de la ventana principal
            root_x = window.winfo_x()
            root_y = window.winfo_y()
            root_width = window.winfo_width()
            root_height = window.winfo_height()

            # calcular la posición de la ventana "Registro de exploración" a la derecha de la ventana principal
            x = root_x + root_width + 5  # 10 es el espacio entre las ventanas
            y = root_y

            # ajustar la posición de la ventana secundaria si se sale de la pantalla
            screen_width = window.winfo_screenwidth()
            if x + window_width_4 > screen_width:
                x = screen_width - window_width_4

            # establecer la geometría de la ventana secundaria
            self.window_4.geometry(f"{window_width_4}x{window_height_4}+{x}+{y}")

            self.estado3 = True

            def independiente():
                boton_registros.config(state="disabled")
                progreso_actual = tk.DoubleVar(value=0.0)
                with open(self.ruta_archivo, "r") as csv1:
                        self.total_filas = sum(1 for _ in csv.reader(csv1))
                        barra_progreso = ttk.Progressbar(frame_colum4, length=170, mode='determinate', maximum=self.total_filas, variable=progreso_actual,)
                        barra_progreso.lower()
                        barra_progreso.grid(row=0, column=1)
                        etiqueta_porcentaje = tk.Label(frame_colum4, text="0%", width=5, height=1, relief="ridge")
                        etiqueta_porcentaje.grid(row=0, column=2, pady=(2,0))

                with open(self.ruta_archivo,"r") as csv1:
                    lector_fila = csv.reader(csv1)
                    for valor_d in lector_fila:
                        if self.detener_proceso:
                            break
                        try:
                            concatenado = valor_d[0]+"."+self.ingresado
                        except:
                            extension_ingresada.config(highlightbackground="red", highlightthickness=2)
                            break
                        try:
                         for ruta_origen, carpetas, archivos in os.walk(self.ruta_busqueda.replace("/","\\")):    
                            if concatenado in archivos:
                                register = "Archivos_encontrados.txt"
                                ruta_archivo_encontrado = os.path.join(ruta_origen, concatenado)
                                if self.opcion  == "Cortar":
                                    shutil.move(ruta_archivo_encontrado, self.ruta_destino2.replace("/","\\")) 
                                    self.c1 += 1
                                    self.nombre = valor_d
                                elif self.opcion == "Copiar":
                                    shutil.copy2(ruta_archivo_encontrado, self.ruta_destino2.replace("/","\\"))
                                    self.c1 += 1
                                    self.nombre = valor_d
                                elif self.opcion == "Borrar":
                                    os.remove(ruta_archivo_encontrado)
                                    self.c1 += 1
                                    self.nombre = valor_d
                                resetlogs = ""
                                resetlogs += f"Nombre: {self.nombre}\nRuta: {ruta_archivo_encontrado}\n"
                                with open(register, "a") as logs1:
                                    logs1.write(resetlogs)
                                ruta_script = os.path.dirname(os.path.abspath(__file__))
                                ruta_archivos_encontrados = os.path.join(ruta_script, "..", "Archivos_encontrados.txt")
                                shutil.copy2(ruta_archivos_encontrados,self.ruta_destino2.replace("/", "\\"))
                        except:
                            value1 = ruta_ubicacion.get()
                            if not value1:
                                ruta_ubicacion.config(highlightbackground="red", highlightthickness=2)
                                break
                        if self.opcion == None:
                            Cortar_1.config(bg="#FFCCCC")
                            Copiar_2.config(bg="#FFCCCC")
                            Borrar_3.config(bg="#FFCCCC")
                            break
                        value2 = ruta_destino.get()
                        if not value2 and self.opcion != "Borrar":
                            ruta_destino.config(highlightbackground="red", highlightthickness=2)
                            break
                        
                        ruta_destino.config(relief=tk.SOLID, bd=2, disabledforeground="forest green", highlightbackground="#00FF00", highlightthickness=1)
                        progreso_actual.set(progreso_actual.get() + 1)
                        porcentaje = int((progreso_actual.get() / self.total_filas) * 100)
                        etiqueta_porcentaje.config(text=f"{porcentaje}%")
                        barra_progreso.update_idletasks()
                        self.c2 += 1
                        self.localizando.config(text=f"Localizando {self.c2} de {self.total_filas}")
                        self.encontrados_l.config(text=f"/Archivos Encontrados {self.c1}")
                        if self.nombre is not None:
                            text_widget2.insert("end", f"Nombre: {self.nombre}\nRuta:{ruta_archivo_encontrado}\n")
                            self.texto_actualizado = text_widget2.get("1.0", "end-1c")
                            self.nombre = None
                    progreso_actual.set(self.total_filas)
                    etiqueta_porcentaje.config(text="100%")
                    barra_progreso.grid_remove()
                    etiqueta_porcentaje.grid_remove()
                    boton_inicio.configure(text="Iniciar")
                boton_registros.config(state="normal")
            threading.Thread(target=independiente).start()

    def abrir_ventana_secundaria(self):
        if self.window_4 is not None and self.estado3:
            self.window_4.destroy()
            self.estado3 = False
        else:
            self.window_4 = tk.Toplevel()
            self.window_4.title("Registro de exploración")
            self.window_4.configure(bg="forest green")
            self.window_4.resizable(width=False, height=False)

            # marco secundario "Registro de exploración"
            self.frame_margen4 = tk.Frame(self.window_4, bd=2, relief=tk.SUNKEN)
            self.frame_margen4.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

            self.frame_contador = tk.Frame(self.frame_margen4, bd=2, highlightbackground="forest green", relief="sunken", highlightthickness=3)
            self.frame_contador.grid(row=0, column=0, padx=(5, 0), pady=(10, 10))

            # Label de conteo, busqueda y encontrados
            self.localizando = tk.Label(self.frame_contador, text=f"Localizando {self.c2} de {self.total_filas}")
            self.localizando.grid(row=0, column=0)
            self.encontrados_l = tk.Label(self.frame_contador, text=f"/Archivos Encontrados {self.c1}")
            self.encontrados_l.grid(row=0, column=1)
            self.frame_registros = tk.Frame(self.frame_margen4, bd=2, height=349, width=309, relief="ridge")
            self.frame_registros.grid(row=1, column=0, padx=(4, 0), pady=2)
            text_widget2 = tk.Text(self.frame_registros, height=22, width=38)
            text_widget2.pack(fill="both", expand=True)
            text_widget2.insert("1.0", self.texto_actualizado)
            self.registro_encontrado = ttk.Scrollbar(self.frame_registros, orient="vertical", command=text_widget2.yview)
            text_widget2.configure(yscrollcommand=self.registro_encontrado.set)
            self.registro_encontrado.pack(side="right", fill="y")

            # tamaño de la ventana secundaria
            window_width_4 = 330
            window_height_4 = 420

            # obtener la posición y tamaño de la ventana principal
            root_x = window.winfo_x()
            root_y = window.winfo_y()
            root_width = window.winfo_width()
            root_height = window.winfo_height()

            # calcular la posición de la ventana "Registro de exploración" a la derecha de la ventana principal
            x = root_x + root_width + 5  # 10 es el espacio entre las ventanas
            y = root_y

            # ajustar la posición de la ventana secundaria si se sale de la pantalla
            screen_width = window.winfo_screenwidth()
            if x + window_width_4 > screen_width:
                x = screen_width - window_width_4

            # establecer la geometría de la ventana secundaria
            self.window_4.geometry(f"{window_width_4}x{window_height_4}+{x}+{y}")

            self.estado3 = True



            
# CODIGO DE INTERFAZ EMPIEZA AQUI

# Funcion Center_Window: Ajusta la ventana principal en la posicion del centro de la pantalla de acuerdo a la resolucion
# que tenga el equipo a utilizar.

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")


def clear_placeholder(event):
    if extension_ingresada.get() == "Ejemplo: JPG":
        extension_ingresada.delete(0, tk.END)
        extension_ingresada.config(highlightthickness=0)


estado1 = False
window_2 = None
def intructivo_uso():
    global estado1, window_2
    # segunda ventana instructivo
    if window_2 is not None and estado1:
        window_2.destroy()
        estado1 = False
    else:
        window_2 = tk.Toplevel()
        window_2.title("Instructivo")
        window_2.configure(bg="forest green")
        window_2.resizable(width=False, height=False)

        # marco secundario instructivo
        frame_margen2 = tk.Frame(window_2, bd=2, relief=tk.SUNKEN)
        frame_margen2.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # tamaño de la ventana secundaria
        window_width_2 = 307
        window_height_2 = 420

        # obtener la posición y tamaño de la ventana principal
        root_x = window.winfo_x()
        root_y = window.winfo_y()
        root_width = window.winfo_width()
        root_height = window.winfo_height()

        # calcular la posición de la ventana secundaria al lado izquierdo de la ventana principal
        x = root_x - window_width_2 - 5  # 10 es el espacio entre las ventanas
        y = root_y

        # ajustar la posición de la ventana secundaria si se sale de la pantalla
        screen_width = window.winfo_screenwidth()
        if x < 0:
            x = 0

        # establecer la geometría de la ventana secundaria
        window_2.geometry(f"{window_width_2}x{window_height_2}+{x}+{y}")

        # SCROLL para ventana de instrucción
        text_widget = tk.Text(frame_margen2)
        text_widget.pack(fill="both", expand=True)

        scrollbar = ttk.Scrollbar(frame_margen2, orient="vertical", command=text_widget.yview)
        text_widget.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Texto para el label
        texto = """\
==============Abrir CSV=============

Selecciona un archivo CSV (delimitado por comas),que contenga en la primera columna los nombres de los archivos que deseas buscar, sin extension

=============Extensión==============
 
Escribe la extensión de archivo que deseas buscar y haz clic en el botón "Extensión" para guardarla. Después de hacerlo, la opción de escritura se deshabilitará. Si deseas cambiar la extensión, simplemente presiona nuevamente el botón.

=============Ubicacion==============

Selecciona la carpeta desde donde deseas comenzar la búsqueda. Ten en cuenta que el programa buscará en todas las subcarpetas de la ruta seleccionada.

=============Destino================ 

Elige la carpeta donde deseas guardar la información encontrada, ya sea copiándola o moviéndola. Si eliges la opción "Borrar", no necesitas seleccionar ninguna carpeta de destino, ya que no se aplicará.

===========Funciones================

Selecciona una de las tres opciones disponibles en el programa. Una vez que elijas una opción, las demás se deshabilitarán para evitar conflictos. Si deseas cambiar de opción, simplemente haz clic nuevamente en la opción.

===========Iniciar==================

Una vez que hayas completado los pasos anteriores, haz clic en "Iniciar" para comenzar la búsqueda y ejecutar la función correspondiente. Se mostrará una barra de progreso que se llenará a medida que el programa avance. Al finalizar la barra de progreso y búsqueda, se mostrará la cantidad de datos buscados y encontrados.

===========Acerca De================

En esta sección encontrarás información sobre la versión del programa, el fundador, el propósito y cómo ponerte en contacto.

===========Ver Historial============

Desde aquí podrás visualizar las rutas de los archivos encontrados y las rutas donde se realizó la búsqueda. Esto incluye tanto el registro histórico como la información en tiempo real si el programa está en ejecución

=========FIN DE INSTRUCTIVO=========

Espero que esta guía te sea útil. ¡Buena suerte con tu búsqueda de archivos y funciones correspondientes!
"""
# Crear label dentro del frame
        text_widget.insert("end", texto)
        estado1 = True

estado2 = False
window_3 = None
def acerca_de():
    global estado2, window_3
    # segunda ventana "Acerca de"
    if window_3 is not None and estado2:
        window_3.destroy()
        estado2 = False
    else:
        window_3 = tk.Toplevel()
        window_3.title("Acerca de")
        window_3.configure(bg="forest green")
        window_3.resizable(width=False, height=False)

        # marco secundario "Acerca de"
        frame_margen3 = tk.Frame(window_3, bd=2, relief=tk.SUNKEN)
        frame_margen3.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # tamaño de la ventana secundaria
        window_width_3 = 307
        window_height_3 = 420

        # obtener la posición y tamaño de la ventana principal
        root_x = window.winfo_x()
        root_y = window.winfo_y()
        root_width = window.winfo_width()
        root_height = window.winfo_height()

        # calcular la posición de la ventana "Acerca de" al lado izquierdo de la ventana principal
        x = root_x - window_width_3 - 5  # 10 es el espacio entre las ventanas
        y = root_y

        # ajustar la posición de la ventana secundaria si se sale de la pantalla
        if x < 0:
            x = 0

        # establecer la geometría de la ventana secundaria
        window_3.geometry(f"{window_width_3}x{window_height_3}+{x}+{y}")

        # SCROLL para ventana de "Acerca de"
        text_widget1 = tk.Text(frame_margen3)
        text_widget1.pack(fill="both", expand=True)

        scrollbar1 = ttk.Scrollbar(frame_margen3, orient="vertical", command=text_widget1.yview)
        text_widget1.configure(yscrollcommand=scrollbar1.set)
        scrollbar1.pack(side="right", fill="y")

        # Texto para el label
        texto = """\
========Informacion_Itera_Copy======

Nombre: Itera_Copy
Versión: 1.0
Fecha de lanzamiento:
Desarrollador: Simon Falla

============Descripcion=============

Itera_Copy es una aplicación de escritorio diseñada para simplificar y automatizar tareas repetitivas y búsquedas innecesarias por parte del usuario. Permite proporcionar una base de datos con nombres de archivos y una extensión específica para realizar búsquedas extendidas desde una ruta determinada. La aplicación ofrece diversas opciones, como especificar una ruta de destino para copiar o mover el archivo encontrado, o incluso eliminarlo. También cuenta con funcionalidades para verificar registros y validar instrucciones para un mejor entendimiento.

============Proposito===============

El propósito de Itera_Copy es facilitar la búsqueda masiva de archivos y automatizar procesos y tareas repetitivas para los usuarios.

=========Requisitos Minimos=========

Sistema operativo: Windows 10
Espacio en disco: 5GB
Memoria RAM: Mínimo 2 GB
Procesador: 1 GHz en adelante
Dependencias: Python 3.11.4,Tkinter

============Contactanos=============

Correo: sdfalla_co@gmail.com
GitHub: https://github.com/sdfalla99
"""
        text_widget1.insert("end", texto)
        estado2 = True


# Configuraciones ventana principal: Carga el titulo, Carga el icono, Carga el color de fondo para el margen, y por ultimo
# deshabilita el tamaño de ajuste de la ventana para el usuario, se deja de un tamaño fijo.
script_dir = os.path.dirname(os.path.abspath(__file__))
window = tk.Tk()
window.title("Itera_Copy")
window.iconphoto(True, tk.PhotoImage(file=f"{script_dir}/icon/escarabajo.png"))
window.configure(bg="#008000")
window.resizable(width=False, height=False)

# tamaño de la ventana principal
window_width = 310
window_height = 422
window.geometry(f"{window_width}x{window_height}")

# Centrar la ventana principal en la pantalla, se llama a la funcion  y se entrega el tamaño y las proporciones
center_window(window, window_width, window_height)

# Marco Principal, este marco es el que permite visualizar el borde del aplicativo en verde ya que cubre la ventana principal
# y dentro de este se agrega todo el codigo correspondiente, por lo cual vendria siendo la ventana_padre

frame_margen = tk.Frame(window, relief=tk.SOLID, bd=1)
frame_margen.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

#==========================================================================================
# Marco Superior 1
#==========================================================================================
# Se genera la margen Leyenda Label para que tenga un titulo de entrada, se centra el texto
# se verifica que el  tamaño de la ventana no se afecte por los elementos a agregar con sticky="nsew"

frame_colum1 = tk.LabelFrame(frame_margen, width=300, height=100, text="CSV - EXTENSION")
frame_colum1.configure(labelanchor="n")
frame_colum1.grid(row=0, column=0, padx=(10, 0), sticky="nsew")

# Botones Superior 1
# se genera el Boton Abrir CSV, permitira abrir el documento con el listado de archivos, y se almacenara
# el nombre del archivo en la variable de ENTRY asignada

# Se genera el Boton Extension, este solicitara como entrada la extension, cualquiera extension es valida
# la cual buscara el archivo con ese formato.

abrir_1 = busqueda_init()
abrir_csv = tk.Button(frame_colum1, text="Abrir CSV", width=10,height=1, command=abrir_1.abrir_archivo)
abrir_csv.grid(row=0, column=0, padx=10, pady=10)

Extension = tk.Button(frame_colum1, text="Extension", width=10,height=1, command=abrir_1.valor_extension)
Extension.grid(row=1, column=0,padx=10, pady=10)

nombre_csv = tk.Entry(frame_colum1, selectbackground="forest green", foreground="forest green", justify="center", state="disabled")
nombre_csv.grid(row=0, column=1)

extension_guardada = tk.StringVar()
extension_ingresada = tk.Entry(frame_colum1, selectbackground="forest green", foreground="forest green", textvariable=extension_guardada, justify="center",highlightbackground=None)

extension_ingresada.bind('<FocusIn>', clear_placeholder)
extension_ingresada.insert(0, "Ejemplo: JPG")
extension_ingresada.grid(row=1, column=1)

#===========================================================================================
# Marco Superior 2
#==========================================================================================

frame_colum2 = tk.LabelFrame(frame_margen, width=300, height=100, text="CARPETAS")
frame_colum2.configure(labelanchor="n")
frame_colum2.grid(row=1, column=0, padx=(10,0) ,sticky="nsew")

# Botones Superior 2
ubicacion_carpeta = tk.Button(frame_colum2, text="Ubicacion", width=10, height=1, command=abrir_1.ruta_ubicacion_)
ubicacion_carpeta.grid(row=0, column=0, padx=10, pady=10)

destino_carpeta = tk.Button(frame_colum2, text="Destino", width=10, height=1,command =abrir_1.ruta_destino_)
destino_carpeta.grid(row=1, column=0, padx=10, pady=10)

ruta_ubicacion = tk.Entry(frame_colum2, text=None, selectbackground="forest green", state="disabled", justify="center")
ruta_ubicacion.grid(row=0, column=1)
ruta_destino = tk.Entry(frame_colum2, text=None, selectbackground="forest green",state="disabled", justify="center")
ruta_destino.grid(row=1, column=1)

#==========================================================================================
# Marco Inferior 1
#==========================================================================================

frame_colum3 = tk.LabelFrame(frame_margen, width=300,height=100, text="FUNCIONES")
frame_colum3.configure(labelanchor="n")
frame_colum3.grid(row=2, column=0, padx=(10, 0), sticky="nsew")

# Botones Inferior 1
Cortar_1 = tk.Button(frame_colum3, text="Cortar", width=10, height=1, command=lambda: abrir_1.opcion_disponible("Cortar"))
Cortar_1.grid(row=1, column=0, padx=(0,15), pady=(20))
Copiar_2 = tk.Button(frame_colum3, text="Copiar", width=10, height=1,command=lambda: abrir_1.opcion_disponible("Copiar"))
Copiar_2.grid(row=1, column=1, padx=(0,15))
Borrar_3 = tk.Button(frame_colum3, text="Borrar", width=10, height=1, command=lambda: abrir_1.opcion_disponible("Borrar"))
Borrar_3.grid(row=1, column=2, padx=(0,2))

#==========================================================================================
# Marco Inferior 2
#==========================================================================================

frame_colum4 = tk.Frame(frame_margen, background="#999f9b", bd=2, relief="sunken",height=68)
frame_colum4.grid(row=3, column=0, padx=(10, 0), pady=(8,9), sticky="nesw")

# Botones Inferior 3

frame_separador1 = tk.Frame(frame_colum4, background="forest green")
frame_separador1.grid(row=0,column=0, padx=0, pady=0)

boton_inicio = tk.Button(frame_separador1, text="Iniciar",width=8, height=1, relief="ridge", command=abrir_1.ejecucion_principal)
boton_inicio.lift()
boton_inicio.grid(row=0, column=0, padx=0, pady=0)

#==========================================================================================
# Marco Inferior 3
#==========================================================================================
frame_colum5 = tk.Frame(frame_margen, bd=2, relief="sunken",height=68)
frame_colum5.grid(row=4, column=0, padx=(10, 0), pady=0, sticky="nesw")

# Botones Inferior 3
frame_separador2 = tk.Frame(frame_colum5)
frame_separador2.grid(row=0,column=0)

boton_instrupcion = tk.Button(frame_separador2, text="Instrupciones",width=10, height=1, relief="ridge", command=intructivo_uso)
boton_instrupcion.grid(row=0, column=0, padx=(8, 8), pady=(5, 5))

boton_info = tk.Button(frame_separador2, text="Acerca de",width=10, height=1, relief="ridge", command=acerca_de)
boton_info.grid(row=0, column=1, padx=(0, 0), pady=(5, 5))

boton_registros = tk.Button(frame_separador2, text="Ver historial",width=10, height=1, relief="ridge", command=abrir_1.abrir_ventana_secundaria)
boton_registros.grid(row=0, column=2, padx=(8, 0), pady=(5, 5))

#==========================================================================================

# Mostrar la ventana principal
window.mainloop()
