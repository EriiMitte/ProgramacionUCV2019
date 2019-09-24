def valInt(*args):
    """Descripcion de la funcion valInt"""
    isInt = False
    if len(args) == 1:
        if type(args[0]) == type([4]):
            isInt = True
    if len(args) == 2:
        try:
            if args[1][0] < args[1][1]:
                if type(args[1] == type((4))) and len(args[1]) == 2:
                    isInt = args[0] > args[1][0] and args[0] < args[1][1]
                elif type(args[1] == type([4])) and len(args[1]) == 2:
                    isInt = args[0] >= args[1][0] and args[0] <= args[1][1]
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
            if args[1][0] < args[1][1]:
                if type(args[1] == type((4))) and len(args[1]) == 2:
                    isFloat = args[0] > args[1][0] and args[0] < args[1][1]
                elif type(args[1] == type([4])) and len(args[1]) == 2:
                    isFloat = args[0] >= args[1][0] and args[0] <= args[1][1]
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
            if args[1][0] < args[1][1]:
                if type(args[1] == type((4))) and len(args[1]) == 2:

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
        try:
            if type(args[0]) != type([1,2,3,4]):
                isList = False
            elif args[2] == "len":
                if len(args[0]) == args[1]:
                    isList = True
            elif args[2] == "value":
                if len(args[0]) == args[1]:
                    isList = True
            elif (type(args[1]) != type([1,2,3,4]) or type([4])) and type(args[2]) != type("hola"):
                raise TypeError
            else:
                raise ValueError("El tercer argumento solo admite len o value. ")
        except TypeError:
            raise TypeError("Argumento diferente a las combinaciones sugeridas. ")
    return isList
