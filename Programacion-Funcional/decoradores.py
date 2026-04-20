def requerir_autenticacion(func):
    def envoltura(user: str):
        if user.lower() == 'admin':
            return func(user)
        else:
            return 'Acceso denegado.'
    return envoltura

@requerir_autenticacion
def panel_administrador(user: str):
    return f'Bienvenido al panel de control, {user}'

print(panel_administrador('Admin'))
print(panel_administrador('Johnny'))