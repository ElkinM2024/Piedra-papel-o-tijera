import tkinter as tk
from tkinter import messagebox
import random

class JuegoPiedraPapelTijera:
    def __init__(self):
        # Inicialización de puntuaciones
        self.puntaje_jugador = 0
        self.puntaje_computadora = 0

        # Crear la ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("Piedra, Papel o Tijera")
        self.ventana.geometry("700x600")
        self.ventana.config(bg="#1E1E1E")  # Fondo oscuro

        # Título
        self.titulo = tk.Label(self.ventana, text="¡Piedra, Papel o Tijera!", font=("Arial", 26, "bold"), fg="#F5F5F5", bg="#1E1E1E")
        self.titulo.pack(pady=30)

        # Etiquetas para mostrar los resultados
        self.resultado_label = tk.Label(self.ventana, text="Selecciona una opción", font=("Arial", 18), fg="#F5F5F5", bg="#1E1E1E")
        self.resultado_label.pack(pady=10)

        self.seleccion_computadora_label = tk.Label(self.ventana, text="Computadora elige...", font=("Arial", 16), fg="#F5F5F5", bg="#1E1E1E")
        self.seleccion_computadora_label.pack(pady=10)

        self.puntaje_label = tk.Label(self.ventana, text=f"Puntaje - Jugador: {self.puntaje_jugador}  Computadora: {self.puntaje_computadora}", font=("Arial", 16), fg="#F5F5F5", bg="#1E1E1E")
        self.puntaje_label.pack(pady=20)

        # Frame para los botones
        self.boton_frame = tk.Frame(self.ventana, bg="#1E1E1E")
        self.boton_frame.pack(pady=40)

        # Botones con estilo para seleccionar Piedra, Papel o Tijera
        self.boton_piedra = self.crear_boton("Piedra", "#FF6347", lambda: self.jugar("Piedra"))
        self.boton_piedra.grid(row=0, column=0, padx=30)

        self.boton_papel = self.crear_boton("Papel", "#1E90FF", lambda: self.jugar("Papel"))
        self.boton_papel.grid(row=0, column=1, padx=30)

        self.boton_tijera = self.crear_boton("Tijera", "#32CD32", lambda: self.jugar("Tijera"))
        self.boton_tijera.grid(row=0, column=2, padx=30)

        # Añadir imagen a las opciones
        self.img_piedra = tk.PhotoImage(file="piedra.png")  # Asegúrate de tener esta imagen
        self.img_papel = tk.PhotoImage(file="papel.png")    # Asegúrate de tener esta imagen
        self.img_tijera = tk.PhotoImage(file="tijera.png")  # Asegúrate de tener esta imagen

        # Etiqueta para mostrar la imagen seleccionada por la computadora
        self.imagen_computadora_label = tk.Label(self.ventana, image=self.img_piedra, bg="#1E1E1E")
        self.imagen_computadora_label.pack(pady=10)

        # Fondo adicional para un toque más visual
        self.fondo_frame = tk.Frame(self.ventana, bg="#1E1E1E")
        self.fondo_frame.pack(fill="both", expand=True)

    def crear_boton(self, texto, color, comando):
        """Crea un botón estilizado con efecto hover y bordes redondeados"""
        boton = tk.Button(self.boton_frame, text=texto, command=comando, width=12, height=3, font=("Arial", 14, "bold"), bg=color, fg="#fff", relief="flat", bd=0, highlightthickness=0)
        boton.config(activebackground="#ffcc00", activeforeground="black", fg="#fff")
        boton.bind("<Enter>", lambda e: boton.config(bg="#ffcc00", fg="black", relief="solid", bd=2))  # Cambio de color al pasar el ratón
        boton.bind("<Leave>", lambda e: boton.config(bg=color, fg="#fff", relief="flat", bd=0))  # Restaurar color al quitar el ratón
        boton.config(borderwidth=2, relief="raised", padx=10, pady=10)
        return boton

    def obtener_eleccion_computadora(self):
        """Devuelve una elección aleatoria de la computadora"""
        opciones = ["Piedra", "Papel", "Tijera"]
        return random.choice(opciones)

    def obtener_resultado(self, eleccion_jugador, eleccion_computadora):
        """Determina el resultado del juego"""
        if eleccion_jugador == eleccion_computadora:
            return "Empate"
        elif (eleccion_jugador == "Piedra" and eleccion_computadora == "Tijera") or \
             (eleccion_jugador == "Tijera" and eleccion_computadora == "Papel") or \
             (eleccion_jugador == "Papel" and eleccion_computadora == "Piedra"):
            return "Ganaste"
        else:
            return "Perdiste"

    def actualizar_puntuaciones(self, resultado):
        """Actualiza las puntuaciones del jugador y la computadora"""
        if resultado == "Ganaste":
            self.puntaje_jugador += 1
        elif resultado == "Perdiste":
            self.puntaje_computadora += 1
        # Actualizar la etiqueta de puntajes
        self.puntaje_label.config(text=f"Puntaje - Jugador: {self.puntaje_jugador}  Computadora: {self.puntaje_computadora}")

    def actualizar_imagen_computadora(self, eleccion_computadora):
        """Actualiza la imagen que muestra la elección de la computadora"""
        if eleccion_computadora == "Piedra":
            self.imagen_computadora_label.config(image=self.img_piedra)
        elif eleccion_computadora == "Papel":
            self.imagen_computadora_label.config(image=self.img_papel)
        elif eleccion_computadora == "Tijera":
            self.imagen_computadora_label.config(image=self.img_tijera)

    def jugar(self, eleccion_jugador):
        """Función que maneja la lógica del juego"""
        # Elección de la computadora
        eleccion_computadora = self.obtener_eleccion_computadora()

        # Obtener el resultado
        resultado = self.obtener_resultado(eleccion_jugador, eleccion_computadora)

        # Actualizar puntuaciones
        self.actualizar_puntuaciones(resultado)

        # Mostrar los resultados en la interfaz
        self.resultado_label.config(text=f"Resultado: {resultado}")
        self.seleccion_computadora_label.config(text=f"Computadora eligió: {eleccion_computadora}")

        # Actualizar imagen de la computadora
        self.actualizar_imagen_computadora(eleccion_computadora)

    def iniciar(self):
        """Inicia la interfaz gráfica"""
        self.ventana.mainloop()

# Crear una instancia del juego y ejecutarlo
if __name__ == "__main__":
    juego = JuegoPiedraPapelTijera()
    juego.iniciar()
