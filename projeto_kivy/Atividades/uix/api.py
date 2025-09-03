def autenticar_usuario(usuario, senha):
    """
    API fake que simula validação de login.
    """
    usuarios = {
        "lucas": "1234",
        "admin": "admin",
        "Morales": "morales123"
    }

    return usuarios.get(usuario) == senha