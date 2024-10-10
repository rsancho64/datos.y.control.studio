#! /usr/bin/python3

import random

def servant(urgente=False):
    """
    acepta control descendente de peticion urgente
    emite control ascendente de buena disposicion (aleatoria)
    """
    if random.randint(0,1):
        willing = True
    else:
        willing = False
        print("servant: sin ganas")        
    if urgente:
        print("servant: oido urgente")
        print("servant: done!!")
    return willing

def master():
    # status = servant()     # peticion de servicio normal
    status = servant(True) # peticion de servicio urgente
    if status == False:  ## no tenia ganas,, mas gratitud
        print("master: thanks to servant!")
    return

if __name__ == "__main__":

    master()