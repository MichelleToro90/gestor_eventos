import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

class Interfaz:
    def __init__(self, root, controlador):
        self.root = root
        self.controlador = controlador

        self.root.title("Gestor de Eventos")

        # ===== FRAME LISTA =====
        frame_lista = tk.Frame(root)
        frame_lista.pack()

        self.tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
        for col in ("Fecha", "Hora", "Descripción"):
            self.tree.heading(col, text=col)

        self.tree.pack()

        # ===== FRAME ENTRADA =====
        frame_input = tk.Frame(root)
        frame_input.pack()

        tk.Label(frame_input, text="Fecha").grid(row=0, column=0)
        self.fecha = DateEntry(frame_input)
        self.fecha.grid(row=0, column=1)

        tk.Label(frame_input, text="Hora").grid(row=1, column=0)
        self.hora = tk.Entry(frame_input)
        self.hora.grid(row=1, column=1)

        tk.Label(frame_input, text="Descripción").grid(row=2, column=0)
        self.descripcion = tk.Entry(frame_input)
        self.descripcion.grid(row=2, column=1)

        # ===== BOTONES =====
        frame_btn = tk.Frame(root)
        frame_btn.pack()

        tk.Button(frame_btn, text="Agregar", command=self.agregar).grid(row=0, column=0)
        tk.Button(frame_btn, text="Eliminar", command=self.eliminar).grid(row=0, column=1)
        tk.Button(frame_btn, text="Salir", command=root.quit).grid(row=0, column=2)

    def agregar(self):
        self.controlador.agregar_evento(
            self.fecha.get(),
            self.hora.get(),
            self.descripcion.get()
        )

    def eliminar(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Error", "Seleccione un evento")
            return

        if messagebox.askyesno("Confirmar", "¿Eliminar evento?"):
            for item in seleccion:
                self.controlador.eliminar_evento(item)

    def mostrar_evento(self, evento):
        self.tree.insert("", "end", values=evento.to_tuple())

    def eliminar_evento(self, item):
        self.tree.delete(item)