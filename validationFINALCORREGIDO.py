def valInt(*args):
    """Descripcion de la funcion valInt"""
    isInt = False
    if len(args) == 1:
        if type(args[0]) is int:
            isInt = True
    if len(args) == 2:
        try:
            if args[1][0] < args[1][1]:
                if type(args[1]) is tuple and len(args[1]) is 2:
                    isInt = args[0] > args[1][0] and args[0] < args[1][1]
                elif type(args[1]) is list and len(args[1]) is 2:
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
            isFloat = True
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

def valComplex(*args):
    isComplex = False
    complejo = args[0]
    if len(args) == 1:
        if type(args[0]) is complex:
            isComplex = True
    if len(args) == 2:
        try:
            if args[1][0] < args[1][1]:
                if type(args[1] == type((4))) and len(args[1]) == 2:
                    isComplex = ((complejo.real)**2 + (complejo.imag)**2)**0.5 > args[1][0] and ((complejo.real)**2 + (complejo.imag)**2)**0.5 < args [1][1]
                elif type(args[1] == type([4])) and len(args[1]) == 2:
                    isComplex = (((complejo.real)**2 + (complejo.imag)**2)**0.5) >= args[1][0] and ((complejo.real)**2 + (complejo.imag)**2)**0.5 <= args [1][1]
            else:
                raise ValueError("El segundo argumento no esta ordenado de manera creciente. ")
        except TypeError:
            raise TypeError("El segundo argumento no es de tipo lista ni tupla. ")
    return isComplex

def valList(*args):
    isList = False
    if len(args) == 1:
        if type(args[0]) is list:
            isList = True
    if len(args) == 3:
        try:
            if type(args[0]) != type([1,2,3,4]):
                isList = False
            elif args[2] == "len":
                if len(args[0]) == args[1]:
                    isList = True
            elif args[2] == "value":
                if args[0] == args[1]:
                    isList = True
            elif (type(args[1]) is not list or type(args[1]) is not int) and type(args[2]) is not str:
                raise TypeError("El segundo argumento solo admite enteros o listas. ")
            else:
                raise ValueError("El tercer argumento solo admite len o value. ")
        except TypeError:
            raise TypeError("Argumento diferente a las combinaciones sugeridas. ")
    return isList
