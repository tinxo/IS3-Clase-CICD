def suma(a, b):
    """ Función que realiza una suma de dos argumentos

    Args:
        a (int/float): argumento a
        b (int/float): argumento b

    Returns:
        int/float: resultado de la suma
    """
    try:
        num_a = int(a)
        num_b = int(b)
    except TypeError:
        return None
    except ValueError:
        return None
    if num_a == None or num_b == None:
        return None
    else:
        return num_a + num_b
    