class Evento:
    def __init__(self, fecha, hora, descripcion):
        self.fecha = fecha
        self.hora = hora
        self.descripcion = descripcion

    def to_tuple(self):
        return (self.fecha, self.hora, self.descripcion)