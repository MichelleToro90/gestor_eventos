from modelo.evento import Evento

class ControladorEventos:
    def __init__(self, vista):
        self.vista = vista
        self.eventos = []

    def agregar_evento(self, fecha, hora, descripcion):
        evento = Evento(fecha, hora, descripcion)
        self.eventos.append(evento)
        self.vista.mostrar_evento(evento)

    def eliminar_evento(self, item):
        self.vista.eliminar_evento(item)