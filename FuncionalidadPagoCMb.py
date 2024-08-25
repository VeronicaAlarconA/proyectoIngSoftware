#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      USUARIO
#
# Created:     24/08/2024
# Copyright:   (c) USUARIO 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
root = tk.Tk()
root.title("Cuota Moderadora")
root.geometry("900x600")

# Crear y colocar el mensaje en la ventana principal
mensaje = tk.Label(root, text="El valor de su cuota moderadora es: xxxxxxxx", padx=10, pady=10, font=("Helvetica", 16))
mensaje.pack(expand=True)

# Variable para almacenar la ventana secundaria actual
ventana_actual = None

# Función para mostrar el mensaje de pago exitoso en una ventana que se asemeja a las otras ventanas
def mostrar_pago_exitoso():
    global ventana_actual
    if ventana_actual is not None:
        ventana_actual.destroy()

    ventana_exito = tk.Toplevel()
    ventana_exito.title("Éxito")
    ventana_exito.geometry("900x600")

    frame_contenido = tk.Frame(ventana_exito)
    frame_contenido.pack(expand=True)

    mensaje_exito = tk.Label(frame_contenido, text="Su pago ha sido exitoso", font=("Helvetica", 16))
    mensaje_exito.pack(pady=20)

    boton_aceptar = tk.Button(frame_contenido, text="Aceptar", bg="black", fg="white", width=20, height=2, command=cerrar_todas_las_ventanas)
    boton_aceptar.pack(pady=20)

# Función para cerrar la ventana principal y cualquier ventana secundaria
def cerrar_todas_las_ventanas():
    global ventana_actual
    if ventana_actual is not None:
        ventana_actual.destroy()
    root.destroy()

# Función para abrir la ventana de efectivo
def abrir_ventana_efectivo():
    global ventana_actual
    if ventana_actual is not None:
        ventana_actual.destroy()
    ventana_actual = tk.Toplevel()
    ventana_actual.title("Efectivo")
    ventana_actual.geometry("900x600")

    frame_contenido = tk.Frame(ventana_actual)
    frame_contenido.pack(expand=True)

    mensaje = tk.Label(frame_contenido, text="Por favor ingrese su dinero", font=("Helvetica", 16))
    mensaje.pack(pady=20)

    # Crear un marco para los botones
    frame_botones = tk.Frame(frame_contenido)
    frame_botones.pack(side=tk.BOTTOM, anchor=tk.SE, padx=10, pady=10)

    boton_continuar = tk.Button(frame_botones, text="Continuar", bg="black", fg="white", width=20, command=mostrar_pago_exitoso)
    boton_continuar.pack(side=tk.LEFT, padx=10)

    boton_cancelar = tk.Button(frame_botones, text="Cancelar", bg="black", fg="white", width=20, command=abrir_ventana_pago)
    boton_cancelar.pack(side=tk.RIGHT, padx=10)

# Función para abrir la ventana de tarjeta de crédito
def abrir_ventana_tarjeta_credito():
    global ventana_actual
    if ventana_actual is not None:
        ventana_actual.destroy()
    ventana_actual = tk.Toplevel()
    ventana_actual.title("Tarjeta de Crédito")
    ventana_actual.geometry("900x600")

    frame_contenido = tk.Frame(ventana_actual)
    frame_contenido.pack(expand=True)

    mensaje = tk.Label(frame_contenido, text="Por favor ingrese su tarjeta", font=("Helvetica", 16))
    mensaje.pack(pady=20)

    # Crear un marco para los botones
    frame_botones = tk.Frame(frame_contenido)
    frame_botones.pack(side=tk.BOTTOM, anchor=tk.SE, padx=10, pady=10)

    boton_continuar = tk.Button(frame_botones, text="Continuar", bg="black", fg="white", width=20, command=mostrar_pago_exitoso)
    boton_continuar.pack(side=tk.LEFT, padx=10)

    boton_cancelar = tk.Button(frame_botones, text="Cancelar", bg="black", fg="white", width=20, command=abrir_ventana_pago)
    boton_cancelar.pack(side=tk.RIGHT, padx=10)

# Función para validar la entrada del código
def validar_codigo(P):
    if P.isdigit() and len(P) <= 6:
        return True
    return False

