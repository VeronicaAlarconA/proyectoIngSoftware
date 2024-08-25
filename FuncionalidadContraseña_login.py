import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Lista de usuarios predefinidos para el sistema 
usuarios = [
    {"nombre": "Juan Pérez", "tipo_documento": "cedula de ciudadanía", "documento": "123456789", "contraseña": "password123"},
    {"nombre": "Maria García", "tipo_documento": "cedula de extranjería", "documento": "987654321", "contraseña": "passw0rd"},
    {"nombre": "Carlos Rodríguez", "tipo_documento": "tarjeta de identidad", "documento": "456789123", "contraseña": "123456"},
    {"nombre": "Ana López", "tipo_documento": "cedula de ciudadanía", "documento": "321654987", "contraseña": "abc123"},
    {"nombre": "Sofia Martínez", "tipo_documento": "cedula de extranjería", "documento": "654321789", "contraseña": "qwerty"}
]

# Estado de sesión sin hacer login, se inicializa en falso
usuario_logueado = {"estado": False, "nombre": ""}

#datos ingresados por el usuario
def verificar_usuario():
    tipo_doc = tipo_documento_var.get()
    documento = entry_documento.get()
    contraseña = entry_contraseña.get()
    # Esta funcion valida inicialmente si el tipo de documento y el documento ingresados por el usuarios sean lo mismo, 
    # si no es asi muestra un mensaje de error.
    # Si es correcto verifica que la contraseña ingresada sea la correcta e igualmente lo valida con un mensaje

    for usuario in usuarios:
        if usuario["tipo_documento"] == tipo_doc and usuario["documento"] == documento:
            if usuario["contraseña"] == contraseña:
                usuario_logueado["estado"] = True
                usuario_logueado["nombre"] = usuario["nombre"]
                messagebox.showinfo("Acceso concedido", f"Bienvenido {usuario['nombre']}!")
                return
            else:
                messagebox.showerror("Error", "Contraseña incorrecta.")
                return

    messagebox.showerror("Error", "Usuario no encontrado.")

#cget obtiene el valor actual de show, la primera linea del if cambia la configuracion de los caracteres del campo a asteriscos
#toggle_button... es para cambiar el texto del boton
def toggle_password():
    if entry_contraseña.cget('show') == '':
        # Si show está con caracteres * es porque la contraseña está oculta
        entry_contraseña.config(show='*')
        toggle_button.config(text="Mostrar")
    else:
        entry_contraseña.config(show='')
        # Si show está vacío es porque la contraseña es visible
        toggle_button.config(text="Ocultar")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Login de Usuario")

# Configurar la ventana para pantalla completa
ventana.attributes('-fullscreen', True)
ventana.configure(bg='gray')  # Cambiar el fondo a gris

# Crear el marco principal
frame_principal = tk.Frame(ventana, bg='gray')
frame_principal.pack(expand=True, fill=tk.BOTH)

# Crear el marco izquierdo para la imagen (reducido de tamaño y movido a la derecha)
frame_imagen = tk.Frame(frame_principal, bg='gray', width=ventana.winfo_screenwidth()//5)
frame_imagen.pack(side=tk.LEFT, padx=40, pady=20, fill=tk.BOTH, expand=False)

# Crear un canvas para mostrar una imagen (puedes cargar una imagen aquí)
canvas = tk.Canvas(frame_imagen, bg='white')
canvas.pack(expand=True, padx=20, pady=20)

# Crear el marco derecho para los campos de entrada (aumentado de tamaño)
frame_derecho = tk.Frame(frame_principal, bg='gray')
frame_derecho.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Centrar los campos en el marco derecho
frame_campos = tk.Frame(frame_derecho, bg='gray')
frame_campos.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Tipo de documento (tamaño de texto aumentado y alineado a la izquierda)
label_tipo_documento = tk.Label(frame_campos, text="Tipo de Documento:", bg='gray', font=('Arial', 14), anchor='w')
label_tipo_documento.grid(row=0, column=0, pady=10, sticky='w')

tipo_documento_var = tk.StringVar()
tipo_documento_var.set("cedula de ciudadanía")  # Valor por defecto
opcion_tipo_documento = tk.OptionMenu(frame_campos, tipo_documento_var, "cedula de ciudadanía", "cedula de extranjería", "tarjeta de identidad")
opcion_tipo_documento.config(font=('Arial', 12))
opcion_tipo_documento.grid(row=1, column=0, pady=10, sticky='w')

# Número de documento (tamaño de texto aumentado y alineado a la izquierda)
label_documento = tk.Label(frame_campos, text="Número de Documento:", bg='gray', font=('Arial', 14), anchor='w')
label_documento.grid(row=2, column=0, pady=10, sticky='w')

entry_documento = tk.Entry(frame_campos, font=('Arial', 12))
entry_documento.grid(row=3, column=0, pady=10, sticky='w')

# Contraseña (tamaño de texto aumentado y alineado a la izquierda)
label_contraseña = tk.Label(frame_campos, text="Contraseña:", bg='gray', font=('Arial', 14), anchor='w')
label_contraseña.grid(row=4, column=0, pady=10, sticky='w')

entry_contraseña = tk.Entry(frame_campos, show='*', font=('Arial', 12))
entry_contraseña.grid(row=5, column=0, pady=10, sticky='w')

# Botón para mostrar/ocultar la contraseña (tamaño de botón ajustado y alineado a la izquierda)
toggle_button = tk.Button(frame_campos, text="Mostrar", command=toggle_password, bg='black', fg='white', font=('Arial', 12))  # Botón negro
toggle_button.grid(row=6, column=0, pady=10, sticky='w')

# Botón de login (tamaño de botón ajustado y alineado a la izquierda)
login_button = tk.Button(frame_campos, text="Login", command=verificar_usuario, bg='black', fg='white', font=('Arial', 12))  # Botón negro
login_button.grid(row=7, column=0, pady=10, sticky='w')

# Ejecutar la ventana
ventana.mainloop()
