import datetime


class Reloj:
    formato_fecha = '%A, %B %d, %Y'
    formato_hora = '%I:%M:%S %p'

    def __init__(self, **kwargs):
        self.zona_horaria = datetime.timezone(
            datetime.timedelta(
                hours=kwargs.get('zona_horaria', 0)
            )
        )
        self.lugar = kwargs.get('lugar', 'Greenwich')

    def __str__(self):
        datos = {
            'fecha': self.get_fecha_formato(),
            'hora': self.get_hora_formato()
        }
        return "{fecha} {hora}".format(**datos)

    def get_fecha_formato(self):
        return "{}".format(self.get_fecha().strftime(self.formato_fecha))

    def get_hora_formato(self):
        return "{}".format(self.get_hora().strftime(self.formato_hora))

    def get_fecha(self):
        return datetime.datetime.now(self.zona_horaria).date()

    def get_hora(self):
        return datetime.datetime.now(self.zona_horaria).time()
