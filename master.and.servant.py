#! /usr/bin/python3

import random

def doblador(dato, urgente=False):
    """
    acepta control descendente de peticion urgente
    emite control ascendente de buena disposicion (aleatoria)
    acepta dato descendentes
    emite dato acendentes
    """
    if random.randint(0,1):
        willing = True
    else:
        willing = False
        print("doblador: sin ganas")        
    if urgente:
        print("doblador: oido urgente")
        print("doblador: done!!")
    salida = dato*2 # datos ascendentes
    print(f"doblador: recibido: {dato}; emitido: {salida}")
    answ = []
    answ.append(salida)
    answ.append(willing)
    return answ  # ¿datos y control?  .. que remedio

def master():
    # todo .... 
    retornos = doblador(4)   # peticion de servicio normal
    # retornos = doblador(4 ,True) # peticion urgente
    if retornos[1] == False:  ## no tenia ganas,, mas gratitud
        print("master: thanks to doblador!")
    print("master: recibida: ", retornos[0] )
    return

if __name__ == "__main__":

    master()