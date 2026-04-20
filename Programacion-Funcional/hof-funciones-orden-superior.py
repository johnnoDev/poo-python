# Higher-Order Function

def requerir_autenticacion(func):
    def envoltura(user: str):
        if user.lower() == 'admin':
            return func(user)
        else:
            return 'Acceso denegado.'
    return envoltura

def panel_administrador(user: str):
    return f'Bienvenido al panel de control, {user}'

autenticacion = requerir_autenticacion(panel_administrador)
print(autenticacion('Admin'))
print(autenticacion('Invitado'))

