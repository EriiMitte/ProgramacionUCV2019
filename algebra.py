def vectorP(v_1,v_2):
    """Esta funcion realiza el producto vectorial entre dos vectores dados"""
    product = []
    i = (v_1[1]*v_2[2] - v_1[2]*v_2[1])
    j = (-1)*(v_1[0]*v_2[2] - v_1[2]*v_2[0])
    k = (v_1[0]*v_2[1] - v_1[1]*v_2[0])
    product.append(i)
    product.append(j)
    product.append(k)
    return product

def transpMatriz(list_1):
    """Esta funcion obtiene la transposicion de una matriz dada. """
    m = [list(i) for i in (zip(*list_1))]
    return m
