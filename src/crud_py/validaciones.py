def validacion_vacio_w(X):
    if X == "":
        print("El campo no puede estar vacio.")
        return True
    return False


def validacion_num_w(X):
    if any(c.isdigit() for c in X):
        print("No puede contener números.")
        return True
    return False


def validacion_notnum_w(X):
    if not any(c.isdigit() for c in X):
        print("El valor debe ser numerico.")
        return True
    return False


def validacion_none_w(X):
    if X is None:
        print("Usuario no existente.")
        return True
    return False


def validacion_vacio(X):
    if X == "":
        print("Credenciales incorrectas...")
        return True
    return False


def validacion_none(X):
    if X is None:
        print("Credenciales incorrectas...")
        return True
    return False
