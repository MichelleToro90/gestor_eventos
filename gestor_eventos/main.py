import tkinter as tk
from tkinter import ttk, messagebox
import winsound
import datetime

# ===== MODELO =====
class Evento:
    def __init__(self, fecha, hora, descripcion):
        self.fecha = fecha
        self.hora = hora
        self.descripcion = descripcion

    def to_tuple(self):
        return (self.fecha, self.hora, self.descripcion)


# ===== CONTROLADOR =====
class ControladorEventos:
    def __init__(self, vista):
        self.vista = vista
        self.eventos = []

    def agregar_evento(self, fecha, hora, descripcion):
        if not fecha or not hora or not descripcion:
            winsound.Beep(1000, 300)
            messagebox.showwarning("Error", "Todos los campos son obligatorios")
            return

        if not self.validar_hora(hora):
            winsound.Beep(1000, 300)
            messagebox.showerror("Error", "Hora inválida (HH:MM)")
            return

        evento = Evento(fecha, hora, descripcion)
        self.eventos.append(evento)
        self.vista.mostrar_evento(evento)

    def eliminar_evento(self, items):
        for item in items:
            self.vista.eliminar_evento(item)

    def validar_hora(self, hora):
        try:
            h, m = map(int, hora.split(":"))
            return 0 <= h < 24 and 0 <= m < 60
        except:
            return False


# ===== VISTA =====
class Interfaz:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Eventos con Alarma")
        self.root.geometry("650x450")

        self.controlador = ControladorEventos(self)

        # ===== LISTA =====
        frame_lista = tk.Frame(root)
        frame_lista.pack(pady=10)

        self.tree = ttk.Treeview(
            frame_lista,
            columns=("Fecha", "Hora", "Descripción"),
            show="headings"
        )

        for col in ("Fecha", "Hora", "Descripción"):
            self.tree.heading(col, text=col)

        self.tree.pack()

        # ===== INPUT =====
        frame_input = tk.Frame(root)
        frame_input.pack(pady=10)

        tk.Label(frame_input, text="Fecha (YYYY-MM-DD):").grid(row=0, column=0)
        self.fecha = tk.Entry(frame_input)
        self.fecha.grid(row=0, column=1)

        tk.Label(frame_input, text="Hora (HH:MM):").grid(row=1, column=0)
        self.hora = tk.Entry(frame_input)
        self.hora.grid(row=1, column=1)

        tk.Label(frame_input, text="Descripción:").grid(row=2, column=0)
        self.descripcion = tk.Entry(frame_input)
        self.descripcion.grid(row=2, column=1)

        # ===== BOTONES =====
        frame_btn = tk.Frame(root)
        frame_btn.pack(pady=10)

        tk.Button(frame_btn, text="Agregar Evento", command=self.agregar).grid(row=0, column=0, padx=5)
        tk.Button(frame_btn, text="Eliminar Evento", command=self.eliminar).grid(row=0, column=1, padx=5)
        tk.Button(frame_btn, text="Salir", command=root.quit).grid(row=0, column=2, padx=5)

        # Iniciar verificación de alarmas
        self.verificar_eventos()

    def agregar(self):
        self.controlador.agregar_evento(
            self.fecha.get(),
            self.hora.get(),
            self.descripcion.get()
        )

        self.hora.delete(0, tk.END)
        self.descripcion.delete(0, tk.END)

    def eliminar(self):
        seleccion = self.tree.selection()

        if not seleccion:
            winsound.Beep(800, 300)
            messagebox.showwarning("Error", "Seleccione un evento")
            return

        if messagebox.askyesno("Confirmar", "¿Eliminar evento?"):
            self.controlador.eliminar_evento(seleccion)

    def mostrar_evento(self, evento):
        self.tree.insert("", "end", values=evento.to_tuple())

    def eliminar_evento(self, item):
        self.tree.delete(item)

    # ===== 🔔 ALARMA AUTOMÁTICA =====
    def verificar_eventos(self):
        ahora = datetime.datetime.now()
        fecha_actual = ahora.strftime("%Y-%m-%d")
        hora_actual = ahora.strftime("%H:%M")

        for evento in self.controlador.eventos:
            if evento.fecha == fecha_actual and evento.hora == hora_actual:
                winsound.Beep(1500, 500)
                messagebox.showinfo("Recordatorio", f"Evento: {evento.descripcion}")

        # Revisar cada segundo
        self.root.after(1000, self.verificar_eventos)


# ===== MAIN =====
if __name__ == "__main__":
    root = tk.Tk()
    app = Interfaz(root)
    root.mainloop()