import json

#clase creada para guardar datos para el acta

class EvaluacionEstudiante:

    def __init__(self) -> None:
        super().__init__()

        # Datos de toda evaluacion
        self.calificacion = []
        self.id_estudiante = ""
        self.periodo = ''
        self.nombre_autor = ""
        self.nombre_trabajo = ""
        self.tipo_trabajo = ""
        self.nombre_director = ""
        self.nombre_codirector = "No aplica"
        self.enfasis = ''
        self.nombre_jurado1 = " "
        self.nombre_jurado2 = " "
        self.inicilizar = 0
        self.nota = 0.0
        self.comentario_final = ""
        self.correciones = ""
        self.recomendacion = ''


    def guardar_calificaciones(self):
        lista = []
        for calificaciones in self.calificacion:
            lista.append(calificaciones.crear_dic())
        return lista