# Función para abrir la ventana de pago digital
def abrir_ventana_pago_digital():
    global ventana_actual
    if ventana_actual is not None:
        ventana_actual.destroy()
    ventana_actual = tk.Toplevel()
    ventana_actual.title("Pago Digital")
    ventana_actual.geometry("900x600")

    frame_contenido = tk.Frame(ventana_actual)
    frame_contenido.pack(expand=True)

    mensaje_opcion = tk.Label(frame_contenido, text="Seleccione un método de pago", font=("Helvetica", 16))
    mensaje_opcion.pack(pady=10)

    # Crear una barra de selección (dropdown) con las opciones de pago
    opciones_pago = tk.StringVar(value="nequi")  # Valor predeterminado
    opciones = ["Nequi", "Daviplata", "Paypal"]
    menu_desplegable = tk.OptionMenu(frame_contenido, opciones_pago, *opciones)
    menu_desplegable.config(width=20, font=("Helvetica", 14))
    menu_desplegable.pack(pady=10)

    mensaje_codigo = tk.Label(frame_contenido, text="Ingrese el código (6 dígitos)", font=("Helvetica", 16))
    mensaje_codigo.pack(pady=10)

    # Validar la entrada para aceptar solo números y longitud de 6 dígitos
    validacion_codigo = (frame_contenido.register(validar_codigo), '%P')

    entrada_codigo = tk.Entry(frame_contenido, width=40, validate='key', validatecommand=validacion_codigo)
    entrada_codigo.pack(pady=10)

    # Crear un marco para los botones
    frame_botones = tk.Frame(frame_contenido)
    frame_botones.pack(side=tk.BOTTOM, anchor=tk.SE, padx=10, pady=10)

    boton_continuar = tk.Button(frame_botones, text="Continuar", bg="black", fg="white", width=20, command=lambda: verificar_codigo(entrada_codigo.get()))
    boton_continuar.pack(side=tk.LEFT, padx=10)

    boton_cancelar = tk.Button(frame_botones, text="Cancelar", bg="black", fg="white", width=20, command=abrir_ventana_pago)
    boton_cancelar.pack(side=tk.RIGHT, padx=10)

def verificar_codigo(codigo):
    if len(codigo) == 6 and codigo.isdigit():
        mostrar_pago_exitoso()
    else:
        messagebox.showerror("Error", "El código debe tener exactamente 6 dígitos.")

# Función para abrir la ventana de selección de método de pago
def abrir_ventana_pago():
    global ventana_actual
    if ventana_actual is not None:
        ventana_actual.destroy()
    ventana_actual = tk.Toplevel()
    ventana_actual.title("Seleccionar Método de Pago")
    ventana_actual.geometry("900x600")

    frame_contenido = tk.Frame(ventana_actual)
    frame_contenido.pack(expand=True)

    mensaje_pago = tk.Label(frame_contenido, text="Seleccione método de pago", padx=10, pady=10, font=("Helvetica", 16))
    mensaje_pago.pack(pady=20)

    # Crear los botones de método de pago centrados
    boton_efectivo = tk.Button(frame_contenido, text="Efectivo", command=abrir_ventana_efectivo, bg="white", fg="black", width=20, height=2)
    boton_efectivo.pack(pady=5)

    boton_tarjeta = tk.Button(frame_contenido, text="Tarjeta de Crédito", command=abrir_ventana_tarjeta_credito, bg="white", fg="black", width=20, height=2)
    boton_tarjeta.pack(pady=5)

    boton_pago_digital = tk.Button(frame_contenido, text="Pago Digital", command=abrir_ventana_pago_digital, bg="white", fg="black", width=20, height=2)
    boton_pago_digital.pack(pady=5)

# Función que se ejecutará al hacer clic en el botón Realizar pago
def realizar_pago():
    abrir_ventana_pago()

# Crear el botón Realizar pago
boton = tk.Button(root, text="Realizar pago", command=realizar_pago, bg="black", fg="white", width=20)
boton.pack(side=tk.BOTTOM, anchor=tk.SE, padx=10, pady=10)

# Ejecutar el bucle principal de la interfaz
root.mainloop()
