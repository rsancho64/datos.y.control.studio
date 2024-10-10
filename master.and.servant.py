#! /usr/bin/python3

import random

def servant(datos, urgente=False):
    """
    acepta control descendente de peticion urgente
    emite control ascendente de buena disposicion (aleatoria)
    acepta datos descendentes
    emite datos acendentes
    """
    if random.randint(0,1):
        willing = True
    else:
        willing = False
        print("servant: sin ganas")        
    if urgente:
        print("servant: oido urgente")
        print("servant: done!!")
    print("servant: recibidos datos: ", datos)
    answ = ["carne hecha"]   # datos ascendentes
    answ.append(willing)
    return answ  # ++ control ascendente

def master():
    # retornos = servant("4 kg de carne")     # peticion de servicio normal
    retornos = servant("4 kg de carne",True) # peticion de servicio urgente
    if retornos[1] == False:  ## no tenia ganas,, mas gratitud
        print("master: thanks to servant!")
    print("master: recibida: ", retornos[0] )
    return

if __name__ == "__main__":

    master()