import tkinter as tk
import random

def center_window(window):
    """Centra una ventana en la pantalla."""
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

def visualizar_detalles_cita():
    # Ventana principal
    ventana_principal = tk.Tk()
    ventana_principal.title("Sistema de Citas")
    ventana_principal.geometry("400x300")
    ventana_principal.configure(bg="#f0f0f0")  # Fondo gris claro

    # Centrar la ventana principal
    center_window(ventana_principal)

    # Botón para visualizar detalles
    boton_visualizar = tk.Button(ventana_principal, text="Visualizar Detalles de su Cita",
                                bg="black", fg="white", font=("Arial", 12),
                                command=mostrar_detalles_cita)
    boton_visualizar.pack(pady=50)

    ventana_principal.mainloop()

def mostrar_detalles_cita():
    # Ventana de detalles
    ventana_detalles = tk.Toplevel()
    ventana_detalles.title("Detalles de la Cita")
    ventana_detalles.geometry("500x300")
    ventana_detalles.configure(bg="#f0f0f0")  # Fondo gris claro

    # Centrar la ventana de detalles
    center_window(ventana_detalles)

    # Título
    titulo = tk.Label(ventana_detalles, text="Los detalles de su cita son:",
                     font=("Arial", 16), pady=20)
    titulo.pack()

    # Recuadro con detalles
    frame_detalles = tk.Frame(ventana_detalles, bg="white", padx=20, pady=20)
    frame_detalles.pack(pady=20)

    # Detalles aleatorios (puedes reemplazar esto con datos de una base de datos)
    especialidades = ["Cardiología", "Pediatría", "Ginecología", "Oftalmología"]
    profesionales = ["Dr. Juan Pérez", "Dra. María López", "Dr. Carlos Gómez"]

    especialidad = random.choice(especialidades)
    piso = random.randint(1, 5)
    codigo = f"C{random.randint(100, 999)}"
    consultorio = random.randint(101, 300)
    profesional = random.choice(profesionales)

    # Mostrar los detalles en etiquetas
    label_especialidad = tk.Label(frame_detalles, text=f"Especialidad: {especialidad}")
    label_piso = tk.Label(frame_detalles, text=f"Piso: {piso}")
    label_codigo = tk.Label(frame_detalles, text=f"Código: {codigo}")
    label_consultorio = tk.Label(frame_detalles, text=f"Consultorio: {consultorio}")
    label_profesional = tk.Label(frame_detalles, text=f"Profesional: {profesional}")

    label_especialidad.pack()
    label_piso.pack()
    label_codigo.pack()
    label_consultorio.pack()
    label_profesional.pack()

    # Botón finalizar
    boton_finalizar = tk.Button(ventana_detalles, text="Finalizar",
                                bg="black", fg="white", font=("Arial", 12),
                                command=ventana_detalles.destroy)
    boton_finalizar.pack(pady=10)

if __name__ == "__main__":
    visualizar_detalles_cita()