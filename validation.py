def valInt(*args):
    """Descripcion de la funcion valInt"""
    isInt = False
    if len(args) == 1:
        if type(args[0]) == type([4]):
            isInt = True
    if len(args) == 2:
        #try:
            if type(args[0]) == type([4]):
                if type(args[1]) == (type([1,9]) or type((1,9))):
                    if type(args[1]) == type((1,5)):
                        list = []
                        for i in range[1,20]:
                            if type(args[1]) < type(args[1]):
                                isInt = True
                            else:
                                #isVal = False
            else:
                raise ValueError("El segundo argumento no esta ordenado de manera creciente. ")
        except TypeError:
            raise TypeError("El segundo argumento no es de tipo lista ni tupla. ")
    return isInt

def valFloat(*args):
    """Descripcion de la funcion valFloat"""
    isFloat = False
    if len(args) == 1:
        if type(args[0]) == type([1.5]):
            isInt = True
    if len(args) == 2:
        try:
        #    if:
            else:
                raise ValueError("El segundo argumento no esta ordenado de manera creciente. ")
        except TypeError:
            raise TypeError("El segundo argumento no es de tipo lista ni tupla. ")
    return isFloat

def ValComplex(*args):
    isComplex = False
    complex = args[0]
    if len(args) == 1:
        if type(args[0]) == type([2+3j]):
            isFloat = True
    if len(args) == 2:
        try:
            if:
            else:
                raise ValueError("El segundo argumento no esta ordenado de manera creciente. ")
        except TypeError:
            raise TypeError("El segundo argumento no es de tipo lista ni tupla. ")

def valList(*args):
    isList = False
    if len(args) == 1:
        if type(args[0]) == type([1,2,3,4]):
            isList = True
    if len(args) == 3:
        try
