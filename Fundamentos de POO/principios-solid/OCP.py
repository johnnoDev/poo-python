class Notificador:
    def __init__(self, usuario: str, mensaje: str):
        self.usuario = usuario
        self.mensaje = mensaje
    
    def notificar(self):
        raise NotImplementedError
        """
        Lo que estaría diciendo:
        "Si heredas de esta clase, estás obligado a escribir tu propia versión del método notificar. Si no lo haces y tratas de usarlo, el programa se detendrá con un error".
        """

class NotificadorEmail(Notificador):
    def notificar(self):
        print(f'Enviando mensaje a {self.usuario.email}')

class NotificadorWhatsApp(Notificador):
    def notificar(self):
        print(f'Enviando WhatsApp a {self.usuario.whatsapp}')

class NotificadorSMS(Notificador):
    def notificar(self):
        print(f'Enviando SMS a {self.usuario.sms}')

class NotificadorTwitter(Notificador):
    def notificar(self):
        print(f'Enviando twit a {self.usuario.twitter}')

# notificador = Notificador('Carlos', 'Hola, esto es un mensaje')


    
    